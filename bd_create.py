import sqlite3

conn = sqlite3.connect("samples.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE samples (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  time_step REAL NOT NULL,
  voltage_step REAL NOT NULL,
  zero_level INTEGER NOT NULL,
  smpl TEXT NOT NULL
);
""")
