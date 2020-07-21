import pandas as pd
import cx_Oracle
dsn_tns = cx_Oracle.makedsn('localhost', '1521', 'xe')
conn = cx_Oracle.connect(user='C##OT', password='Orcl1234', dsn=dsn_tns)
try:
    query = '''
         SELECT * from customers
             '''
    df = pd.read_sql(con = conn, sql = query)
finally:
    conn.close()
df.head()
