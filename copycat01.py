#!/usr/bin/env python3
import shutil
import os

# setting the default path
os.chdir("/home/student/mycode/")
# only copy a single file
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy the entire tree
shutil.copytree("5g_research/", "5g_research_backup/")

