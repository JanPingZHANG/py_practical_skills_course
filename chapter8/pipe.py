#-*-coding:utf8-*-
import os,sys

print 'the child will write text to a pipe '
print 'the parent will read the text written by child'

r,w = os.pipe()

processid = os.fork() #会派生出一个子进程执行后面的代码，原进程也会执行后面的代码
if processid:
	print 'this is parent process ',processid
	os.close(w)
	rf = os.fdopen(r)
	print 'parent process is watting child write'
	txt = rf.read()
	print 'parent read text: ',txt
	rf.close()
	print 'end parent'
	sys.exit(0)
else :
	print 'this is child process ',processid
	os.close(r)
	wf = os.fdopen(w,'w')
	s = 'this text is written by child'
	wf.write(s)
	print 'child write a text: ',s
	wf.close()
	print 'end child'
	sys.exit(0)

