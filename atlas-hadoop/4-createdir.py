#!/usr/bin/env python
from snakebite.client import Client


def createdir(l):
    # Initialize the HDFS client (adjust host and port as needed)
    client = Client('localhost', 9000)

    # Create the new directory in HD
    responses = client.mkdir(l)
    
    for response in responses:
        print(response)
