import sqlite3

#Creates database if it does not exist
with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    #Execute SQL code
    #c.execute('DROP TABLE posts') # - This deletes the current table called posts
    c.execute('CREATE TABLE users(id INTEGER, cardid TEXT, name TEXT, credit INTEGER, bottles INTEGER)')
    c.execute('INSERT INTO users VALUES(1,"12345678","Thomas Hunn",5.43,2)')
    c.execute('INSERT INTO users VALUES(2,"87654321","Damien Sinclair",2.43,1)')
