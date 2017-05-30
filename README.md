# sqlite-db-tools 
Tools for sqlite3 in python

# Installation
```
pip install sqlite_db_tools
```

# Features
Copy table

#Migration
This allows you to copy data in one table to a table in a different database.

## Usage
Basic usage is as simple as:
```
from sqlite-db-tools import Migration

src_db = path_to_db1
dest_db = path_to_db2
table = table_name
migration = Migration(src_db, dest_db, table)
# If your destination table has a different name
migration.dest_table = dest_table_name
# If you have an autoincrementing field and set the name of the field id is default
migration.autoincrement = True
migration.auto_field = auto_field_name
migration.copy_table()
```

