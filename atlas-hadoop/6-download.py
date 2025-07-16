#!/usr/bin/env python
from snakebite.client import Client
import os

def download(l):


    # local_path = "/tmp/" + os.path.basename(l[0]) 
    # hdfs_path = "".join(l)
    client = Client('localhost', 9000)
    responses = list(client.copyToLocal(l, '/tmp'))
    print(responses[0])
