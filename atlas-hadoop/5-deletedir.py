#!/usr/bin/env python
from snakebite.client import Client


def deletedir(l):
    # Initialize the HDFS client (adjust host and port as needed)
    client = Client('localhost', 9000)

    # reversing list
    l.sort(reverse=True)

    # remove the directory in HD
    responses = client.delete(l, recurse=True)
    
    for response in responses:
        print(response)
