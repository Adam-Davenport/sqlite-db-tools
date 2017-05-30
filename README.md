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
copier = Copier(src_db, dest_db, table)
# If your destination table has a different name
copier.dest_table = dest_table_name
```

