import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "database/cloud_costs.db"


def load_data():
    conn = sqlite3.connect(DB_PATH)

    query = "SELECT * FROM cloud_costs"

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


def basic_analysis():
    df = load_data()

    print("\n--- BASIC ANALYSIS ---")

    print(f"Počet záznamů: {len(df)}")

    print("\nCelkové náklady podle služby:")
    print(df.groupby("service")["cost"].sum())

    print("\nPrůměrná cena:")
    print(df["cost"].mean())

    print("\nNejdražší cloud služba:")
    print(df.loc[df["cost"].idxmax()])


def plot_service_costs():
    df = load_data()

    service_costs = df.groupby("service")["cost"].sum()

    plt.figure(figsize=(8, 5))

    service_costs.plot(kind="bar")

    plt.title("Cloud Costs by Service")
    plt.xlabel("Service")
    plt.ylabel("Total Cost")

    plt.tight_layout()

    plt.show()

def plot_costs_over_time():
    
    # Zobrazí vývoj cloud nákladů v čase.
    

    df = load_data()

    # převod timestamp na datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # seřazení podle času
    df = df.sort_values("timestamp")

    plt.figure(figsize=(10, 5))

    plt.plot(df["timestamp"], df["cost"])

    plt.title("Cloud Costs Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Cost")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()    