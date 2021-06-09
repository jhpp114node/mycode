#!/usr/bin/env python3
# list 1
vendor = ["cisco", "juniper", "big_ip", "f5", "arista"]
# list 2
approved_vendor = ["cisco", "juniper", "big_ip"]

for x in vendor:
    print("The vendor is:" + x, end="")
    if x not in approved_vendor:
        print("- not an approved vendor", end="")
    print()
print("\nOur loop has ended.")
