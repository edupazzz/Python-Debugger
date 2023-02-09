from ctypes import *
import time
from os import getpid

msvcrt = cdll.msvcrt
counter = 0

# get pid
_pid = getpid() 
print "# [DEBUG] PID: ", _pid 
while 1:
    msvcrt.printf("Loop iteration %d!\n" % counter)
    time.sleep(2)
    counter += 1