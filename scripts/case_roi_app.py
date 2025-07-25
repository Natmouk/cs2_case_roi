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


sl.header("Case ROI Calculator")

key_cost = 2.5

rarity_probs = {
    "Covert": 0.0064,
    "Classified": 0.0320,
    "Restricted": 0.1598,
    "Mil-Spec": 0.7992
}


weapons["avg_price"] = (weapons["low_price"] + weapons["high_price"]) / 2

roi_data = []

for case_name in cases["case_name"].unique():
    case_price = cases.loc[cases["case_name"] == case_name, "price"].values[0]
    total_price = case_price + key_cost
    case_weapons = weapons[weapons["case_name"] == case_name]
    
    expected_value = 0
    
    for rarity, prob in rarity_probs.items():
        rarity_items = case_weapons[case_weapons["rarity"] == rarity]
        if not rarity_items.empty:
            avg_price = rarity_items["avg_price"].mean()
            expected_value += prob * avg_price

    roi = expected_value / total_price if total_price else 0

    roi_data.append({
        "Case": case_name,
        "Expected Value": round(expected_value, 2),
        "Case Price": round(case_price, 2),
        "ROI": round(roi, 2)
    })

roi_df = pd.DataFrame(roi_data).sort_values(by="ROI", ascending=False)

sl.subheader("ROI by Case")
sl.dataframe(roi_df)

sl.bar_chart(roi_df.set_index("Case")["ROI"])


conn.close()