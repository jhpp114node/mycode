#!/usr/bin/env python3

heroes = {
    "wolverine":
        {"real name": "James Howlett",
         "powers": "regeneration",
         "archenemy": "Sabertooth"},
    "harry potter":
        {"real name": "Harry Potter",
         "powers": "magic",
         "archenemy": "Voldemort"},
    "captain america":
        {"real name": "Steve Rogers",
         "powers": "frisbee shield",
         "archenemy": "Hydra"
        }
}

try_again = True
while (try_again):
    char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Captain America)\n>").lower()
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n>").lower()
    hero_name = heroes.get(char_name)
    if hero_name:
        hero_stat = hero_name.get(char_stat)
        if hero_stat:
            print(f"{char_name}'s {char_stat} is: {hero_name.get(char_stat, 'stat cannot be found')}")
            # bonus 1
            print("Bonus 1")
            print(f"{char_name.upper()}'s {char_stat} is: {hero_name.get(char_stat, 'stat cannot be found')}")
        else:
            print("Hero stat is not valid")
    else:
        print("Hero name not valid")
    try_again = input("Do you want to try it again? (y/n)").lower()
    if try_again == 'y':
        continue
    elif try_again == 'n':
        break
    else:
        print("hummm.... just exiting, I don't care")
        break


