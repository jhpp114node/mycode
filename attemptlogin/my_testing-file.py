#!/usr/bin/env python3
import os

fail_counter = 0
success_counter = 0
counter = 0
os.chdir("/home/student/mycode/attemptlogin/")
with open ("keystone.common.wsgi", "r") as kfile:
    for line in kfile:
        if counter == 1:
            print(line.split(" ")[-1])
        if "- - - - -] Authorization failed" in line:
            fail_counter += 1
        elif "-] Authorization failed" in line:
            success_counter += 1
        counter += 1
print(f"Fail counter: {fail_counter}")
print(f"Success counter: {success_counter}")
# I don't think this is right
print(line.split(" ")[-1])
