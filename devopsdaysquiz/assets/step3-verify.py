from datetime import datetime

with open('db-secret.yaml') as f:
    if 'db-user-pass' in f.read():
        endFile = open("/tmp/end.txt", "w")
        endFile.write(str(datetime.now()))
        endFile.close()
        print("done")
