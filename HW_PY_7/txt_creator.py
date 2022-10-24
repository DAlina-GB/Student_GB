import csv

def export_to_txt():
    with open('/Users/alina/Desktop/Seminar PY/HW_PY_7/data_base.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    with open('base_export.txt', 'w') as file:
        for i in data:
            for j in i:
                file.write('{}; \n'.format(j))