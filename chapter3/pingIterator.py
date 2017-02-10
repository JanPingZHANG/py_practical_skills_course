import requests
from collections import Iterator,Iterable

def ping(address):
	r = requests.get(address)
	return r.status_code

class PingIterator(Iterator):
	def __init__(self,addresses):
		self.addresses = addresses
		self.index = 0
	def next(self):
		if self.index == len(self.addresses):
			raise StopIteration
		else:
			address = self.addresses[self.index]
			status_code = ping(address)
			self.index = self.index +1
			return address+': '+str(status_code) 

class PingIterable(Iterable):
	def __init__(self,addresses):
		self.addresses = addresses
	def __iter__(self):
		return PingIterator(self.addresses)

addrs = ['http://www.qiushibaike.com/hot',
				'http://gz.weather.com.cn/zunyi/index.shtml',
				'http://gz.weather.com.cn/guiyang/index.shtml',
				'http://baike.baidu.com/link?url=XCCMUgELYLYjBhC4UnKq9GJhxGYvSvcbBNuBNQe_5PIhc0Z33ngBSz5l2-yRTHGU-g8Y6PZ6ZwTGCtgVhBR0CwPaQ3Re90mx9412OD4YaAO',
				'http://www.cnblogs.com/dkblog/archive/2011/02/24/1980651.html',
				'https://www.baidu.com/s?wd=requests%E8%8E%B7%E5%BE%97%E7%9A%84%E9%A1%B5%E9%9D%A2%E6%80%8E%E4%B9%88%E7%94%A8xpath&rsv_spt=1&rsv_iqid=0xa6056f640009703d&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=42&rsv_sug1=6&rsv_sug7=100&rsv_t=82afOOhwvwrMnPtEWvHPj3GFcGIPF%2BXAdA4Pka5QyJbk%2BBhtgOXPq4TMeL6UUXfLf19H&rsv_sug2=0&inputT=13146&rsv_sug4=13147',
				]
cls = PingIterable(addrs)
#cls = PingIterator(addrs) #also can run
for i in cls:
	print i
