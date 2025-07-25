import streamlit as sl
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def get_cases():
    query = "SELECT * FROM cases"
    return pd.read_sql_query(query, conn)

def get_weapons():
    query = "SELECT * FROM weapons"
    return pd.read_sql_query(query, conn)





sl.title("CS2 Case & Weapon ROI Dashboard")

cases = get_cases()
weapons = get_weapons()

if sl.checkbox("Show raw cases data"):
    sl.dataframe(cases)

if sl.checkbox("Show raw weapons data"):
    sl.dataframe(weapons)


conn.close()