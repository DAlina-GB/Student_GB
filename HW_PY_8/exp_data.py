import csv
import sqlite3
import json
import collections

def t_csv():
    base = sqlite3.connect('data_base.db')
    cur = base.cursor()
    cur.execute("SELECT * FROM data")

    header = ['last_name', 'name', 'tel', 'description']
    with open('/Users/alina/Desktop/Seminar PY/HW_PY_8/data_base.csv', 'w', encoding='UTF8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",", lineterminator="\r")
        csv_writer.writerow(header)
        csv_writer.writerows(cur)
    base.close()

def t_txt():
    base = sqlite3.connect('data_base.db')
    cur = base.cursor()
    cur.execute("SELECT * FROM data")
    with open('data_base.txt', 'w') as file:
        for i in cur:
            for j in i:
                file.write('{}; \n'.format(j))
    base.close()