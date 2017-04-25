# -*- coding: utf-8 -*-
import os, sqlite3

def testSqlLite():
    dbFile = r'd:\temp\python_test.db'
    if (os.path.exists(dbFile) and os.path.isfile(dbFile)):
        os.remove(dbFile)

    conn = None
    cursor = None
    try:
        conn = sqlite3.connect(dbFile)
        cursor = conn.cursor()
        cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
        cursor.execute(r"insert into user values ('001', 'adam', 95)")
        cursor.execute(r"insert into user values ('002', 'bart', 62)")
        cursor.execute(r"insert into user values ('003', 'lisa', 78)")
        conn.commit()
    finally:
        if (cursor):
            cursor.close()
        if (conn):
            conn.close()

    readRecords()

def readRecords():
    dbFile = r'd:\temp\python_test.db'

    conn = None
    cursor = None
    try:
        conn = sqlite3.connect(dbFile)
        cursor = conn.cursor()
        cursor.execute('select * from user')
        values = cursor.fetchall()
        for v in values:
            print(v)
    finally:
        if (cursor):
            cursor.close()
        if (conn):
            conn.close()
