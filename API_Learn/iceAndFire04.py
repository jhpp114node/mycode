#!/usr/bin/env python3

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"


def main():
    ## Ask user for input
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

    ## Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)

    ## Decode the response
    got_dj = gotresp.json()
    # pprint.pprint(got_dj)
    # this returns a list
    house_info_url = got_dj.get('allegiances')
    print(f"Character name: {got_dj.get('name') if len(got_dj.get('name')) else f'Could not found the name.'}")
    print(f"Character associated books: {list(got_dj.get('books')) if len(got_dj.get('books')) else 'no book associated'}")
    if len(house_info_url) > 0:
        house_info_response = requests.get(house_info_url[0])
        house_info_data = house_info_response.json()
        pprint.pprint(house_info_data)
    if len(got_dj.get('books')) > 0:
        for each_book_link in got_dj.get('books'):
            # print(each_book_link)
            each_book_info_res = requests.get(each_book_link)
            each_book_info = each_book_info_res.json()
            print(f"Selected Character is in {each_book_info.get('name')}")
            print(f"Selected Character is in {each_book_info.get('isbn')}")
    else:
        print("cannot find any house(s) affiliated with the character..")


if __name__ == "__main__":
    main()
