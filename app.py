from database import *
from file import *

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
def student_update(df:DataFrame):
    df_showData(df)

    idx = int(input('Please insert the index of the student: '))
    field = input('Please insert the field you want change: ')
    val = input(f'Please insert the new value to the {field}: ')

    return df_update(df, (idx, field, val))

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

def student_remove(df:DataFrame):
    df_showData(df)

    idx = int(input('Please insert the index of the student: '))

    return df_remove(df, idx)

def student_cleanAll():
    return df_reset()
# -------------------- END STUDENT -------------------

def infiniteLoop(df:DataFrame):

    while(True):
        printMenu()
        user = input()
        
        if user == OPTIONS['check']:
            df_showData(df)
            continue
        elif user == OPTIONS['update']: # TODO
            df = student_update(df)
            continue
        elif user == OPTIONS['add']:
            df = student_addNew(df)
            continue
        elif user == OPTIONS['remove']:
            df = student_remove(df)
            continue
        elif user == OPTIONS['clean']:
            df = student_cleanAll()
            continue
        elif user == OPTIONS['save']:
            CSV_save(df)
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