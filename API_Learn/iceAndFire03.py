#!/usr/bin/env python3

import requests

AOIF_END_POINT = "https://www.anapioficeandfire.com/api/books"


def main():
    # get request from api
    got_response = requests.get(AOIF_END_POINT)
    response = got_response.json()

    # loop across repsonse
    for single_book in response:
        # display the names of each book
        print(f"{single_book.get('name')}, page - {single_book.get('numberOfPages')}")
        print(f"\tAPI URL -> {single_book.get('url')}")
        # print ISBN
        print(f"\tISBN -> {single_book.get('isbn')}\n")
        print(f"\tPublisher -> {single_book.get('publisher')}\n")
        print(f"\tNo. of Characters -> {single_book.get('characters')}\n")


if __name__ == "__main__":
    main()
