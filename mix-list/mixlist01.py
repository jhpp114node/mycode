#!/usr/bin/env python3
my_list = ["192.168.0.5", 5060, "UP"]
print(f"The first item in the list (IP): {my_list[0]}")
# you do not have to convert this into str when you using the format
print(f"The second item in the list (PORT): {str(my_list[1])}")
# displaying the third item in the list
print(f"The third item in the list (state): {my_list[2]}")

# Challenge
iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]
# display only the IP on the screen
print(iplist[3])

