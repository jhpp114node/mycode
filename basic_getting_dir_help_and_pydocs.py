#!/usr/bin/env python3


print(dir(str))
x = "EthGIG01"
print(x.lower())

# print(help(x.lower))
print(x.lower().startswith("eth#"))
\
# below code will throw an error because x.startswith(xxx) returns boolean
# and .lower() is for String
# print(x.startswith("eth").lower())
x = open("./myTestingFiles/read_it.txt", "w")
x.write("hello I am chaing the text in the file - Jun")
