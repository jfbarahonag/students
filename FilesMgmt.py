import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

# ----------------------- CSV  -----------------------
def CSV_checkExistence(filename:str)->dict:
    results = {
        "found" : False
    }
    try:
        df = pd.read_csv(filename, skiprows=1, names=['dni', 'name', 'grades', 'comments'])
        results["dataFrame"] = df
        results["found"] = True
        return results
    except:
        return results

def CSV_createFile(filename:str)->dict:
    results = {
        "created" : False
    }
    try:
        students_data = {
            'dni': [],
            'name': [],
            'grades': [],
            'comments': [],
        }

        df = pd.DataFrame(students_data)
        df.to_csv(filename)
        results["dataFrame"] = df
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
    
    return file['dataFrame']
# --------------------- END CSV  ---------------------
# ------------------------ DF ------------------------
def df_isEmpty(df:DataFrame):
    return df.empty

def df_showData(df:DataFrame):
    if (df_isEmpty(df)):
        print("\nIt is empty. Please add at least 1 student\n")
        return
    print(df)
# ---------------------- END DF ----------------------
# ----------------------- VIEW -----------------------
def printStartup():
    print(f'+-----------------------------+\nPress 1 to open a CSV file\n+-----------------------------+')

def printMenu():
    print("+-----------------------------+")
    print("Select an option:")
    print("1. Check all students")
    print("2. Modify a student info") # TODO
    print("3. Add student")
    print("4. Delete student")
    print("5. Clean all students info")
    print("6. Exit")
    print("+-----------------------------+")
# --------------------- END VIEW ---------------------

def infiniteLoop(df:DataFrame):

    while(True):
        printMenu()
        user = input()
        
        if user == '1':
            df_showData(df)
            continue
        elif user == '2': # TODO
            
            continue
        elif user == '3':
            
            continue
        elif user == '4':
            
            continue
        elif user == '5':
            
            continue
        elif user == '6':
            print("\nBye")
            break
        else:
            print("Bad input")

def run():
    printStartup()

    init = input()

    if init != "1":
        exit()

    df = CSV_open('students_db.csv')

    infiniteLoop(df)

run()