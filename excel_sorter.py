#!/usr/bin/env python3
import pandas as pd
import os
import re
from functions import options, choose_separator, filter_value
pd.set_option('display.max_columns', None)
os.system("clear")

# Source Info
while True:
    try:
        print("Options:\n\n1: CSV\n2: excel")
        form = int(input("\nEnter number of the file format: "))
        file1 = input("Enter location/name of file: ")
        if form == 1:
            df = pd.read_csv(file1)
            cols = pd.read_csv(file1).columns
        else:
            sheet = input("\nEnter sheet name you wish to sort or hit only Enter for default (first sheet): ")
            if not sheet:
                sheet = 0
            df = pd.read_excel(file1,sheet,na_values=['NA'])
            cols = pd.read_excel(file1).columns
    except:
        os.system("clear")
        print("Try again")
        continue
    else:
        break

# Sort Info
sorter = []
style = []
sort = True
while sort:
    os.system("clear")
    options(cols, 0)
    sorter.append(input(("\nName of the column you wish to sort by: ")))
    style.append(int(input("Type '1' for Ascending, '0' for Descending sort: ")))
    sort = input("Do you want to use another column for sorting? Enter 'y' for yes and 'n' no: ")
    if sort[0] == 'n':
        sort = False
    else:
        continue
new_df = df.sort_values(sorter,ascending=style)

# Filter Row Info
os.system("clear")
filter_row = input("Would you like to filter rows with spesific value?\n\nEnter 'y' for yes and 'n' for no: ")
if filter_row[0] == 'y':
    sort = True
    while sort:    
        os.system("clear")
        options(cols, 0)
        from_col = input("\nName of the column where value exist: ")
        new_df = filter_value(new_df, from_col)
        sort = input("Do you want to use another value for for filtering? Enter 'y' for yes and 'n' no: ")
        if sort[0] == 'n':
            sort = False
        else:
            continue

# Filter Column Info
os.system("clear")
filter_col = input("Would you like to filter columns? Enter 'y' for yes and 'n' for no: ")
if filter_col[0] == 'y':
    os.system("clear")
    options(cols, 1)
    columns = print("\nChoose range of columns to show")
    from_col = int(input("Enter number of the first column to show: "))
    to_col = int(input("Enter number of the last column to show: "))
    new_df = new_df.iloc[:, from_col:(to_col+1)]

# Destination Info
os.system("clear")
dest = input("Enter destination/filename you wish to store as: ")
if form == 1:
    new_df.to_csv(dest, index=False)
else:
    new_df.to_excel(dest, index=False)