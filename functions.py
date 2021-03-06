import os, re

def choose_format():
    '''
    Allowing user to choose file format
    '''
    while True:
        try:
            print("Options:\n\n1: CSV\n2: excel")
            form = int(input("\nEnter number of the file format: "))
        except:
            os.system("clear")
            print("Please try again!\n".upper())
            continue
        else:
            if form != 1 and form != 2:
                os.system("clear")
                print("Incorrect number!\n".upper())
                continue
            else:
                break
    return form

def choose_separator():
    '''
    Allowing user to choose an operator for numeric values
    '''
    os.system("clear")
    print("filter section (1)\n".upper())
    print("Options:\n\n1: == Equal to\n2: >= Greater or equal to\n3: <= Less or equal to")
    while True:
        try:
            sep = int(input("\nEnter number of separator: "))
        except TypeError:
            print("Please try again!")
            continue
        else:
            break
    return sep

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

def filter_value(df, from_col):
    '''
    Filtering rows based on user's input/value.
    '''
    col_type = df[from_col].dtype.kind
    if col_type == 'i' or col_type == 'f':
        sep = choose_separator()
    arg = input("Enter value you wish to filter: ").lower()
    if col_type == 'i' or col_type == 'f':
        if sep == 1:
            if col_type == 'i':
                new_df = df.loc[df[from_col] == int(arg)]
            else:
                new_df = df.loc[df[from_col] == float(arg)]      
        elif sep == 2:
            if col_type == 'i':
                new_df = df.loc[df[from_col] >= int(arg)]
            else:
                new_df = df.loc[df[from_col] >= float(arg)]
        else:
            if col_type == 'i':
                new_df = df.loc[df[from_col] <= int(arg)]
            else:
                new_df = df.loc[df[from_col] <= float(arg)]
    elif col_type == 'b':
        if arg[0] == 'f':
            arg = False
        else:
            arg = True
        new_df = df.loc[df[from_col] == arg]
    elif col_type == 'O':
        new_df = df.loc[df[from_col].str.contains(arg, flags=re.I)]
    return new_df