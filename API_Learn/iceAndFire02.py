#!/usr/bin/env python3

# pprint is a standard library i guess?
import pprint
import requests

AOIF_END_POINT = "https://www.anapioficeandfire.com/api/books"


def main():
    # send a http get request
    request_got_response = requests.get(AOIF_END_POINT)

    # decode the response
    response_got_from_request = request_got_response.json()
    # use the pprint
    pprint.pprint(response_got_from_request)


if __name__ == "__main__":
    main()
