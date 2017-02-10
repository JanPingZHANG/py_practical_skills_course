from random import randint,choice
from create_random_str import create_random_str
import csv
import string

headers = ['name','age','grade','bloodPressure']
filenames = ['test1.csv','test2.csv','test3.csv']
row_count = 100

for filename in filenames:
	wf = open(filename,'wb')
	writer=csv.writer(wf)
	writer.writerow(headers)
	for i in range(row_count):
	    row = []
	    row.append(create_random_str(randint(5,10)))
	    row.append(randint(6,18))
	    row.append(randint(1,12))
	    row.append(randint(800,8000))
	    writer.writerow(row)
	wf.close()

