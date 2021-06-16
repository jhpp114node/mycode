#!/usr/bin/env python3

import paramiko

# send COMANDS to other machines over an SSH connection
# set up paramiko to use keys instead of password

conn = paramiko.SSHClient()

# We need the private key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

# translation alwasys "Yes" to connect into new machine
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# connect
conn.connect(hostname="10.10.2.4", username="fry", pkey=mykey)


conn.exec_command("touch bendersnewfile.txt")

conn.close()
