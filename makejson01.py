#!/usr/bin/env python3

# JSON is part of the python standard library
import json

def main():
    # list of object
    hitchhikers = [
        {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        },
        {
            "name": "Arthur Dent",
            "species": "Human"
        }
    ]
    print(hitchhikers)
    # open a new file in write mode
    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)


if __name__ == "__main__":
    main()

