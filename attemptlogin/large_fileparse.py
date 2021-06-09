#!/usr/bin/env python3
import os

os.chdir("/home/student/mycode/attemptlogin/")
loginfail = 0
keystone_file = open("keystone.common.wsgi", "r")
for line in keystone_file:
    if "- - - - -] Authorization failed" in line:
        loginfail += 1
print("The number of failed log in attempt is", loginfail)
keystone_file.close()
