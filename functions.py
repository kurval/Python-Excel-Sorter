def choose_separator():
    '''
    Allowing user to choose an operator for numeric values
    '''
    os.system("clear")
    print("Options:\n1: == Equal to\n2: >= Greater or equal to\n3: <= Less or equl to")
    sep= int(input("\nEnter number of separator: "))
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
    print(col_type)
    arg = input("Enter value you wish to filter: ").lower()
    if col_type == 'i':
        if sep == 1:
            new_df = df.loc[df[from_col] == int(arg)]
        elif sep == 2:
            new_df = df.loc[df[from_col] >= int(arg)]
        else:
            new_df = df.loc[df[from_col] <= int(arg)]
    elif col_type == 'b':
        if arg[0] == 'f':
            arg = False
        else:
            arg = True
        new_df = df.loc[df[from_col] == arg]
    elif col_type == 'O':
        new_df = df.loc[df[from_col].str.contains(arg, flags=re.I)]
    elif col_type == 'f':
        if sep == 1:
            new_df = df.loc[df[from_col] == float(arg)]
        elif sep == 2:
            new_df = df.loc[df[from_col] >= float(arg)]
        else:
            new_df = df.loc[df[from_col] <= float(arg)]
    return new_df