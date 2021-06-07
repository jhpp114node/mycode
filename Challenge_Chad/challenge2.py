#!/usr/bin/env python3
icecream = ["flavors", "salty"]
tlgclass= ["Brian","Clint","Damian","Dan","David","Jelani","Jerad","Jon","Jun","Mark","Max"]

icecream.append(int(99))
user_choice = input("Type a number between 0 and 10\n>")
print(f"<{icecream[-1]}> <{icecream[0]}>, and <{tlgclass[int(user_choice)]}> choose to be <{icecream[1]}>")

# super bonus
# randomize student
# @https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
import random
print(f"<{icecream[-1]}> <{icecream[0]}>, and <{tlgclass[random.randint(0,10)]}> choose to be <{icecream[1]}>")

# mega bonus
# If the user types in a name instead of a number, use the name instead!
name = input("Type a name instead of number\n>")
target_index = tlgclass.index(name)
print(f"<{icecream[-1]}> <{icecream[0]}>, and <{tlgclass[target_index]}> choose to be <{icecream[1]}>")
