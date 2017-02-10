#!/usr/bin/env python
# encoding: utf-8

import cv2,struct,os,threading
from threading import Thread,RLock
from select import select
from http.server import BaseHTTPRequestHandler
from socketserver import ThreadingTCPServer
from concurrent.futures import ThreadPoolExecutor

class JpegStreamer(Thread):
    def __init__(self,camera):
        Thread.__init__(self)
        self.cap = cv2.VideoCapture(camera)
        self.pipes = {}
        self.lock = RLock()

    def register(self):
        r,w = os.pipe()
        self.lock.acquire()
        self.pipes[r] = w
        self.lock.release()
        return r

    def unregister(self,r):
        w = self.pipes[r]
        os.close(r)
        os.close(w)
        self.lock.acquire()
        del self.pipes[r]
        self.lock.release()

    def capture(self):
        while self.cap.isOpened():
            ret,frame = self.cap.read()
            if ret:
                r,data = cv2.imencode('.jpg',frame,(cv2.IMWRITE_JPEG_QUALITY, 40))
                yield data.tostring()

    def send(self,frame):
        n = struct.pack('l',len(frame))
        self.lock.acquire()
        if len(self.pipes):
            _,pipes,_=select([],iter(self.pipes.values()),[],1)
            for pw in pipes:
                os.write(pw,n)
                os.write(pw,frame)
        self.lock.release()

    def run(self):
        for frame in self.capture():
            self.send(frame)

class JpegRetriever(object):
    def __init__(self,streamer):
        self.streamer = streamer
        self.local = threading.local()
        print ('init retriver')

    def retriever(self):
        while True:
            ns = os.read(self.local.pipe,8)
            n = struct.unpack('l',ns)[0]
            data = os.read(self.local.pipe,n)
            yield data

    def __enter__(self):
        if hasattr(self.local,'pipe'):
            raise RuntimeError('local already has pipe attr')
        self.local.pipe = self.streamer.register()
        print('enter retriver')
        return self.retriever()

    def __exit__(self,*args):
        self.streamer.unregister(self.local.pipe)
        del self.local.pipe
        print('exit retriver')
        return True

class Handler(BaseHTTPRequestHandler):
    retriever = None
    @staticmethod
    def setJpegRetriever(retriever):
        Handler.retriever = retriever

    def send_frame(self,frame):
        s = '--abcde\r\n'
        s += 'Content-Type: image/jpeg\r\n'
        s += 'Content-Length: %s\r\n\r\n'%len(frame)
        self.wfile.write(s.encode('ascii'))
        self.wfile.write(frame)

    def do_GET(self):
        if self.retriever is None:
            raise RuntimeError('retriever is none')
        if not self.path =='/':
            return
        self.send_response(200)
        self.send_header('Content-type','multipart/x-mixed-replace;boundary=abcde')
        self.end_headers()

        with self.retriever as frames:
            for frame in frames:
                self.send_frame(frame)

class ThreadingPoolTCPServer(ThreadingTCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True,thread_num=100):
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)
        self.thread_pool = ThreadPoolExecutor(thread_num)

    def process_request(self,request,client_address):
        self.thread_pool.submit(self.process_request_thread,request,client_address)

if __name__ == '__main__':
    streamer = JpegStreamer(0)
    streamer.start()

    retriever = JpegRetriever(streamer)
    Handler.setJpegRetriever(retriever)

    print ('Start server at port: 9000')
    #httpd = ThreadingTCPServer(('',9000),Handler)
    httpd = ThreadingPoolTCPServer(('',9000),Handler,thread_num=2)
    httpd.serve_forever()
