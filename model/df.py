import pandas as pd
from pandas.core.frame import DataFrame

# ------------------------ DF ------------------------

def df_isEmpty(df:DataFrame):
    return df.empty

def df_showData(df:DataFrame):
    if (df_isEmpty(df)):
        print("\nIt is empty. Please add at least 1 student\n")
        return
    print(df)

def df_create():
    results = {
        "created" : False
    }
    try:
        fields = [
            'dni', 
            'name', 
            'grades', 
            'comments', 
        ]

        df = pd.DataFrame({}, columns=fields, index={})
        df.index.name = "index"
        
        results["df"] = df
        results["created"] = True
        return results
    except:
        print(f"Some error occurred while creating the dataframe")
        return results

def df_addNew(df:DataFrame, args:list)->DataFrame:
    df = df.append(pd.Series(args, index=df.columns), ignore_index=True)
    df.index.name = "index"
    
    return df

def df_remove(df:DataFrame, idx:int)->DataFrame:
    df = df.drop(index=idx)

    return df

def df_assignVal(val: any, field:str)->any: #private
    if field ==  "dni" or field ==  "comments":
        return val
    elif field == "name":
        return val.capitalize()
    elif field ==  "grades":
        return float(val)
                                                                      
def df_parseArgs(df:DataFrame, args:tuple)->tuple: #private
    idx, field, val = args
    # validate index
    try:
        df.loc[idx]
    except:
        print('\033[91m' + "Invalid index" + '\033[0m')# TODO: This is an interface message
        return (-1,-1,-1)
    
    # validate field
    try:
        df.loc[idx, field]
    except:
        print('\033[91m' + "Invalid field" + '\033[0m')# TODO: This is an interface message
        return (-1,-1,-1)
    
    #assign the value
    val = df_assignVal(val, field)

    return (idx, field, val)

def df_update(df:DataFrame, args:tuple)->DataFrame:
    idx, field, val = df_parseArgs(df, args)

    if (idx == -1):
        print("Not saved") # TODO: This is an interface message
        return df
    #idx, field, val = args
    df.loc[idx, field] = val
    df.index.name = "index" # to avoid deleting index in the dataframe
    return df

def df_saveCSV(df:DataFrame, filename:str):
    df.to_csv(filename)

def df_reset():
    res = df_create()
    return res["df"] 

def df_validate(df:DataFrame, val=0, key="index"):
    if key == "index":
        return val in df.index
    
    return key in df
# ---------------------- END DF ----------------------