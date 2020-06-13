#!/usr/bin/python3

######################################################################
#															         #
# Python Program to bulk loading			          				 # 
# Created on : 13/06/2020									         #
# Author     : Vikas Bansode								         #
#															         #
######################################################################

import csv
import sqlite3
import sys

db_filename = 'todo.db'

data_filename = sys.argv[1]

SQL = """
insert into task (details,priority,status,deadline,project)
values (:details,:priority,'active',:deadline,:project)
"""

with open(data_filename,'rt') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	with sqlite3.connect(db_filename) as conn:
		cursor = conn.cursor()
		cursor.executemany(SQL,csv_reader)



# Run script using

# python3 10.bulk_loading task.csv

