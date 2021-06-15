#!/usr/bin/env python3

import json


def main():
    with open("datacenter.json", "r") as datacenter:
        datacenter_string = datacenter.read()
        print(datacenter_string)
        print(type(datacenter_string))

        # loads => str
        # load => dic
        datacenter_decoded = json.loads(datacenter_string)
        # This is now a dictionary
        print(type(datacenter_decoded))
        print(datacenter_decoded)
        print(datacenter_decoded["row3"])
        print(datacenter_decoded["row2"][1])


if __name__ == "__main__":
    main()
