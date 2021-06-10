#!/usr/bin/env python3
from one_piece_read import displayAllCharacters, searchByName, searchByDevilFruit
from one_piece_write import form_group_by_played_year
from one_piece_graph import generate_graph

onepiece_character_list = []
with open ("./Onepiece_data/onepice_fruits.txt") as onepiece_devil_fruit_file:
    for each_character in onepiece_devil_fruit_file:
        onepiece_character_list.append(each_character.strip('\n'))


one_piece_episode_list = []
with open('Onepiece_data/ONE_PIECE_Episode.txt', 'r') as episode_file:
    for each_line in episode_file:
        one_piece_episode_list.append(each_line)

one_piece_episode_list = one_piece_episode_list[1:]


def main():
    user_choice_tuple = ('-1','1','2','3','4')
    while True:
        try:
            print("="* 30)
            print("="* 10 + "Welcome to One Piece Library" + "="*10)
            user_choice = input("1. Display All Characters in One Piece"
                                "\n2. Search One Piece Character by name\n"
                                "3. Search by Devil's Fruit name\n"
                                "4. Save Episode title based on the year\n"
                                "5. View episode played distribution graph by year\n"
                                "-1 to exit\n> ")
            if not user_choice.isnumeric() and user_choice not in user_choice_tuple:
                assert False
            # if user input is valid
            if user_choice == '1':
                displayAllCharacters(onepiece_character_list)
            elif user_choice == '2':
                searchByName(onepiece_character_list)
            elif user_choice == '3':
                searchByDevilFruit(onepiece_character_list)
            elif user_choice == '4':
                form_group_by_played_year(one_piece_episode_list)
            elif user_choice == '-1':
                break
            elif user_choice == '5':
                generate_graph(one_piece_episode_list)
        except AssertionError:
            print("Invalid input...")


if __name__ == "__main__":
    main()
