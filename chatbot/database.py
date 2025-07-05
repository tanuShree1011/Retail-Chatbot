import sqlite3

DEPARTMENTS = ["billing", "account", "orders_returns", "delivery", "technical" ,"general"]

def init_db():
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()

    for dept in DEPARTMENTS:
        c.execute(f"""
            CREATE TABLE IF NOT EXISTS {dept} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                user_name TEXT,
                query TEXT
            )
        """)
    conn.commit()
    conn.close()

def insert_to_db(department, user_id, user_name, query):
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()

    c.execute(f"""
        INSERT INTO {department} (user_id, user_name, query)
        VALUES (?, ?, ?)
    """, (user_id, user_name, query))

    conn.commit()
    conn.close()

def fetch_all_data():
    conn = sqlite3.connect("chatbot.db")
    c = conn.cursor()
    results = {}
    for dept in DEPARTMENTS:
        c.execute(f"SELECT * FROM {dept}")
        results[dept] = c.fetchall()
    conn.close()
    return results