#!/usr/bin/env python3
### Lab 11
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
print(proto[1])
# save as list
# good way to extend data as a list into a single list
proto.extend("dns")
protoa.append("dns")
# expects ssh http https d n s
print(proto)
proto2 = [22, 80, 443, 53]
proto.extend(proto2)
# proto: expects ssh http https d n s 22, 80, 443, 53
print(proto)
# expects ssh http https dns [22, 80, 443, 53]
protoa.append(proto2)
print(protoa)

