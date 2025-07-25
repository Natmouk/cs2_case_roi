import sqlite3

def check_database():
    conn = sqlite3.connect("database/cs2cases.db")
    c = conn.cursor()

    print("Cases:")
    for row in c.execute("SELECT * FROM cases"):
        print(row)

    print("\nCase Items:")
    for row in c.execute("SELECT * FROM case_items"):
        print(row)

    conn.close()

if __name__ == "__main__":
    check_database()
