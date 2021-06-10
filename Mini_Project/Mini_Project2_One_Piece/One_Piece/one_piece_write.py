#!/usr/bin/env python3
played_year_dic = {}
for x in range(1999, 2022, 1):
    played_year_dic[x] = []


def form_group_by_played_year(one_piece_episode_list):
    for each_episode in one_piece_episode_list:
        each_episode_split = each_episode.split(",")
        played_year_dic[int(each_episode_split[-3])].append((each_episode_split[-4]))
    print(played_year_dic)
    # loop trough key
    for keys in played_year_dic:
        one_piece_episode_filename = f"one_piece_epi{keys}.txt"
        with open(one_piece_episode_filename, "w") as one_piece_create_file:
            for each_title in played_year_dic[keys]:
                print(f"Title: {each_title}", file=one_piece_create_file)

