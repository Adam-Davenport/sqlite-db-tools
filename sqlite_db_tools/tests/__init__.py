import unittest
from sqlite_db_tools import Copier
import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
src_db = os.path.join(base_dir, 'db1.sqlite3')
dest_db = os.path.join(base_dir, 'db2.sqlite3')


def create_test_db(ignore_id):
    # Delete both dbs if they exist
    delete_db(src_db)
    delete_db(dest_db)
    # Create db files
    src = sqlite3.connect(src_db)
    dest = sqlite3.connect(dest_db)
    # Create the table in both databases
    create_table(src)
    create_table(dest)
    # Populate source table
    populate_table(src)
    # Run tests
    copy_db(src_db, dest_db, ignore_id)
    # Close connections
    src.close()
    dest.close()


def copy_db(src_db, dest_db, ignore_id):
    # sqlite_db_tools.copy_table('dogs', src_db, 'dogs', dest_db)
    copier = Copier(src_db, dest_db, 'dogs')
    if ignore_id is False:
        copier.ignore = False
    copier.copy_table()


def delete_db(db):
    try:
        os.remove(db)
    except OSError:
        pass


def create_table(db):
    query = (
        'create table dogs('
        'id integer primary key autoincrement not null, '
        'name text not null, '
        'age int not null)')
    db.execute(query)


def table_data():
    dogs = [
        ['Lucky', 9],
        ['Barnie', 7],
        ['Zeus', 3],
        ['Bob', 2],
        ['Odin', 11]
    ]
    return dogs


def populate_table(db):
    dogs = table_data()
    for d in range(len(dogs)):
        query = 'insert into dogs values({}, "{}", {})'.format(
            'Null', dogs[d][0], dogs[d][1])
        db.execute(query)
    db.commit()


def query_table(db, table):
    query = 'Select * from ' + table
    results = db.execute(query)
    return results.fetchall()


class Copy_Test(unittest.TestCase):

    def test(self):
        create_test_db(False)
        src = sqlite3.connect(src_db)
        dest = sqlite3.connect(dest_db)
        src_data = query_table(src, 'dogs')
        dest_data = query_table(dest, 'dogs')
        self.assertEqual(src_data, dest_data)

    def test_autoincrement(self):
        create_test_db(True)
        src = sqlite3.connect(src_db)
        dest = sqlite3.connect(dest_db)
        src_data = query_table(src, 'dogs')
        dest_data = query_table(dest, 'dogs')
        self.assertEqual(src_data, dest_data)


if __name__ == "__main__":
    unittest.main()
