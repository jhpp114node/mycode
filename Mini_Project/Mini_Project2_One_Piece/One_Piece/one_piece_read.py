#!/usr/bin/env python3
# open the file
dash = "=" * 70
onepiece_character_list = []

with open ("./Onepiece_data/onepice_fruits.txt") as onepiece_devil_fruit_file:
    for each_character in onepiece_devil_fruit_file:
        onepiece_character_list.append(each_character.strip('\n'))

# get total number of characters
def getTotalNumberOfCharacter(onepiece_character_list):
    remove_header = onepiece_character_list[1:]
    return len(remove_header)

# display header
def displayHeader(one_piece_data, optional_len = 0):
    print(dash * 3)
    headers = one_piece_data[0].split(",")
    # print(headers)
    for each_header in headers:
        print("{:<30s}".format(each_header), end=" ")
    if optional_len == 0:
        print("\n"+"Total # Characters " + str(getTotalNumberOfCharacter(one_piece_data)) + " Found" + dash*3)
    else:
        print("\n"+"Total # Characters " + str(optional_len) + " Found" + dash * 3)

def displayAllCharacters(one_piece_data):
    displayHeader(one_piece_data)
    all_characters = one_piece_data[1:]
    for each_character in all_characters:
        each_character_info = each_character.split(',')
        for each_info in each_character_info:
            print("{:<31s}".format(each_info), end="")
        print()

# search function
def searchByName(one_piece_data):
    all_one_piece_chars = one_piece_data[1:]
    try:
        user_search_keyword = input("Let's search character by name!\n> ").strip().lower()
        # print(user_search_keyword)
        if user_search_keyword.isnumeric():
            raise ValueError
        else:
            foundByName = findByParamForName(all_one_piece_chars, user_search_keyword)
        if len(foundByName) == 0:
            print("I cannot get any matching or even partially matching character(s)..")
        else:
            displayHeader(one_piece_data, len(foundByName))
            for each_found_character in foundByName:
                # print(each_found_character)
                for each_character_info in each_found_character:
                    print("{:<31s}".format(each_character_info), end="")
                print()
    except ValueError:
        print("Invalid Input...")


# util function for search by name
def findByParamForName(one_piece_data_set, one_piece_param):
    target_character = []
    for each_character in one_piece_data_set:
        each_character_name = each_character.split(',')
        # if found it then return the name of the character name
        # print(one_piece_param.lower())
        if one_piece_param.lower() == each_character_name[0].lower():
            target_character.append(each_character_name)
            return target_character
    # ============= NOT FOUND CASE ===============
    # if not found then get the most matching data
    # some edge case
    if len(one_piece_param) == 1:
        for each_character in one_piece_data_set:
            each_character_name = each_character.split(',')
        # if found it then return the name of the character name
        if each_character_name[0].lower().startswith(one_piece_param.lower()):
            target_character.append(each_character_name)
            return target_character

    # print(target_character)
    for index in range(len(one_piece_param), 0, -1):
        # print("in?")
        partial_param_name =  one_piece_param[0:index]
        # print(partial_param_name)
        for each_character_infos in one_piece_data_set:
            each_character_names = each_character_infos.split(',')
            # checks for partial
            if each_character_names[0].lower().startswith(partial_param_name.lower()):
                target_character.append(each_character_names)
        if (len(target_character) > 0):
            return target_character
    return target_character

# search by name of devil fruit
def searchByDevilFruit(one_piece_data):
    all_one_piece_chars = one_piece_data[1:]
    try:
        user_search_devil_fruit = input("Let's search character by the devil Fruit\n> ")
        if user_search_devil_fruit.isnumeric():
            raise ValueError
        else:
            foundByDevilFruit = findByParamForDevilFruit(all_one_piece_chars, user_search_devil_fruit)
            if len(foundByDevilFruit) == 0:
                print("I cannot get any matching or even partially matching character(s)..")
            else:
                displayHeader(one_piece_data, len(foundByDevilFruit))
                for each_found_character in foundByDevilFruit:
                    # print(each_found_character)
                    for each_character_info in each_found_character:
                        print("{:<31s}".format(each_character_info), end="")
                    print()
    except ValueError:
        print("Invalid input")

# util search devil fruit name
def findByParamForDevilFruit(one_piece_data_set, target_devil_fruit):
    print("From Find by Fruit name")
    target_devil_fruit_result = [];
    for each_data_set in one_piece_data_set:
        each_character_data = each_data_set.split(',')
        # Suna
        if each_character_data[1].lower().startswith(target_devil_fruit.lower()):
            target_devil_fruit_result.append(each_character_data)
    if len(target_devil_fruit_result) > 0:
        return target_devil_fruit_result

    # if cannot find any exact matching then find partial
    if len(target_devil_fruit) == 1:
        for each_character in one_piece_data_set:
            each_character_devil_fruit = each_character.split(',')
        # if found it then return the name of the character name
        if each_character_devil_fruit[1].lower().startswith(target_devil_fruit.lower()):
            target_devil_fruit_result.append(each_character_devil_fruit)
            return target_devil_fruit_result

    # finding the besting partial matching data
    for index in range(len(target_devil_fruit), 0, -1):
        # print("in?")
        partial_param_devil_fruit =  target_devil_fruit[0:index]
        # print(partial_param_name)
        for each_character_infos in one_piece_data_set:
            each_character_info = each_character_infos.split(',')
            # checks for partial
            if each_character_info[1].lower().startswith(partial_param_devil_fruit.lower()):
                target_devil_fruit_result.append(each_character_info)
        if (len(target_devil_fruit_result) > 0):
            return target_devil_fruit_result
    return target_devil_fruit_result

