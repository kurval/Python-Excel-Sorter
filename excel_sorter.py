#!/usr/bin/env python3
import pandas as pd
import os
import re
pd.set_option('display.max_columns', None)

def options(cols, opt):
    '''
    Shows column names that user can choose to sort/filter
    '''
    x = 0
    print("\nOptions:\n")
    for col in cols:
        if opt:
            print(str(x) + ": " + col)
        else:
            print(col)
        x += 1

def filter_value(df, from_col, arg):
    '''
    Filtering rows based on user's input/value.
    '''
    col_type = df[from_col].dtype.kind
    if col_type == 'i':
        new_df = df.loc[df[from_col] == int(arg)]
    elif col_type == 'b':
        if arg[0] == 'f':
            arg = False
        else:
            arg = True
        new_df = df.loc[df[from_col] == arg]
    elif col_type == 'O':
        new_df = df.loc[df[from_col].str.contains(arg, flags=re.I)]
    elif col_type == 'f':
        new_df = df.loc[df[from_col] == float(arg)]
    return new_df

# Source Info
form = int(input("Do you want to open csv or excel file? Enter '1' for CSV or '2' for excel: "))
file1 = input("Enter location/name of file: ")
if form == 1:
    df = pd.read_csv(file1)
    cols = pd.read_csv(file1).columns
else:
    sheet = input("\nEnter sheet name you wish to sort or hit only Enter for default (first sheet): ")
    if not sheet:
        sheet = 0
    df = pd.read_excel(file1,sheet)
    cols = pd.read_excel(file1).columns

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
new_df = df.sort_values(sorter, ascending=style)

# Filter Row Info
os.system("clear")
filter_row = input("Would you like to filter rows with spesific value? Enter 'y' for yes and 'n' for no: ")
if filter_row[0] == 'y':
    sort = True
    while sort:    
        os.system("clear")
        options(cols, 0)
        from_col = input("\nName of the column where value exist: ")
        arg = input("Enter value you wish to filter: ").lower()
        new_df = filter_value(new_df, from_col, arg)
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