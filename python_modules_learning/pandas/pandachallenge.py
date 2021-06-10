#!/usr/bin/env python3

import pandas as pd

def main():
    dataframe = pd.read_json('5movies.json')
    # write it into csv
    dataframe.to_csv("5movies-translated-from-json.csv")

if __name__ == "__main__":
    main()

