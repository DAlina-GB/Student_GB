import sqlite3

def add_to_db(last_name, name, tel, description):
    base = sqlite3.connect('data_base.db')
    cur = base.cursor()
    base.execute('CREATE TABLE IF NOT EXISTS data(last_name, name, tel, description)')
    base.commit()
    cur.execute('INSERT INTO data VALUES(?, ?, ?, ?)', (last_name, name, tel, description))
    base.commit()

    base.close()

def find_in_db(to_find):
    base = sqlite3.connect('data_base.db')
    cur = base.cursor()
    r = cur.execute("SELECT rowid,* FROM data WHERE last_name=? OR name=? OR tel=? OR description=?", (to_find,to_find,to_find,to_find,)).fetchall()
    base.close()
    return r

def change_in_db(id, field_to_change, new_value):
    base = sqlite3.connect('data_base.db')
    cur = base.cursor()
    if field_to_change == '1':
        r = cur.execute('UPDATE data SET last_name == ? WHERE rowid == ?',(new_value, id,)).fetchmany()
    elif field_to_change == '2':
        r = cur.execute('UPDATE data SET name == ? WHERE rowid == ?',(new_value, id,)).fetchmany()
    elif field_to_change == '3':
        r = cur.execute('UPDATE data SET tel == ? WHERE rowid == ?',(new_value, id,)).fetchmany()
    elif field_to_change == '4':
        r = cur.execute('UPDATE data SET description == ? WHERE rowid == ?',(new_value, id,)).fetchmany()
    else:
        return 0
    base.commit()
    return r

def delete_from_db(id):
    base = sqlite3.connect('data_base.db')
    cur = base.cursor()
    cur.execute('DELETE FROM data WHERE rowid == ?', (id,))
    base.commit()

def all_from_db():
    base = sqlite3.connect('data_base.db')
    cur = base.cursor()
    r = cur.execute('SELECT * FROM data').fetchall()
    base.commit()
    return r