import sqlite3

connection = sqlite3.connect('my_db.db', 5)
cursor = connection.cursor()
print(connection)

cursor.execute(
    'create table first_table (name TEXT);'
)
cursor.execute(
    'insert into first_table (name) values ("Nick")'
)
cursor.execute(
    'insert into first_table (name) values ("John");'
)
cursor.execute(
    'insert into first_table (name) values ("Alex");'
)
cursor.execute(
    'insert into first_table (name) values ("Kate");'
)

cursor.execute(
    'select rowid, name from first_table;'
)
connection.commit()
# result = cursor.fetchall()
# print(result)
#
# cursor.execute(
#     'select rowid, name from first_table where rowid = 3;'
# )
# connection.commit()
# result = cursor.fetchall()
# print(result)
#
# cursor.execute(
#     'update first_table set name="Ann" where rowid=2;'
# )
# connection.commit()
#
# cursor.execute(
#     'select rowid, name from first_table;'
# )
# connection.commit()
# result = cursor.fetchall()
# print(result)

# cursor.execute(
#     'delete from first_table where rowid=4'
# )
# connection.commit()

cursor.execute(
    'select rowid, name from first_table;'            # delete tables
)
connection.commit()
result = cursor.fetchall()
print(result)

cursor.execute(
    'dro table first_table'
)
connection.commit()

# # print(connection)
# # print(cursor)

connection.close()
