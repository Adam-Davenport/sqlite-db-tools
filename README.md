# sqlite-db-tools 
Tools for sqlite3 in python

# Installation
```
pip install sqlite_db_tools
```

# Features

#Copy
This allows you to copy data in one table to a table in a different database.

## Useage
Basic usage is as simple as:
```
from sqlite-db-tools import Copier

src_db = path_to_db1
dest_db = path_to_db2
table = table_name
copier = Copier(src_db, dest_db, table)
# If your destination table has a different name
copier.dest_table = dest_table_name
```

