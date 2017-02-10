import requests
from Queue import Queue
from threading import Thread
from time import sleep

class Download(Thread):
	def __init__(self,addr,queue):
		Thread.__init__(self)
		self.addr = addr
		self.queue = queue
	def run(self):
		r = requests.get(self.addr)
		self.queue.put((self.addr,r))	
		print 'download ',self.addr

class Processing(Thread):
	def __init__(self,queue):
		Thread.__init__(self)
		self.queue = queue
	def run(self):
		while True:
			url,r = self.queue.get()
			if url == 1:
				print 'end processing'
				break
			sleep(1)
			print 'processing  ',url

urls=[
	 'http://www.qiushibaike.com/hot',
	 'http://gz.weather.com.cn/zunyi/index.shtml',
	 'http://gz.weather.com.cn/guiyang/index.shtml',
	 'http://baike.baidu.com/link?url=XCCMUgELYLYjBhC4UnKq9GJhxGYvSvcbBNuBNQe_5PIhc0Z33ngBSz5l2-yRTHGU-g8Y6PZ6ZwTGCtgVhBR0CwPaQ3Re90mx9412OD4YaAO',
	 'http://www.cnblogs.com/dkblog/archive/2011/02/24/1980651.html',
]
q = Queue()
threads = [Download(url,q) for url in urls ]
pthread = Processing(q)
for t in threads:
	t.start()
pthread.start()
for t in threads:
	t.join()
q.put((1,None))
