import pandas as pd
import sqlite3

cases_df = pd.read_csv("data/cases.csv")
weapons_df = pd.read_csv("data/weapons.csv")

cases_df.columns = cases_df.columns.str.strip().str.lower().str.replace(" ", "_")
weapons_df.columns = weapons_df.columns.str.strip().str.lower().str.replace(" ", "_")

cases_df["case_name"] = cases_df["case_name"].str.strip()
weapons_df["case_name"] = weapons_df["case_name"].str.strip()

weapons_df["low_price"] = pd.to_numeric(weapons_df["low_price"], errors="coerce")
weapons_df["high_price"] = pd.to_numeric(weapons_df["high_price"], errors="coerce")

cases_df = cases_df.reset_index().rename(columns={"index": "case_id"})
cases_df["case_id"] += 1  # Start case_id from 1

weapons_df = weapons_df.merge(cases_df[["case_id", "case_name"]], on="case_name", how="left")

conn = sqlite3.connect("database.db")
cases_df.to_sql("cases", conn, if_exists="replace", index=False)
weapons_df.to_sql("weapons", conn, if_exists="replace", index=False)
conn.commit()
conn.close()

print("Saved to database.db")
