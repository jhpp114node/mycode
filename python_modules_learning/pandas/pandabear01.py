#!/usr/bin/env python3

import pandas as pd

def main():
    # define the xls file
    excel_file = 'movies.xls'
    
    # create data frame (pandas is coverting the file into dataframe (df)
    movies = pd.read_excel(excel_file)

    # display first 5 lines of data by using head()
    print(movies.head())
    # choose the first column "Title" as
    # index (index =0)
    movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)

    # DF (data frame) has 5 rows and 24 columns
    print(movies_sheet1.head())
    
    # export 5 movies from the top of the dataframe to json
    movies_sheet1.head(5).to_json("5movies.json")

    # export 5 movies from the top of the dataframe to csv
    movies_sheet1.head(5).to_csv("5movies.csv")

if __name__ == "__main__":
    main()
