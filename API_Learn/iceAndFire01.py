#!/usr/bin/env python3

import requests

AOIF_END_POINT = "https://www.anapioficeandfire.com/api"

def main():
    # send https get to the api
    request_get_data = requests.get(AOIF_END_POINT)

    # decode the response
    got_data = request_get_data.json()
    print(got_data)


if __name__ == "__main__":
    main()
