#!/usr/bin/python

import json
import os
import os.path
import csv
os.system("kubectl get pods -o=json > q2pods.json")
os.system("kubectl get svc cache -ojson > q2svccache.json")

podReplicas = 0
podReplicaPass = False
svcExposePass = False
endpointJSONPass = False
sortedTxtPass = False
sortedTxtNames = []

with open('q2pods.json') as podlist:
    pods = json.load(podlist)
with open('q2svccache.json') as svccache:
    service = json.load(svccache)
with open('q2.json') as q2json:
    endpointJSON = json.load(q2json)
import csv


def sortedTxt(csv_file):
    try:
        with open(csv_file) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=' ')
            for row in reader:
                sortedTxtNames.append(row['NAME'])
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return

for pod in pods['items']:
    if ((pod['metadata']['labels']['run'] == 'cache') and (pod['spec']['containers'][0]['image'] == 'memcached') and (pod['metadata']['ownerReferences'][0]['kind'] == 'ReplicaSet')):
        podReplicas = podReplicas + 1

if podReplicas == 5:
    podReplicaPass = True


if service['metadata']['labels']['run'] == 'cache' and service['spec']['ports'][0]['port'] == 11211 and service['spec']['ports'][0]['targetPort'] == 11211:
    svcExposePass = True

if endpointJSON['kind'] == 'Endpoints' and endpointJSON['metadata']['name'] == 'cache':
    endpointJSONPass = True


sortedTxt('q2.txt')

sortedSortedTxtNames = sorted(sortedTxtNames)
sortedTxtPass = True

if podReplicaPass and svcExposePass and sortedTxtPass:
    print "done"
