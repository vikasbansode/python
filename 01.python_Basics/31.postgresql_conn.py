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