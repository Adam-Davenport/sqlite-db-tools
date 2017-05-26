import sqlite_db_tools
import sqlite3
import os


def create_test_db():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    src_db = os.path.join(base_dir, 'db1.sqlite3')
    dest_db = os.path.join(base_dir, 'db2.sqlite3')
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

if __name__ == "__main__":
    create_test_db()
