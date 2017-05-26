
import sqlite3
import sys
import os


def copy_table(src_table, src_db, dest_table, dest_db):
    source = open_connection(src_db)
    dest = open_connection(dest_db)
    print('Copying data from db {} to db {}.'.format(src_db, dest_db))
    src_data = source.execute('select * from ' + src_table)
    dest_data = dest.cursor()
    for row in src_data.fetchall():
        ins = 'insert into {} values ({})'.format(
          dest_table, ','.join(str(c) for c in row)
        )
        dest.execute(ins)


def open_connection(db_location):
    db = sqlite3.connect(db_location)
    print('Opened database: ' % db_location)
