import sqlite3
from pathlib import Path

DB_PATH = Path("database/cloud_costs.db")


def create_database():
    """
    Vytvoří SQLite databázi a tabulku cloud_costs.
    """

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cloud_costs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service TEXT NOT NULL,
        region TEXT NOT NULL,
        cost REAL NOT NULL,
        timestamp TEXT NOT NULL,
        status TEXT DEFAULT 'normal'
    )
    """)

    conn.commit()
    conn.close()

    print("Databáze a tabulka připravena.")


def insert_cloud_cost(data):
    
    # Uloží jeden cloud cost záznam do databáze.
    

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO cloud_costs (
        service,
        region,
        cost,
        timestamp,
        status
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        data["service"],
        data["region"],
        data["cost"],
        data["timestamp"],
        data["status"]
    ))

    conn.commit()
    conn.close()

    # print("Záznam uložen do databáze.")