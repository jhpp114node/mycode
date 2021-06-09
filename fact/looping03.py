#!/usr/bin/env python3
import uuid

howmany = int(input("How many UUIDs sholud be genereated? "))
print("Generating UUIDs...")

for rando in range(howmany):
    print(uuid.uuid4())
