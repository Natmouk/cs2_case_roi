import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")

cases = pd.read_sql_query("SELECT * FROM cases", conn)
weapons = pd.read_sql_query("SELECT * FROM weapons", conn)

print("\nCases:\n", cases)
print("\nWeapons:\n", weapons)

conn.close()