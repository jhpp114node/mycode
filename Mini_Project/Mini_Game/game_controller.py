#!/usr/bin/env python3
import json
# for clear the console
from os import system, name


with open('areas.json', "r+") as areas_file:
    areas = json.load(areas_file)


def clear_screen():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


def display_map():
    print("-"*80)
    with open("map.txt") as map_file:
        for each_line in map_file:
            print(each_line, end="")
    print(f"* Your current location {currentRoom}")


def show_instructions():
    #print a main menu and the commands
    print('''
RPG Game
========
Commands:
go [direction]
get [item]
use [item]
talk
map
status
''')


def show_status():
    # print the player's current status
    print('---------------------------')
    print(f"You are in the {currentRoom}")
    # print the current inventory
    if len(inventory) > 0:
        print("Your inventory:")
        for each_obj in inventory:
            print(f"*{list(each_obj.keys())}")
    else:
        print(f"The inventory is empty")
    # print an item if there is one
    if "item" in areas[currentRoom] and len(areas.get(currentRoom).get("item")[0]) > 0:
        # or key_master_flg
        if areas.get(currentRoom).get("Get_able"):
            print(f"You see item {list(areas.get(currentRoom).get('item')[0].keys())} <- get item_name")
    else:
        print(f"You took it all items in {currentRoom}")
    # NPC
    if "NPC" in areas.get(currentRoom):
        print(f"NPC name: [{areas.get(currentRoom).get('NPC')['name']}] available. <- talk")
    print("---------------------------")


currentRoom = "Garden"
inventory = []

# main controller
show_instructions()
instructions_list = ("go", "get", "talk", "map", "status", "use")
move_instruction_list = ("south", "east", "north", "west")
key_master_flg = False
isWon = False
while True:
    show_status()
    try:
        user_instruction = input("> ").lower()
        # input validation
        if not user_instruction.startswith(instructions_list):
            raise ValueError
        # after validate the input
        instruction_split = user_instruction.split(" ", 1)
        # conditions for [go get talk map status]
        if instruction_split[0] == "go":
            if instruction_split[1] in move_instruction_list and areas.get(currentRoom).get(instruction_split[1]):
                currentRoom = areas.get(currentRoom).get(instruction_split[1])
                if currentRoom == 'The Main Hall':
                    print("The Castle: ??? You think you can get into the Main Hall?")
                    print("The Castle: You Shall Not Pass!!")
                    print("The Castle: To get into the hall, you need a key!!!")
                    currentRoom = "The Fallen Castle Entrance"
                    # Todo:
                    # update the Get_able to true
                    # now the key shows and I have to update the Key maker's talk
                    areas.get(currentRoom).get("NPC").update({"description": "Ha! I knew you will comback for the key to enter the main hall.\nGood luck..."})
                    key_master_flg = True

            elif instruction_split[1]:
                if currentRoom == "Garden":
                    print("Possible go: south, east")
                elif currentRoom == "Home":
                    print("Possible go: north")
                elif currentRoom == "The Fallen Castle Entrance":
                    print("Possible go: west, south")
                elif currentRoom == "The Main Hall":
                    print("Possible go: north")
                raise KeyError
            else:
                raise IndexError
        elif instruction_split[0] == 'get':
            # print(instruction_split[1])
            # print(areas.get(currentRoom).get("item")[0].keys())
            if "item" in areas.get(currentRoom) and instruction_split[1] in areas.get(currentRoom).get("item")[0].keys():
                # print("it should?")
                print(f"An item found {instruction_split[1]}")
                inventory.append({instruction_split[1]: areas.get(currentRoom).get('item')[0].get(instruction_split[1])})
                del areas.get(currentRoom).get('item')[0][instruction_split[1]]
            else:
                print(f"Cannot find the item: {instruction_split[1]}")
        elif instruction_split[0] == 'talk':
            if instruction_split[1] == 'the key maker':
                if key_master_flg:
                    inventory.append({"Key": areas.get(currentRoom).get('item')[0].get(instruction_split[1])})
                    key_master_flg = False
            if "NPC" in areas.get(currentRoom):
                # print(f"{areas.get(currentRoom).get('NPC')}")
                print(f"{areas.get(currentRoom).get('NPC').get('name')}:"
                      f"\n\t{areas.get(currentRoom).get('NPC').get('description')}")
            elif "NPC" not in areas.get(currentRoom):
                print(f"Cannot find NPC in {currentRoom}")
            else:
                raise ValueError
        elif instruction_split[0] == 'map':
            display_map()
        elif instruction_split[0] == 'status':
            show_status()
        elif instruction_split[0] == 'use':
            # print(instruction_split[1])
            # print(inventory)
            for each_obj in inventory:
                # print(each_obj)
                # print(each_obj.keys())
                if instruction_split[1] == 'key':
                    currentRoom = "The Main Hall"
                    clear_screen()
                    # remove all items
                    inventory.clear()
                    life = 3
                    # create a loop to play the ending game
                    print("You better answer the questions all correctly or you die!")
                    while life > 0:
                        size_of_the_quiz = len(areas[currentRoom].get("quiz"))
                        for i in range(size_of_the_quiz):
                            print(f"Question: {areas[currentRoom].get('quiz')[i].get('question')}")
                            print(f"Choice: {areas[currentRoom].get('quiz')[i].get('choice')}")
                            try:
                                user_answer = int(input("Select your answer!!!\n> "))
                                if user_answer == areas.get(currentRoom).get('quiz')[i].get('answer'):
                                    print("hummmmm...")
                                else:
                                    print("ahhhahhhh")
                                    life -= 1
                            except Exception:
                                print("Invalid answer")
                        if life > 0:
                            isWon = True
                            break
                if each_obj.get(instruction_split[1]):
                    print(f"Using Item [{instruction_split[1]}]:{each_obj.get(instruction_split[1])}")
        if isWon:
            break
    # Exception
    except ValueError:
        print("I cannot understand the instruction..")
    except KeyError:
        print("I cannot understand the instruction...")
    except IndexError:
        print("Index error")

if isWon:
    print("You won")
else:
    print("You lose")


