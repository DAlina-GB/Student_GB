import csv



PATH_FILE = "/Users/alina/Desktop/Seminar PY/HW_PY_8.1/data.csv"
NAME_FILE = "data.txt"


def File_recording_csv(data):
    lst = data
    with open(PATH_FILE, 'a', encoding="UTF8") as file:
        file_writer = csv.writer(file, delimiter=";", lineterminator="\r")
        file_writer.writerow(lst)
        return


def File_newrecording_csv(data):
    lst = data
    with open(PATH_FILE, 'w', encoding="UTF8") as file:
        file_writer = csv.writer(file, delimiter=";", lineterminator="\r")
        file_writer.writerows(lst)
        return


def show_csv_users():
    lst = []
    with open(PATH_FILE, 'r', encoding="UTF8") as file:
        file_reader = csv.reader(file, delimiter=";", lineterminator="\r")
        for item in file_reader:
            lst.append(item)
    return lst


def show_txt_users():
    lst = []
    with open(NAME_FILE, 'r', encoding="UTF8") as file:
        lines = file.readlines()
        for line in lines:
           lst.append(line.strip())
    return lst


def File_newrecording_csv(data):
    lst = data
    with open(PATH_FILE, 'w', encoding="UTF8") as file:
        file_writer = csv.writer(file, delimiter=";", lineterminator="\r")
        file_writer.writerows(lst)
        return


def File_recording_txt(data):
    lst = data
    stroka = ''
    with open(NAME_FILE, 'a', encoding="UTF8") as file:
        for item in lst:
            stroka += item + ";"
        stroka = stroka[:-1]
        file.write(stroka + "\n")
    return


def File_newrecording_txt(data):
    lst = data
    stroka = ''
    with open(NAME_FILE, 'w', encoding="UTF8") as file:
        for item in lst:
            stroka += str(item) + ";"
        stroka = stroka[:-1]
        file.writelines(stroka + "\n")
    return