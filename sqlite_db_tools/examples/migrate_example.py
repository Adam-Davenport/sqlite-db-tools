from sqlite_db_tools.migrate import Migration

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


# Internal Migration

from sqlite_db_tools.migrate import Internal_Migration

db = 'path_to_db'
table1 = 'table1'
table2 = 'table2'
migration = Internal_Migration(db, table1, table2)

# If you have an autoincrementing field
migration.autoincrement = True
# Autoincrementing field name, default is id
migration.auto_field = 'auto_field name'
# Execute migration of table data
migration.copy_table()
