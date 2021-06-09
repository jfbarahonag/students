import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame

OPTIONS = {
    "check":'1',
    "update":'2',
    "add":'3',
    "remove":'4',
    "clean":'5',
    "save":'6',
    "exit":'7',
}

# ------------------------ DF ------------------------
def df_create():
    results = {
        "created" : False
    }
    try:
        fields = [
            'DNI', 
            'NAME', 
            'GRADES', 
            'COMMENTS', 
        ]

        df = pd.DataFrame({}, columns=fields, index={})
        
        results["df"] = df
        results["created"] = True
        return results
    except:
        print(f"Some error occurred while creating the dataframe")
        return results

def df_isEmpty(df:DataFrame):
    return df.empty

def df_showData(df:DataFrame):
    if (df_isEmpty(df)):
        print("\nIt is empty. Please add at least 1 student\n")
        return
    print(df)

def df_addNew(df:DataFrame, args:list)->DataFrame:
    df = df.append(pd.Series(args, index=df.columns), ignore_index=True)
    return df
# ---------------------- END DF ----------------------
# ----------------------- CSV  -----------------------
def CSV_checkExistence(filename:str)->dict:
    results = {
        "found" : False
    }
    try:
        df = pd.read_csv(filename, skiprows=1, names=["DNI", "NAME", "GRADES", "COMMENTS"])
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
        
        df.to_csv(filename)
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
# --------------------- END CSV  ---------------------
# ----------------------- VIEW -----------------------
def printStartup():
    print(f'+-----------------------------+\nPress 1 to open a CSV file\n+-----------------------------+')

def printMenu():
    print("+-----------------------------+")
    print("Select an option:")
    print("1. Check all students")
    print("2. Modify a student info") # TODO
    print("3. Add student (No database)")
    print("4. Delete student (No database)")
    print("5. Clean all students info")
    print("6. Save changes")
    print("7. Exit")
    print("+-----------------------------+")
# --------------------- END VIEW ---------------------
# ---------------------- STUDENT ---------------------
def student_addNew(df:DataFrame):
    dni = input('Insert DNI: ')
    name = input('Insert name: ')
    grade = float(input('Insert final grade: ')) #TODO: Implement a list of notes
    comments = input('Insert comments about the student: ')
    student = [
        dni,
        name.lower(),
        grade,
        comments.lower(),
    ]

    return df_addNew(df, student)
# -------------------- END STUDENT -------------------

def infiniteLoop(df:DataFrame):

    while(True):
        printMenu()
        user = input()
        
        if user == OPTIONS['check']:
            df_showData(df)
            continue
        elif user == OPTIONS['update']: # TODO
            
            continue
        elif user == OPTIONS['add']:
            df = student_addNew(df)
            continue
        elif user == OPTIONS['remove']:
            
            continue
        elif user == OPTIONS['clean']:
            
            continue
        elif user == OPTIONS['save']:
            #CSV_save(df)
            
            continue
        elif user == OPTIONS['exit']:
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
    print(df)
    infiniteLoop(df)

run()