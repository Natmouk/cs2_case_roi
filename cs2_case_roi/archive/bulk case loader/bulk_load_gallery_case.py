import sqlite3

DB_PATH = r"C:\Users\user\Desktop\Projects\cs2 case roi\database\cs2cases.db"

def insert_case(conn, case_name, case_price=None):
    conn.execute(
        "INSERT OR IGNORE INTO cases (name, case_price) VALUES (?, ?)",
        (case_name, case_price)
    )
    conn.commit()

def insert_item(conn, item_name, case_name, rarity):
    rarity_odds = {
        "Mil-Spec": 0.7992,
        "Restricted": 0.1598,
        "Classified": 0.032,
        "Covert": 0.0064,
        # Rare Special not included here
    }
    drop_chance = rarity_odds.get(rarity, None)

    cur = conn.execute("SELECT case_id FROM cases WHERE name = ?", (case_name,))
    row = cur.fetchone()
    case_id = row[0] if row else None

    if case_id is None:
        insert_case(conn, case_name)
        case_id = conn.execute("SELECT case_id FROM cases WHERE name = ?", (case_name,)).fetchone()[0]

    conn.execute(
        """
        INSERT OR IGNORE INTO case_items (case_id, name, rarity, drop_chance)
        VALUES (?, ?, ?, ?)
        """,
        (case_id, item_name, rarity, drop_chance)
    )
    conn.commit()

def bulk_add_case_and_items(conn, case_name, items, case_price=None):
    insert_case(conn, case_name, case_price)
    for item_name, rarity in items:
        insert_item(conn, item_name, case_name, rarity)
    print(f"Case '{case_name}' loaded with {len(items)} items.")

if __name__ == "__main__":
    conn = sqlite3.connect(DB_PATH)

    gallery_items = [
        ("M4A1-S | Vaporwave", "Covert"),
        ("Glock-18 | Gold Toof", "Covert"),
        ("UMP-45 | Neo-Noir", "Classified"),
        ("P250 | Epicenter", "Classified"),
        ("AK-47 | The Outsiders", "Classified"),
        ("SSG 08 | Rapid Transit", "Classified"),
        ("P90 | Randy Rush", "Restricted"),
        ("MAC-10 | Saibā Oni", "Restricted"),
        ("Dual Berettas | Hydro Strike", "Restricted"),
        ("M4A4 | Turbine", "Restricted"),
        ("SCAR-20 | Trail Blazer", "Restricted"),
        ("R8 Revolver | Tango", "Restricted"),
        ("M249 | Hypnosis", "Restricted"),
        ("AUG | Luxe Trim", "Restricted"),
        ("MP5-SD | Statics", "Restricted"),
        ("Desert Eagle | Calligraffiti", "Restricted"),
        ("USP-S | 027", "Restricted"),
    ]

    bulk_add_case_and_items(conn, "Gallery Case", gallery_items)

    conn.close()
