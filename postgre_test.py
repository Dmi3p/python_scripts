import psycopg2

conn = psycopg2.connect(database="diplom", user="postgres", password="12Qwer34", host="127.0.0.1", port="5432")
print('connection on')

cur = conn.cursor()
cur.execute('''CREATE TABLE fourier
       (ID  SERIAL PRIMARY KEY,
       TIME_STEP REAL NOT NULL,
       VOLTAGE_STEP REAL NOT NULL ,
       ZERO_LEVEL REAL NOT NULL,
       FD INT NOT NULL,
       LEN INT NOT NULL,
       SMPL INT ARRAY NOT NULL,
       SPECTRUM_REAL REAL ARRAY,
       SPECTRUM_IMAG REAL ARRAY,
       SUBSTANCE INT,
       IMPURITY_TYPE INT);''')
print("Table created successfully")

conn.commit()
conn.close()