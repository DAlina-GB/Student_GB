import user_interface as ui
import csv


def add_contact():
    last_name = ui.get_info('Last name: ')
    name = ui.get_info('Name: ') 
    tel = ui.get_info('Tel. number: ')
    description = ui.get_info('Description: ')
    data = [last_name, name, tel, description]
    with open('/Users/alina/Desktop/Seminar PY/HW_PY_7/data_base.csv', 'a', encoding='utf-8', newline = '') as file:
        file_writer = csv.writer(file, delimiter = ',', lineterminator='\r')
        file_writer.writerow(data)



def find_contact():
    to_find = ui.get_info('Enter data to find: ')
    with open('/Users/alina/Desktop/Seminar PY/HW_PY_7/data_base.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter= ',')
        count = 0
        result = {}
        for row in file:
            if to_find in row:
                result[count] = row
            count += 1
        if len(result) == 0:
            ui.view_info('No matches found.')
            return 0
        elif len(result) == 1:
            for key, value in result.items():
                ui.view_info(value)
                data = key
        else:
            ui.view_dict_with_keys(result)
            data = ui.get_info('Select id of contact to change. \nPress \"Enter\" to quit: \n')
            if data == '':
                return 0
        func2 = ui.get_info('Input code of operation: \n 1 - change contact \n 2 - delete contact \n 3 - quit\n')
        if func2 == '1':
            change_contact(data)
        elif func2 == '2':
            delete_contact(data)
        elif func2 == '3':
            return 0


def change_contact(num):
    field = int(input('Select field number to change: \n 1 - Last name \n 2 - Name \n 3 - Tel. number \n 4 - Description \n')) - 1
    f = open('/Users/alina/Desktop/Seminar PY/HW_PY_7/data_base.csv', 'r')
    reader = csv.reader(f)
    mylist = list(reader)
    f.close()
    mylist[int(num)][field] = input('Enter new value: ')
    my_new_list = open('/Users/alina/Desktop/Seminar PY/HW_PY_7/data_base.csv', 'w', newline = '')
    csv_writer = csv.writer(my_new_list)
    csv_writer.writerows(mylist)
    my_new_list.close()

def delete_contact(num):
    f = open('/Users/alina/Desktop/Seminar PY/HW_PY_7/data_base.csv', 'r')
    reader = csv.reader(f)
    mylist = list(reader)
    f.close()
    del mylist[int(num)]
    my_new_list = open('/Users/alina/Desktop/Seminar PY/HW_PY_7/data_base.csv', 'w', newline = '')
    csv_writer = csv.writer(my_new_list)
    csv_writer.writerows(mylist)
    my_new_list.close()

def show_all():
    with open('/Users/alina/Desktop/Seminar PY/HW_PY_7/data_base.csv', encoding='utf-8') as file:
        for row in file:
            ui.view_info(row)

