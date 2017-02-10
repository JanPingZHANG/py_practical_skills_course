import tarfile
import requests
from Queue import Queue
from threading import Thread,Event
from time import sleep
import os

class Download(Thread):
	def __init__(self,addr,queue):
		Thread.__init__(self)
		self.addr = addr
		self.queue = queue
	def run(self):
		r = requests.get(self.addr)
		self.queue.put((self.addr,r.content))	
		print 'download ',self.addr

class Processing(Thread):
	def __init__(self,queue,event):
		Thread.__init__(self)
		self.queue = queue
		self.event = event
	def run(self):
		while True:
			url,r = self.queue.get()
			if url == 1:
				self.event.set()
				print 'end processing'
				break
			l = url.split('/')
			f = open(l[len(l)-1],'w')
			f.write(r)
			f.close()
			sleep(1)
			print 'processing  ',url

class TarHtml(Thread):
	def __init__(self,event,filename):
		Thread.__init__(self)
		self.event = event
		self.filename = filename
		#self.setDaemon(True)
	
	def run(self):
		self.event.wait()
		tf = tarfile.open(self.filename,'w:gz')
		for f in os.listdir('.'):
			if not f.endswith('.py'):
				tf.add(f)
		tf.close()
		if not tf.members:
			os.remove(self.filename)
		for f in os.listdir('.'):
			if not (f.endswith('.py') or f.endswith('.tar.gz')):
				os.remove(f)

urls=[
	 'http://www.qiushibaike.com/hot',
	 'http://gz.weather.com.cn/zunyi/index.shtml',
	 'http://gz.weather.com.cn/guiyang/index.shtml',
	 'http://www.cnblogs.com/dkblog/archive/2011/02/24/1980651.html',
]
q = Queue()
threads = [Download(url,q) for url in urls ]
event = Event()
pthread = Processing(q,event)
tarthread = TarHtml(event,'htmls.tar.gz')
for t in threads:
	t.start()
pthread.start()
tarthread.start()
for t in threads:
	t.join()
q.put((1,None))

