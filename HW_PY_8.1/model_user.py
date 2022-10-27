import view
import model_file

PATH_FILE = "data.csv"


def create_user(data):
    model_file.File_recording_csv(data)
    model_file.File_recording_txt(data)

def new_create_user(data):
    model_file.File_newrecording_csv(data)
    model_file.File_newrecording_txt(data)

def show_users():
    num = int(input("1 - csv\n2 - txt\n"))
    if num == 1:
        return model_file.show_csv_users()
    elif num == 2:
        return model_file.show_txt_users()

def show_users_1():
    return model_file.show_csv_users()

def update_user(id_user, data):
    res = view.user_data_entry()
    data[id_user] = res
    return data


def delete_user(id_user, data):
    del data[id_user ]
    return data

def choiceExport(data):
    num = int(input("1 - CSV,\n 2 - XML\n"))
    if num == 1:
        model_file.File_newrecording_csv(data)
    elif num == 2:
        model_file.File_newrecording_xml(data)

def choiceImport(data):
    num = int(input("1 - CSV,\n 2 - XML\n"))
    if num == 1:
        model_file.show_csv_users(data)
    elif num == 2:
        model_file.File_reading_xml(data)
