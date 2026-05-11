import sqlite3
from pathlib import Path

# cesta k databázi
DB_PATH = Path("database/cloud_costs.db")


def create_database():

    # Vytvoří SQLite databázi a tabulku cloud_costs
   
    
    # vytvoření složky database pokud neexistuje
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    # připojení k databázi
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # vytvoření tabulky
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