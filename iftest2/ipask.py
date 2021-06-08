#!/usr/bin/env python3
ipchk = input("Apply an IP address: ")
if ipchk == "192.168.70.1":
    print("Looks like the IP address was set: " + ipchk + " not recommended..")
elif ipchk:
    print("Lloks like the IP address was set: " + ipchk)
else:
    print("You did not provide input")
