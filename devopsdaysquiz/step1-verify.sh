#!/usr/bin/python

import json
import os

os.system("kubectl get po web --namespace=capgemini -o=json > q1out.py")  
with open('q1out.py') as json_file:
    data = json.load(json_file)

if data['spec']['containers'][0]['image'] == 'nginx:1.16.0' and data['spec']['containers'][0]['name'] == 'web':
	print('done')
