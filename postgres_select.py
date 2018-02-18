import psycopg2

conn = psycopg2.connect(database="diplom", user="postgres", password="12Qwer34", host="127.0.0.1", port="5432")
print('connection on')

cur = conn.cursor()

cur.execute("SELECT * from examples_1")

rows = cur.fetchall()
print(rows)
'''for row in rows:
   print("ID = " , row[0])
   print("NAME = " , row[1])
   print("ADDRESS = " , row[2])
   print("SALARY = " , row[3], "\n")
'''
print("Operation done successfully")
conn.close()