import os 
import time

#from time import gmtime, strftime

time_now = time.ctime()

with open(os.path.join('\MyDocuments\Python Scripts','fresh-list'), "r") as fl:
	for line in fl:
		print (line.strip()+ " -- " + time_now)
		time.sleep(1)
