#!/usr/bin/env python3
# import standard libraries
import csv

# import third party libraries
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def count_by_year(data_set):
    year_map = {}
    for x in range(1999, 2022, 1):
        year_map[x] = 0
    # print(year_map)
    # print(year_map.get(2000))
    for each_data in data_set:
        each_episode_split = each_data.split(",")
        year = int(each_episode_split[-3])
        year_map[year] += 1
    # print(year_map)
    return year_map


def generate_graph(one_piece_episode_list):
    counts_group_by_year = count_by_year(one_piece_episode_list)
    print(counts_group_by_year)
    dict_keys = []
    for keys in counts_group_by_year:
        dict_keys.append(keys)

    # Fixing random state for reproducibility
    np.random.seed(19680801)
    plt.rcdefaults()
    fig, ax = plt.subplots()

    # Example data
    people = dict_keys
    y_pos = np.arange(len(dict_keys))
    performance = 3 + 10 * np.random.rand(len(people))
    error = np.random.rand(len(people))

    ax.barh(y_pos, performance, xerr=error, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(people)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('number of episodes')
    ax.set_title('One piece played distribution by year')
    # display the graph
    # plt.show() # you can try this on a Python IDE with a GUI if you'd like
    plt.savefig("/home/student/mycode/Mini_Project/Mini_Project2_One_Piece/One_Piece/distribution.pdf")
    # save a copy to "~/static" (the "files" view)
    plt.savefig("/home/student/static/one_piece_distribution.pdf")

