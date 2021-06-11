from model.df import *
from pandas.core.frame import DataFrame

# ---------------------- STUDENT ---------------------
def student_update(df:DataFrame):
    df_showData(df)

    idx = int(input('Please insert the index of the student: '))
    if not df_validate(df, idx):
        print('Bad index') # TODO: This is an interface message
        return df
    field = input('Please insert the field you want change: ')
    if not df_validate(df, key=field):
        print('Bad field') # TODO: This is an interface message
        return df

    val = input(f'Please insert the new value to the {field}: ')

    return df_update(df, (idx, field, val))

def student_addNew(df:DataFrame):
    dni = input('Insert DNI: ')
    name = input('Insert name: ')
    grade = float(input('Insert final grade: ')) #TODO: Implement a list of notes
    comments = input('Insert comments about the student: ')
    student = [
        dni,
        name.capitalize(),
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