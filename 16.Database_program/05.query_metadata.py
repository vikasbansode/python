#!/usr/bin/python3

######################################################################
#															         #
# Python Program to retrive metadata		          				 # 
# Created on : 13/06/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################


import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
	cursor = conn.cursor()

	cursor.execute("""
		select * from task where project = 'singh'
		"""
		)

	print("Task table has these columns:")
	for colinfo in cursor.description:
		print(colinfo)