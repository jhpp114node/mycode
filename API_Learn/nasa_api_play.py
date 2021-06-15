#!/usr/bin/env python3

# allow the user to pass in both start_date and end_date
# as input!
# use that input as query param for the API call

# Basic - Return the following info:
# how many asteroids are being returned?

# Advanced - Return the following info:
# how many asteroids are potentially hazardous?

# Danger - Return the following info:
# What is the size of the biggest asteriod?
# What asteroid came closest to earth?
# what is the fastest speed of the asteriod in this rnage?

import requests


NASAAPI = "https://api.nasa.gov/planetary/apod?"
SOME_SHTTY_END_POINT = "https://api.nasa.gov/neo/rest/v1/feed?"


def return_creds():
    with open("nasa.creds") as mycred:
        nasa_creds = mycred.read()
        # remove any "extra" new line
        nasa_creds = "api_key=" + nasa_creds.strip("\n")
        return nasa_creds


def return_potential_hazardous_count(dataJSON):
    # print("got here")
    counter = 0
    try:
        if len(dataJSON.get("near_earth_objects")):
            # print("got here2")
            near_earth_object = dataJSON.get("near_earth_objects")
            # print(near_earth_object)
            for key in near_earth_object:
                # print(key)
                for each_index in range(len(near_earth_object.get(key))):
                    # print(each_index)
                    # print(near_earth_object.get(key)[each_index].get("is_potentially_hazardous_asteroid"))
                    if near_earth_object.get(key)[each_index].get("is_potentially_hazardous_asteroid"):
                        counter += 1
            return counter
        else:
            raise KeyError

    except KeyError:
        print("Does not exist")


# What is the size of the biggest asteriod?
def return_biggest_asteriod(dataJSON):
    max = -99999
    try:
        # estimated_diameter is the one determine the biggest?
        if len(dataJSON.get("near_earth_objects")):
            # print("got here2")
            estimated_diameter = dataJSON.get("near_earth_objects")
            # print(near_earth_object)
            for key in estimated_diameter:
                # key is the dates
                # print(key)
                for each_index in range(len(estimated_diameter.get(key))):
                    # print(each_index)
                    # use max-meter
                    # print(estimated_diameter.get(key)[each_index].get("estimated_diameter").get("meters").get("estimated_diameter_max"))
                    if estimated_diameter.get(key)[each_index].get("estimated_diameter").get("meters").get("estimated_diameter_max") > max:
                        max = estimated_diameter.get(key)[each_index].get("estimated_diameter").get("meters").get("estimated_diameter_max")
            return max
        else:
            raise KeyError

    except KeyError:
        print("Does not exist")


# What asteroid came closest to earth?
def return_closest_to_earth(dataJSON):
    closest = 9999999999
    name_of_object = ''
    result = ''
    try:
        # estimated_diameter is the one determine the biggest?
        if len(dataJSON.get("near_earth_objects")):
            # print("got here2")
            close_approach_data = dataJSON.get("near_earth_objects")
            # print(near_earth_object)
            for key in close_approach_data:
                # key is the dates
                # print(key)
                for each_index in range(len(close_approach_data.get(key))):
                    # print(each_index)
                    # use max-meter
                    # print(close_approach_data.get(key)[each_index].get("close_approach_data"))
                    clost_approach_list = close_approach_data.get(key)[each_index].get("close_approach_data")
                    for each_approach in range(len(clost_approach_list)):
                        each_miss_distance = close_approach_data.get(key)[each_index].get("close_approach_data")[each_approach].get("miss_distance").get("lunar")
                        # small number get minimum missing distance (means the closest)
                        if float(each_miss_distance) < closest:
                            closest = float(each_miss_distance)
                            name_of_object = close_approach_data.get(key)[each_index].get("name")
                            # print(name_of_object)
                            result = f"name: {name_of_object}, distance: {closest} lunar"

            return result
        else:
            raise KeyError

    except KeyError:
        print("Does not exist")


def main():
    # define creds
    try:
        starting_date = input("Enter the stating date in format(YYYY MM DD; eg. 2021-06-08)\n > ")
        ending_date = input("Enter the ending date in format(YYYY MM DD; eg. 2021-06-08)\n > ")
        # replace space with -
        starting_date.strip()
        ending_date.strip()
        # set up the starting date and ending date
        trimmed_starting_date = f"start_date={starting_date}"
        trimmed_ending_date = f"end_date={ending_date}"
        print(trimmed_ending_date)
        # get api key
        nasa_creds = return_creds()
        print(nasa_creds)
        # call the webservice with our key
        nasa_response_data = requests.get(f"{SOME_SHTTY_END_POINT}{nasa_creds}&{trimmed_starting_date}&{trimmed_ending_date}").json()
        # how many asteroids are being returned?
        print(nasa_response_data.get("element_count"))
        # how many asteroids are potentially hazardous?
        # print(f"Potential Hazard count: {return_potential_hazardous_count(nasa_response_data)}")
        # # What is the size of the biggest asteriod?
        print(f"Biggest: {return_biggest_asteriod(nasa_response_data)} m")
        # What asteroid came closest to earth?
        print(f"Closest: {return_closest_to_earth(nasa_response_data)}")
    except Exception:
        print("So boring")


if __name__ == "__main__":
    main()
