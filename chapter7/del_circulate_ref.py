#-*-coding:utf8-*-
class Test(object):
    def __init__(self,data,owner):
        self.data = data
        self.owner = owner
    def __del__(self):
        print 'in __del__ test'

#d = Test(1,2)
#del d

class Data(object):
    def __init__(self,data,owner):
        self.data = data
        self.owner = owner

    def __del__(self):
        print 'in data del'
        

class Node(object):
    def __init__(self,data):
        self.data = Data(data,self)

    def __del__(self):
        print 'in Node del'

'''
node = Node(3)
print node.data
#del node.data
del node
'''

import weakref #不会增加引用计数

class Data_del(object):
    def __init__(self,data,owner):
        self.data = data
        self.owner = weakref.ref(owner)

    def __del__(self):
        print 'in data del'

    def __str__(self):
        return str(self.data)+' owner:'+str(self.owner())

class Node_del(object):
    def __init__(self,data):
        self.data = Data_del(data,self)

    def __del__(self):
        print 'in Node del'

#'''
node = Node_del(1)
print node.data
del node
#'''
