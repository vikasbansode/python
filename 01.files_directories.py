import os

# Creating path
os.chdir('D:\\Data_science')

# Getting curret path
os.getcwd()

# Listing files
os.listdir('D:\\Data_science')
os.ls()

# Creating variables
a = 10

# Deleting objects
del a

# Creating directory
os.mkdir('python_folder')

# Creating file

open('python_file.docx','a').close()

# OR
# from pathlib import Path
# path('python2_file.txt').touch()

# copying a file or folder

import shutil, os

shutil.copy('python_file.txt','D:\\Data_science\\python_folder')
shutil.copy('R_folder','D:\\Data_science\\python_folder')

# giving permissions to folder

os.chmod('R_folder',0o444)

# List files in pattern
import glob
glob.glob("*.csv")

# downloading file

import urllib.request

url = "https://www.python.org/static/img/python-logo@2x.png"
urllib.request.urlretrieve(url,'D:\\Data_science\\cat.jpg')

import wget
url = "https://www.python.org/static/img/python-logo@2x.png"
wget.download(url,'D:\\Data_science\\pythonlogo.png')

# Rename directories

os.rename('R_folder','R1_folder')

# Rename files
os.rename('r_file.txt','r1_file.txt')


# Conneting to postgres and doing DML

import psycopg2

conn = psycopg2.connect(database="testdb",user="postgres",password="vikas@123",host="localhost",port="5432")
print("Opened database successfully")


cur = conn.cursor()
cur.execute('''
            CREATE TABLE COMPANY(
                ID INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                AGE INT NOT NULL,
                ADDRESS CHAR(50),
                SALARY REAL
                );
            ''')

print("Table created successfully")

conn.commit()
conn.close()


###

import psycopg2

conn = psycopg2.connect(database="testdb",user="postgres",password="vikas@123",host="localhost",port="5432")
print("Opened database successfully")

cur = conn.cursor()

cur.execute("DELETE from COMPANY where ID=2;")
conn.commit()

print("Total number of rows deleted :", cur.rowcount)

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3]), "\n"

print()
print("Operation done successfully");
conn.close()



##

import psycopg2

conn = psycopg2.connect(database="testdb",user="postgres",password="vikas@123",host="localhost",port="5432")
print("Opened database successfully")

cur = conn.cursor()

cur.execute("INSERT  INTO company (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1,'Paul',32,'California',20000.00)");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
print("Records created successfully")
conn.close()  


##

import psycopg2

conn = psycopg2.connect(database="testdb",user="postgres",password="vikas@123",host="localhost",port="5432")
print("Opened database successfully")

cur = conn.cursor()

cur.execute("Select id,name,address,salary from company")

rows = cur.fetchall()

for row in rows:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")

print("operation done successfully");
conn.close()


###

import psycopg2

conn = psycopg2.connect(database="testdb",user="postgres",password="vikas@123",host="localhost",port="5432")
print("Opened database successfully")

cur = conn.cursor()

cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print("ID = ", row[0])
   print("NAME = ", row[1])
   print("ADDRESS = ", row[2])
   print("SALARY = ", row[3]), "\n"

print()
print("Operation done successfully");
conn.close()
