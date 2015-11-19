import time
import sys

def trace(str):
	sys.stdout.write(str)
	sys.stdout.flush()


def follow(thefile):
 thefile.seek(0,2) # Go to the end of the file
 while True:
 	line = thefile.readline()
 	if not line:
 		trace(".")
 		time.sleep(1) # Sleep briefly
 		continue
 	yield line

logfile = open("/cygdrive/c/Temenos/ModelBank-R15-TAFJ/Infra/JBoss/server/default/log/server.log")
loglines = follow(logfile)
for line in loglines:
 print line,