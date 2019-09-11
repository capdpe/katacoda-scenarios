from datetime import datetime
print datetime.now()
startFile = open("/tmp/start.txt", "w")
startFile.write(str(datetime.now()))
startFile.close()
