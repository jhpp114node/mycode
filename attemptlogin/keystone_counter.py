#!/usr/bin/env python3
import os
os.chdir("/home/student/mycode/attemptlogin/")
loginfail = 0
keystone_file = open("keystone.common.wsgi", "r")
keystone_file_lines = keystone_file.readlines()

for eachline in keystone_file_lines:
    if "- - - - -] Authorization failed" in eachline:
        loginfail += 1
print("The number of failed log in attempts is", loginfail)
keystone_file.close()
