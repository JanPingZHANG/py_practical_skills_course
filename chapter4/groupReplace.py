import re
from time import ctime,sleep

SOURCE = ''
for i in range(5):
	SOURCE = SOURCE + str(ctime()) + '\n'
	sleep(1)
print 'SOURCE: \n',SOURCE
print '-'*30
r = re.sub(r'([a-zA-Z]{3}) ([a-zA-Z]{3})  (\d{1}) (\d{2}:\d{2}:\d{2}) (\d{4})',r'\5 \2 \3 \4 \1',SOURCE)
print r

r = re.sub(r'(?P<week>[a-zA-Z]{3}) (?P<month>[a-zA-Z]{3})  (?P<day>\d{1}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<year>\d{4})',r'\g<year> \g<month> \g<day> \g<time> \g<week>',SOURCE)
print r
