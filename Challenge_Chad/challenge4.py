#!/usr/bin/env python3
# farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
#          {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
#          {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# Super Bonus List
farms = [{"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "E Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

# function 1
# write a for loop that returns all the animals from the NE farm
def displayAll_NE_FARM_Animals():
    for eachFarm in farms:
        if eachFarm["name"].lower() == "ne farm":
            print(eachFarm["agriculture"])

# function 2
# ask a user to choose a farm (NE Farm, W Farm, or SE Farm). Return the plants/animals that are raised on that farm
def display_animals_user_input():
    farm_list = ("ne farm", "w farm", "se farm", "e farm")
    try:
        user_input = input("Choose a farm \nNE Farm\nW Farm\nSE Farm\nE Farm\n> ").lower()
        if user_input not in farm_list:
            assert False
        # if valid then
        for eachFarm in farms:
            if eachFarm.get("name").lower() == user_input:
                return eachFarm.get("agriculture")
    except AssertionError:
        print("Not a valid input")

# function 3
# Ask a user to choose a farm (NE Farm, W Farm, or SE Farm)... but only return ANIMALS from that particular farm.

# assume the vegetable never get added
def display_only_animal():
    vege_tuple = ("carrots", "celery", "bananas", "apples", "oranges")
    only_animal = []
    all_list_with_vege = display_animals_user_input()
    for each_list in all_list_with_vege:
        if each_list not in vege_tuple:
            only_animal.append(each_list)
    # print(only_animal)
    return only_animal

# invoke function 1
displayAll_NE_FARM_Animals()

# invoke function 2
returned_animal_plant_list = display_animals_user_input()
print(returned_animal_plant_list)

# invoke function 3
only_animal_list = display_only_animal()
print(only_animal_list)

