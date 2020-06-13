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

	name,description,deadline = cursor.fetchone()

	print("Project details for {} ({})\n due {}".format(
		description,name,deadline))

	cursor.execute(""""
			select id, priority, details,status,deadline = row
			where project = 'singh' order by deadline

		"""
		)

	print("\nNext 5 task:")
	for row in cursor.fetchmany(5):
		task_id,priority,details,status,deadline = row
		print('{:2d} [{:d}] [{:<25} [{:<8}] ({})'.format(
			task_id,priority,details,status,deadline
			))