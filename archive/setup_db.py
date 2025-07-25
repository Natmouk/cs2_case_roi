import sqlite3

def setup_database():
    conn = sqlite3.connect("database/cs2cases.db")
    c = conn.cursor()

    c.executescript("""
    CREATE TABLE IF NOT EXISTS cases (
        case_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        case_price REAL
    );

    CREATE TABLE IF NOT EXISTS case_items (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_id INTEGER,
        name TEXT,
        rarity TEXT,
        drop_chance REAL,
        FOREIGN KEY (case_id) REFERENCES cases(case_id)
    );

    CREATE TABLE IF NOT EXISTS market_prices (
        item_name TEXT PRIMARY KEY,
        price REAL,
        last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()
    conn.close()
    print("✅ Database schema created.")

if __name__ == "__main__":
    setup_database()


#cases: case_id, name, case_price, key_price
#case_items: item_id, case_id, name, rarity, drop_chance
#market_prices: item_name, price, last_updated