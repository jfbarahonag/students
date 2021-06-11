from model import *
from view import *

OPTIONS = {
    "check":'1',
    "update":'2',
    "add":'3',
    "remove":'4',
    "clean":'5',
    "save":'6',
    "exit":'7',
}
# ---------------------- CONTROLLER --------------------- TODO: Move this out of here
def infiniteLoop(df:DataFrame):

    while(True):
        interface_printMenu()
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
# ------------------- END CONTROLLER --------------------