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

src_db = 'path_to_source'
dest_db = 'path_to_dest'
table = 'table_name'
migration = Migration(src_db, dest_db, table)

# If your destination table has a different name
migration.dest_table = 'dest_table_name'

# If you have an autoincrementing field
migration.autoincrement = True

# Autoincrementing field name, default is id
migration.auto_field = 'auto_field name'

# Execute migration of table data
migration.copy_table()
```

