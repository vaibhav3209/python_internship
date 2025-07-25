import sqlite3
#********LOGGED IN MEIN SPACE HAI NOTE   LINE 10**************
make_database = sqlite3.connect("user_database.db")
make_database.executescript('''
-- drop table if exists user_info;

CREATE TABLE user_info(
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    status TEXT DEFAULT 'not specified' CHECK( status in ('logged in ','logged out',
    'not specified') ) 
    )
''')
make_database.close()