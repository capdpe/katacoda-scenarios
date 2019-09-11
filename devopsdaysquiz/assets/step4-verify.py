#!/usr/bin/python

import json
import os
from datetime import datetime
print datetime.now()

os.system("kubectl get deployments -ojson > q4-deployments.json")
with open('q4-deployments.json') as json_file:
    data = json.load(json_file)

count = 0

for item in data['items']:
    if item['metadata']['name'] == 'cka3':
        count = count + 1
        if item['spec']['replicas'] == 5:
            try:
                a = item['spec']['template']['spec']['initContainers']
            except KeyError:
                raise SystemExit(1)


if count == 1:
    startFile = open("/tmp/end.txt", "w")
    startFile.write(str(datetime.now()))
    startFile.close()
    print "done"
