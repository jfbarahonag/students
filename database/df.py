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

# ---------------------- END DF ----------------------