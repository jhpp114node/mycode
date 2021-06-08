#!/usr/bin/env python3

hostname = "MTG"
if hostname == "MTG":
    print("The hostname was found to be mtg")

hostname = input("What value should we set for hostname?")
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

print("Exiting the script")
