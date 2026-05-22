import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from database import update_anomaly_status
from config import (
    AI_CONTAMINATION,
    AI_RANDOM_STATE
)

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

def detect_anomalies():
    
    #Detekuje podezřelé cloud náklady pomocí AI.
    

    df = load_data()

    # model dostane jen cost hodnoty
    X = df[["cost"]]

    model = IsolationForest(
    contamination=AI_CONTAMINATION,
    random_state=AI_RANDOM_STATE
    )

    model.fit(X)

    predictions = model.predict(X)

    # -1 = anomaly
    df["prediction"] = predictions

    anomalies = df[df["prediction"] == -1]

    normal_count = len(df[df["prediction"] == 1])

    anomaly_count = len(anomalies)

    anomaly_rate = (
        anomaly_count / len(df)
    ) * 100

    for record_id in anomalies["id"]:
        update_anomaly_status(record_id)

    print("\n--- AI ANOMALY DETECTION ---")
    print(f"Normální záznamy: {normal_count}")

    print(f"Anomálie: {anomaly_count}")

    print(
        f"Anomaly rate: "
        f"{anomaly_rate:.2f}%"
    )    

    print("\nPoslední detekované anomálie:")

    print(
        anomalies[
            ["service", "region", "cost", "timestamp"]
        ].tail(20)
    )

def plot_anomalies():
    
       # Zobrazí cloud costs v čase
       # a zvýrazní AI anomálie.
    

    df = load_data()

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    normal = df[df["status"] == "normal"]
    anomalies = df[df["status"] == "anomaly"]

    plt.figure(figsize=(10, 5))

    # normální hodnoty
    plt.plot(
        normal["timestamp"],
        normal["cost"],
        label="Normal Costs"
    )

    # anomálie
    plt.scatter(
        anomalies["timestamp"],
        anomalies["cost"],
        label="Anomalies"
    )

    plt.title("AI Anomaly Detection")
    plt.xlabel("Timestamp")
    plt.ylabel("Cost")

    plt.legend()

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()