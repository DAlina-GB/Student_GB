import user_interface as ui
import csv
import db
import exp_data


def add_contact():
    last_name = ui.get_info('Last name: ')
    name = ui.get_info('Name: ') 
    tel = ui.get_info('Tel. number: ')
    description = ui.get_info('Description: ')
    db.add_to_db(last_name, name, tel, description)
    

def find_contact():
    to_find = ui.get_info('Enter data to find: ')
    res = db.find_in_db(to_find)
    if len(res) == 0:
        ui.view_info('No matches found.')
        return 0
    elif len(res) == 1:
            ui.view_info(res)
            id = res[0][0]
    else:
            ui.view_info(res)
            id = ui.get_info('Enter ID of contact if you want to change or delete it. \nOtherwise, press \"Enter\" to quit: \n')
    
    func2 = ui.get_info('Input code of operation: \n 1 - change contact \n 2 - delete contact \n 3 - quit\n')
    if func2 == '1':
        field_to_change = ui.get_info('Select field number to change: \n 1 - Last name \n 2 - Name \n 3 - Tel. number \n 4 - Description \n')
        new_value = ui.get_info('Enter new value: ')
        changed = db.change_in_db(id, field_to_change, new_value)
        ui.view_info(changed)

    elif func2 == '2':
        db.delete_from_db(id)
        ui.view_info('Deleted')
        return 0

    elif func2 == '3':
        return 0
   

def delete_contact(num):
    f = open('/Users/alina/Desktop/Seminar PY/HW_PY_8/data_base.csv', 'r')
    reader = csv.reader(f)
    mylist = list(reader)
    f.close()
    del mylist[int(num)]
    my_new_list = open('/Users/alina/Desktop/Seminar PY/HW_PY_8/data_base.csv', 'w', newline = '')
    csv_writer = csv.writer(my_new_list)
    csv_writer.writerows(mylist)
    my_new_list.close()

def show_all():
    res = db.all_from_db()
    for i in res:
        ui.view_info(i)

def data_exp():
    op = ui.get_info('Input code of operation: \n 1 - export to .csv \n 2 - export to .txt \n 3 - (export to .json) - not completed yet :( \n 4 - quit \n')
    if op == '1':
        exp_data.t_csv()
    elif op == '2':
        exp_data.t_txt()
    # if op == '3':
    #     exp_data.t_json()
    elif op == '4':
        return 0
    else:
        ui.view_info('Input error')