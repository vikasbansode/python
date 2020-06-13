#!/usr/bin/python3

######################################################################
#															         #
# Python Program to row objects				          				 # 
# Created on : 13/06/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################



import sqlite3
import sys

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
	conn.row_factory = sqlite3.Row

	cursor = conn.cursor()

	cursor.execute("""
		select name,description,deadline from project
		where name = 'singh'
		""")
	name,description,deadline = cursor.fetchone()

	print("Project details for {} ({})\n due {}".format(
		description,name,deadline))

	cursor.execute(""""
		select id, priority, status, deadline, details from task
		where project = 'singh' order by deadline
		"""
		)

	print("\nNext 5 task: ")
	for row in cursor.fetchmany(5):
		print('{:2d}[{:d}] {:<25} [{:<8}] ({})'.format(
			row['id'],row['priority'],row['details'],
			row['status'],row['deadline'],))