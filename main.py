import sqlite3
import os
import csv


def create_new_db(db_name):
    conn = sqlite3.connect(db_name + '.db')
    print "Opened database successfully";
    return conn


def get_current_date(conn):
    curr_stmp = conn.execute("SELECT CURRENT_TIMESTAMP;")
    return curr_stmp


def create_new_tble(conn):
    conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
    print "Table created successfully";
    return


def insert_rows(conn, row):
    uid = row[0]
    name = row[1]
    age = row[2]
    address = row[3]
    salary = row[4]
    conn.execute("INSERT OR IGNORE INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (?, ?, ?, ?, ?)", (uid, name, age, address, salary ));
    conn.commit()
    return


def update_rows(conn):
    conn.execute("UPDATE COMPANY SET SALARY = 25000.00 WHERE ID = 1");
    conn.commit()
    print "Records updated successfully";
    cursor = get_data(conn)
    display_data(cursor)
    return


def delete_rows(conn, tbl_name, col_name, col_val):
    conn.execute("DELETE FROM " + tbl_name + " WHERE " + col_name + "=" + col_val);
    conn.commit()
    print "Records deleted successfully";
    cursor = get_data(conn)
    display_data(cursor)
    return


def get_data(conn):
    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    return cursor


def display_data(cursor):
    for row in cursor:
        print "ID = ", row[0]
        print "NAME = ", row[1]
        print "ADDRESS = ", row[2]
        print "SALARY = ", row[3], "\n"
    return


db_name = 'test' # raw_input()
conn = create_new_db(db_name)
create_new_tble(conn)

with open('data.csv', 'rb') as f:
    reader = csv.reader(f)
    for ix, row in enumerate(reader):
        if ix > 0:
            insert_rows(conn, row)
    print "All Records created successfully";
cursor = get_data(conn)


choice_display = { '0': ['Exit'],
                   '1': ['Display'],
                   '2': ['Update'],
                   '3': ['Delete'],
                 }
choice = 1

while(choice):
    print "WELCOME :: "
    for ch in choice_display:
        print ch, choice_display[ch][0]
    print " 1. Display 2. Update, 3. Delete"
    print "Enter your choice"
    choice = input()

    if choice == 1:
        display_data(cursor)
    elif choice == 2:
        update_rows(conn)
    elif choice == 3:

        print "Enter the table name"
        tbl_name = raw_input()
        print "Enter the column"
        col_name = raw_input()
        print "Enter the value for the column"
        col_val = raw_input()

        delete_rows(conn, tbl_name, col_name, col_val)

conn.close()