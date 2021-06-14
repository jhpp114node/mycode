#!/usr/bin/env python3
import random
"""RZFeeser | Alta3 Research
   Creating a simple dice program utilizing classes."""
# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

def main():
    """called at run time"""
    print("===== OOP Way ======")
    ## create our player objects
    player1 = Player()
    player2 = Player()

    player1.roll()
    player2.roll()
    print(f"Player 1 rolled {player1.get_dice()}")
    print(f"Player 2 rolled {player2.get_dice()}")

    # determine which player won
    if sum(player1.get_dice()) == sum(player2.get_dice()):
        print("Draw!")
    elif sum(player1.get_dice()) > sum(player2.get_dice()):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


if __name__ == "__main__":
    main()




# Not Class Way
# two palyers, 3 dice
print("========== NOT OOP WAY ============")
player1_dice = []
player2_dice = []

# roll the dice!
for i in range(3):
    player1_dice.append(random.randint(1,6))
    player2_dice.append(random.randint(1,6))

print(f"Player 1 rolled {player1_dice}")
print(f"Player 1 rolled {player2_dice}")

# sum will add everything in the iterable
if sum(player1_dice) == sum(player2_dice):
    print("Draw")
elif sum(player1_dice) > sum(player2_dice):
    print("Player 1 won")
else:
    print("Player 2 won")

