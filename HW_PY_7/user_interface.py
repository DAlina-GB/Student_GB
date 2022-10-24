import csv

def get_info(title):
    return input(title)

def view_info(data):
    print(data)

def view_info_str_by_str(data):
    for i in data.split(','):
        print(i)


def view_dict_with_keys(dict):
    for key, value in dict.items():
            print(key, ':', value)

# def view_dict_str_by_str(dict):
#     for i in dict.items():

#         for value in dict[key]:
#             print(''.join(str(n) for n in value))
