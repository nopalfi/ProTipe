# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:26:31 2018

@author: Pankaj
"""

import sqlite3

#creates a database with name usersdatabase.db
conn=sqlite3.connect('usersdatabase.db')

c=conn.cursor()

sql="""
    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
            id integer unique primary key autoincrement,
            name text,
            jabatan text);
    """
# users table with two columns, id and name.
# use DB Browser for sqlite to view the database.
c.executescript(sql)

conn.commit()

sql="""
    DROP TABLE IF EXISTS absensi;
    CREATE TABLE absensi (
            id integer unique primary key autoincrement,
            date text,
            temp double,
            users_id integer,
            FOREIGN KEY(users_id) REFERENCES users(id)
            );
    """
c.executescript(sql)
conn.commit()

conn.close()
