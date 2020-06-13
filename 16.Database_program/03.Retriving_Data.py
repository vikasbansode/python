#!/usr/bin/python3

######################################################################
#															         #
# Python Program to retrive Data		          				     # 
# Created on : 13/06/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################


import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
	cursor = conn.cursor()

	cursor.execute("""

			select id,priority,details,status,deadline from task
			where project = 'singh'
		"""
		)
	for row in cursor.fetchall():
		task_id,priority,details,status,deadline = row
		print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
			task_id,priority,details,status,deadline))