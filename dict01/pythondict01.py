#!/usr/bin/env python3
## create a dictionary
switch = {
    "hostname": "sw1",
    "ip": "10.0.1.1",
    "version": "1.2",
    "vendor": "cisco"
}

## display parts of the dictionary
print( switch["hostname"] )
print( switch["ip"] )

## request a 'fake' key
# This returns an error
# print( switch["lynx"] )

print("First test - get()")
# this returns None
print(switch.get("lynx"));

print ("Second test - get()")
# so the `get()` second param is error message
print(switch.get("lynx", "The key is another castle"));

print("Third test - get()")
print(switch.get("version"))

print("Fourth test .keys()")
print(switch.keys())

print("Fifth test .values()")
print(switch.values())

# ================= POP =======================
print("Sixth test .pop()")
switch.pop("version")
print(switch.keys())
print(switch.values())
# ================ ADD ========================
print("Seventh test - add")
switch["adminlogin"] = "karl08"
print(switch.keys())
print(switch.values())
switch.update({"password": "qwerty"})
print(switch.keys())
print(switch.values())
# ================= CLEAR =====================


