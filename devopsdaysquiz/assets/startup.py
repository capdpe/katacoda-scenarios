import subprocess
import time
from datetime import datetime

p = subprocess.Popen(['sleep', '5'])
print 'Starting Up'
while p.poll() is None:
    print('Still starting')
    time.sleep(8)

print "Startup Complete! Click next. The timer will start as soon as the first question loads"
