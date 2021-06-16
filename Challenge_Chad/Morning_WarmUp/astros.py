#!/usr/bin/env python3
import requests


def main():
    ASTROS_API_END_POINT = "http://api.open-notify.org/astros.json"
    try:
        astros_data_response = requests.get(ASTROS_API_END_POINT)
        astros_data = astros_data_response.json()
        if astros_data.get("message") != "success":
            raise Exception
        print(f"People in Space: {astros_data.get('number')}")
        for each_astro in astros_data.get("people"):
            print(f"{each_astro.get('name')} is on the {each_astro.get('craft')}")
    except Exception:
        print("Fail to connect api")


if __name__ == "__main__":
    main()

