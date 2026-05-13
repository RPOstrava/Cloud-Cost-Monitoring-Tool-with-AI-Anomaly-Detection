import sqlite3
import pandas as pd

DB_PATH = "database/cloud_costs.db"


def load_data():
    
    # Načte data z SQLite do pandas DataFrame.
    

    conn = sqlite3.connect(DB_PATH)

    query = "SELECT * FROM cloud_costs"

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def basic_analysis():
    
    # Provede základní analýzu dat.
    

    df = load_data()

    print("\n--- BASIC ANALYSIS ---")

    print(f"Počet záznamů: {len(df)}")

    print("\nCelkové náklady podle služby:")
    print(df.groupby("service")["cost"].sum())

    print("\nPrůměrná cena:")
    print(df["cost"].mean())

    print("\nNejdražší cloud služba:")
    print(df.loc[df["cost"].idxmax()])