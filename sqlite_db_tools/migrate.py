import sqlite3
import sys
import os


class Migration():

    def __init__(self, source, destination, table):
        self.src_db = source
        self.dest_db = destination
        self.source_table = table
        self.dest_table = table
        self.autoincrement = False
        self.auto_field = 'id'

    def open_connection(self, db_location):
        db = sqlite3.connect(db_location)
        # Let row be dict/tuple type
        db.row_factory = sqlite3.Row
        print('Opened database: {}'.format(db_location))
        return db

    def copy_table(self):
        source = self.open_connection(self.src_db)
        dest = self.open_connection(self.dest_db)
        src_data = source.execute('select * from ' + self.source_table)
        for row in src_data.fetchall():
            cols = tuple([key for key in row.keys()])
            # Create basic insert statement that will be populated with values
            ins = 'INSERT OR REPLACE INTO {} {} VALUES ({})'.format(
                self.dest_table, cols, ','.join(['?'] * len(cols))
            )
            # values = [row[c] for c in cols]
            values = []
            for c in cols:
                if self.ignore is True and c == self.id_field:
                    values.append(None)
                else:
                    values.append(row[c])
            dest.execute(ins, values)
        dest.commit()
        source.close()
        dest.close()

    def create_table(self):
        source = self.open_connection
