#!/usr/bin/python3

######################################################################
#															         #
# Python Program to create create table          				     # 
# Created on : 13/06/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

print("""
*********************************************
* Example 1 : Create table	 	
*********************************************
""")

import os
import sqlite3
os.chdir(r'E:\Python\11.Database_program')

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'	

db_is_new = not os.path.exists(db_filename)

with sqlite3.connect(db_filename) as conn:
	if db_is_new:
		print('Creating schema')
		with open(schema_filename,'rt') as f:
			schema = f.read()
		conn.executescript(schema)

		print('Insert initial data')

		conn.executescript("""
			insert into project(name,description,deadline)
			values('singh','youtube channel','7/20/2017');

			insert into task(details,status,deadline,project)
			values ('record video','done','7/2/2017','singh');

			insert into task(details,status,deadline,project)
			values ('publish the video','waiting','7/2/2017','singh');

			insert into task(details,status,deadline,project)
			values ('get more subscribers','active','7/15/2017','singh');
			""")
	else:
		print('Database exists, assume schema does, too.')