# dataset reference
# 4 letters : @https://www.thefreedictionary.com/4-letter-words.htm
# 5 letters : @https://www.thefreedictionary.com/5-letter-words.htm
# 6 letters : @https://www.thefreedictionary.com/6-letter-words.htm

import random
import json # read all data and store it in the map
json_file = open('hangman_data_set.json')
vocabulary_data = json.load(json_file)

print("="*30)
print("="*8+"Dummy Hangman"+"="*9)
print("="*30)

NUM_CHECK_LIST = ('1', '2', '3')
WORD_CHECK_LIST = ('easy', 'medium', 'hell')
while True:
    try:
        user_difficulty_selelction \
            = input("Select the difficulty!\n1.Easy\n2.Medium\n3.Hell\n> ").lower()
        # basic validation to throw error
        # it does not check both combination
        if (user_difficulty_selelction not in NUM_CHECK_LIST
                and user_difficulty_selelction not in WORD_CHECK_LIST):
            assert False # throw Assertion Error

        # after validation
        if user_difficulty_selelction == 'easy' or user_difficulty_selelction == '1':
            user_difficulty_selelction = [0, '4']
            break;
        elif user_difficulty_selelction == 'medium' or user_difficulty_selelction == '2':
            user_difficulty_selelction = [1, '5']
            break;
        elif user_difficulty_selelction == 'hell' or user_difficulty_selelction == '3':
            user_difficulty_selelction = [2, '6']
            break;
    except AssertionError:
        print("Not a right selection")
        print("type 1 or easy for Easy")
        print("type 2 or medium for Medium")
        print("type 1 or hell for Hell")

# grab the lists of the data based on the user selected difficulty
print(vocabulary_data.get("hangman_data")[user_difficulty_selelction[0]].get(user_difficulty_selelction[1]))
hangman_data_choose_difficulty = \
    vocabulary_data.get("hangman_data")[user_difficulty_selelction[0]].get(user_difficulty_selelction[1])
# get random index to
random_index = random.randint(0, len(hangman_data_choose_difficulty) - 1)
target_hangman_data = hangman_data_choose_difficulty[random_index]
print(target_hangman_data)


# main game board
length_of_user_choice = int(user_difficulty_selelction[1])
# create panel to display based on the len
vocab_panel = []
for x in range(length_of_user_choice):
    vocab_panel.append(" ___ ")

# I need a set to keep track used word
english_list = set({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'})
life = 6
while life > 0:
    # need to find a way to only accepting the str
    print("Available english word list")
    # convert set into list then sort for visualization purpose
    print(sorted(english_list))
    print("\n")
    try:
        # print the panel
        for y in range(len(vocab_panel)):
            print(vocab_panel[y], end=" ")
        user_guess = input(f"Remained life: {life}\nPlease Make a guess\n> ")[0].lower()
        # adding validation to make sure it is only english char
        # isalpha @https://stackoverflow.com/questions/30994738/how-to-make-input-only-accept-a-z-etc
        if not user_guess.isalpha():
            assert False
        else:
            print(f"Entered word: {user_guess}")
            english_list.remove(user_guess)
            # find all indexes that is matching
            matching_index = []
            for x in range(len(target_hangman_data)):
                if user_guess == target_hangman_data[x]:
                    matching_index.append(x)
            # update the board
            print(f"matching Index {matching_index}")
            if len(matching_index) > 0:
                for z in range(len(matching_index)):
                    vocab_panel[matching_index[z]] = "_"+user_guess+"_"
            else:
                print("Nothing Match decrease life")
                life -= 1
                pass
            # check if all the words are revealed
            if " ___ " in vocab_panel:
                # if this does not exist it throws ValueError
                print("vocab panel remained....")
            else:
                print(f"Yes! the word is {target_hangman_data}")
                print("="*12+"You Won"+"="*12+"\n")
                break
    except AssertionError:
        print("Invalid input.\nIt should be only English letter")
        life -= 1
    except KeyError:
        print("The English letter is already used")
        life -= 1

if life == 0:
    print(f"The word was {target_hangman_data}")
    print(f"Maybe next time... :D")
print("="*38)
print("="*8+"Thank you for playing"+"="*9)
print("="*8+"Exiting... Good bye"+"="*9)
print("="*38)
