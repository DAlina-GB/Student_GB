import functions as f
import user_interface as ui
import txt_creator as tc

def button_click():
    func = ui.get_info('Input code of operation: \n 1 - add contact \n 2 - find contact \n 3 - show all contacts \n 4 - export phone book to .txt file \n 5 - quit \n')
    if func == '1':
        f.add_contact()
    elif func == '2':
        f.find_contact()
    elif func == '3':
        f.show_all()
    elif func == '4':
        tc.export_to_txt()
    elif func == '5':
        return 0
    else: 
        print('Input error')