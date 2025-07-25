import sqlite3
conn = sqlite3.connect("database/cs2cases.db")
c = conn.cursor()

case_name = "Revolution Case"
case_price = 0.85  

c.execute("""
    INSERT OR IGNORE INTO cases (name, case_price)
    VALUES (?, ?)
""", (case_name, case_price))


conn.commit()

c.execute("SELECT case_id FROM cases WHERE name = ?", (case_name,))
case_id = c.fetchone()[0]

items = [
    ("AWP | Duality", "Classified", 0.0128),
    ("UMP-45 | Wild Child", "Classified", 0.0128),
    ("M4A4 | Temukau", "Covert", 0.0064),
    ("P2000 | Wicked Sick", "Restricted", 0.064),
    ("Tec-9 | Rebel", "Mil-Spec", 0.7992)
]

for name, rarity, drop_chance in items:
    c.execute("""
        INSERT OR IGNORE INTO case_items (case_id, name, rarity, drop_chance)
        VALUES (?, ?, ?, ?)
    """, (case_id, name, rarity, drop_chance))

conn.commit()
conn.close()

