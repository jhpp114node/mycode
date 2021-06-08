#!/usr/bin/env python3

# standard library imports
import shutil
import os

# main function
def main():
    os.chdir('/home/student/mycode/') # setting up the default directory
    shutil.move('raynor.obj', 'ceph_storage/') # move raynor obj to ceph_storage directory

    xname = input("What is the new name for kerrigan.obj") # setting name for the new obj name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # override the file

main() # this calls the main function
