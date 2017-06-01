import unittest
from sqlite_db_tools.migrate import Migration, Internal_Migration
from sqlite_db_tools.common import open_connection
import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
src_db = os.path.join(base_dir, 'db1.sqlite3')
dest_db = os.path.join(base_dir, 'db2.sqlite3')
solo_db = os.path.join(base_dir, 'solo.sqlite3')


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


def create_single_db(auto_increment):
    # Delete db if it exists
    delete_db(solo_db)
    # Connect db
    db = sqlite3.connect(solo_db)
    # Create the table in both databases
    create_table(db)
    create_internal_table(db)
    # Populate source table
    populate_table(db)
    # Copy the tables
    migration = Internal_Migration(solo_db, 'dogs', 'dogs_copy')
    migration.copy_table()
    # Close connections
    db.close()


def copy_db(src_db, dest_db, auto_field):
    # sqlite_db_tools.copy_table('dogs', src_db, 'dogs', dest_db)
    migration = Migration(src_db, dest_db, 'dogs')
    if auto_field is True:
        migration.autoincrement = True
    migration.copy_table()


def copy_solo_db(db, auto_field):
    migration = Internal_Migration()


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


def create_internal_table(db):
    query = (
        'create table dogs_copy('
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


class Migration_Test(unittest.TestCase):

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

    def test_internal(self):
        create_single_db(False)
        db = sqlite3.connect(solo_db)
        table1 = query_table(db, 'dogs')
        table2 = query_table(db, 'dogs_copy')
        self.assertEqual(table1, table2)

    def test_internal_autoincrement(self):
        create_single_db(True)
        db = sqlite3.connect(solo_db)
        table1 = query_table(db, 'dogs')
        table2 = query_table(db, 'dogs_copy')
        self.assertEqual(table1, table2)
    
    def test_schema(self):
        create_single_db(solo_db)
        migration = Internal_Migration(solo_db, 'dogs', 'dogs')
        migration.copy_schema()

if __name__ == "__main__":
    unittest.main()
