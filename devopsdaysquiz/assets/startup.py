import subprocess
import time
from datetime import datetime

p = subprocess.Popen(['minikube', 'start'])
print 'Starting Up'
while p.poll() is None:
    print('Still starting')
    time.sleep(8)

print "Startup Complete! Click next. The timer will start as soon as the first question loads"
startFile = open("/tmp/startupcomplete", "w")
startFile.write(str(datetime.now()))
startFile.close()
