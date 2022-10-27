import functions as f
import user_interface as ui

def button_click():
    while True:
        func = ui.get_info('Input code of operation: \n 1 - add contact \n 2 - find contact \n 3 - show all contacts \n 4 - export phonebook to another format\n 5 - quit \n')
        if func == '1':
            f.add_contact()
        elif func == '2':
            f.find_contact()
        elif func == '3':
            f.show_all()
        elif func == '4':
            f.data_exp()
        elif func == '5':
            break
        else: 
            ui.view_info('Input error')