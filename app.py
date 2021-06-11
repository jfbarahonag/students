from database import *
from file import *
from model import *
from view import *
from controller import *

def run():
    interface_printStartup()

    init = input()

    if init != "1":
        exit()

    df = CSV_open('students_db.csv')
    print(df)
    infiniteLoop(df)

run()