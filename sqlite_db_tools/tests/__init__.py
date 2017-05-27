import unittest
import sqlite_db_tools
import sqlite3
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
src_db = os.path.join(base_dir, 'db1.sqlite3')
dest_db = os.path.join(base_dir, 'db2.sqlite3')


def create_test_db():
    # Delete both dbs if they exist
    delete_db(src_db)
    delete_db(dest_db)
    # Create db files
    src = sqlite3.connect(src_db)
    dest = sqlite3.connect(dest_db)
    # src.row_factory = sqlite3.Row
    # dest.row_factory = sqlite3.Row
    # Create the table in both databases
    create_table(src)
    create_table(dest)
    # Populate source table
    populate_table(src)
    # Run tests
    test_db(src_db, dest_db)
    # Close connections
    src.close()
    dest.close()


def test_db(src_db, dest_db):
    sqlite_db_tools.copy_table('dogs', src_db, 'dogs', dest_db)


def delete_db(db):
    try:
        os.remove(db)
    except OSError:
        pass


def create_table(db):
    query = (
        'create table dogs('
        'id int primary key not null, '
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
    print('Inserting data into table')
    dogs = table_data()
    for d in range(len(dogs)):
        query = 'insert into dogs values({}, "{}", {})'.format(
            d, dogs[d][0], dogs[d][1])
        db.execute(query)
    db.commit()


def query_table(db, table):
    query = 'Select * from ' + table
    results = db.execute(query)
    return results.fetchall()


class Copy_Test(unittest.TestCase):

    def test(self):
        src = sqlite3.connect(src_db)
        dest = sqlite3.connect(dest_db)
        src_data = query_table(src, 'dogs')
        dest_data = query_table(dest, 'dogs')
        self.assertEqual(src_data, dest_data)

if __name__ == "__main__":
    create_test_db()
    unittest.main()
