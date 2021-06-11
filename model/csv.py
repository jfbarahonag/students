import os

import pandas as pd
import pandas.core.frame as DataFrame

from model.df import df_create, df_saveCSV

# ----------------------- CSV  -----------------------
def CSV_checkExistence(filename:str)->dict:
    results = {
        "found" : False
    }
    try:
        df = pd.read_csv(filename, skiprows=1, names=["dni", "name", "grades", "comments"])
        results["df"] = df
        results["found"] = True
        return results
    except:
        return results

def CSV_createFile(filename:str)->dict:
    results = {
        "created" : False
    }
    try:
        res = df_create()
        df = res["df"]
        
        df_saveCSV(df, filename)
        results["df"] = df
        results["created"] = True
        return results
    except:
        print(f"Some error occurred while creating the file ${filename}")
        return results

def CSV_open(filename:str)->DataFrame:
    file = CSV_checkExistence(filename)

    if file["found"] == True:
        print("DB opened successfully")
    else:
        file = CSV_createFile(filename)
        print("DB created")
    
    return file['df']

def CSV_save(df:DataFrame):
    filename = 'students_db.csv'

    if os.path.isfile(filename): #exists
        os.remove(filename)

    df_saveCSV(df, filename)

# --------------------- END CSV  ---------------------