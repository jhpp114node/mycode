#!/usr/bin/env python3
# pip3 install paramiko
# sudo docker ps
import getpass
import paramiko

# transfer a file from bchd to bender

# an object that represents where files/dirs can be trasported to

t = paramiko.Transport("10.10.2.3", 22)

# Where to go, but we do not know How to access
t.connect(username="bender", password=getpass.getpass())

# we want to trasnfer a FILE, so we need an SFTP connection!
sftp =  paramiko.SFTPClient.from_transport(t)

## copy our firstpasswd.py script to bender
sftp.put("firstpasswd.py", "firstpasswd.py") # move file to target location home directory
    
## close the connection
sftp.close() # close the connection

