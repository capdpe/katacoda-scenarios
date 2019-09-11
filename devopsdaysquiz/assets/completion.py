import datetime

with open("/tmp/start.txt","r") as f:
    start = datetime.datetime.strptime(f.readline(),'%Y-%m-%d %H:%M:%S.%f')
with open("/tmp/end.txt","r") as f:
    end = datetime.datetime.strptime(f.readline(),'%Y-%m-%d %H:%M:%S.%f')

data1 = datetime.datetime.now()
data2 = datetime.datetime.now()

diff = end - start

days, seconds = diff.days, diff.seconds
hours = days * 24 + seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

print hours,"hours,",minutes,"minutes and",seconds,"seconds"
