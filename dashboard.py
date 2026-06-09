from flask import (
    Flask,
    render_template,
    Response,
    request
)

import sqlite3
import io

import pandas as pd

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route("/service-chart")
def service_chart():

    conn = sqlite3.connect(
        "database/cloud_costs.db"
    )

    query = """
        SELECT
            service,
            SUM(cost) AS total_cost
        FROM cloud_costs
        GROUP BY service
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    plt.figure(
        figsize=(8, 4)
    )

    plt.bar(
        df["service"],
        df["total_cost"]
    )

    plt.title(
        "Cloud Costs by Service"
    )

    plt.tight_layout()

    img = io.BytesIO()

    plt.savefig(
        img,
        format="png"
    )

    plt.close()

    img.seek(0)

    return Response(
        img.getvalue(),
        mimetype="image/png"
    )


@app.route("/anomaly-chart")
def anomaly_chart():

    conn = sqlite3.connect(
        "database/cloud_costs.db"
    )

    query = """
        SELECT
            timestamp,
            cost
        FROM cloud_costs
        WHERE status = 'anomaly'
        ORDER BY id DESC
        LIMIT 50
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    plt.figure(
        figsize=(10, 4)
    )

    plt.scatter(
        df["timestamp"],
        df["cost"]
    )

    plt.title(
        "Anomalies Over Time"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    img = io.BytesIO()

    plt.savefig(
        img,
        format="png"
    )

    plt.close()

    img.seek(0)

    return Response(
        img.getvalue(),
        mimetype="image/png"
    )
    
@app.route("/anomalies-by-service-chart")
def anomalies_by_service_chart():

    conn = sqlite3.connect(
        "database/cloud_costs.db"
    )

    query = """
        SELECT
            service,
            COUNT(*) AS anomaly_count
        FROM cloud_costs
        WHERE status = 'anomaly'
        GROUP BY service
        ORDER BY anomaly_count DESC
    """

    df = pd.read_sql_query(
        query,
        conn
    )

    conn.close()

    plt.figure(
        figsize=(8, 4)
    )

    plt.bar(
        df["service"],
        df["anomaly_count"]
    )

    plt.title(
        "Anomalies by Service"
    )

    plt.tight_layout()

    img = io.BytesIO()

    plt.savefig(
        img,
        format="png"
    )

    plt.close()

    img.seek(0)

    return Response(
        img.getvalue(),
        mimetype="image/png"
    )    


@app.route("/")
def home():
    
    selected_service = request.args.get(
        "service",
        "all"
    )

    conn = sqlite3.connect(
        "database/cloud_costs.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM cloud_costs"
    )

    total_records = cursor.fetchone()[0]

    cursor.execute("""
        SELECT COUNT(*)
        FROM cloud_costs
        WHERE status = 'anomaly'
    """)

    anomalies = cursor.fetchone()[0]

    anomaly_rate = round(
        (anomalies / total_records) * 100,
        2
    )

    cursor.execute(
        "SELECT AVG(cost) FROM cloud_costs"
    )

    average_cost = round(
        cursor.fetchone()[0],
        2
    )

    cursor.execute(
        "SELECT MAX(cost) FROM cloud_costs"
    )

    highest_cost = cursor.fetchone()[0]

    cursor.execute("""
        SELECT
            service,
            cost,
            timestamp
        FROM cloud_costs
        WHERE status = 'anomaly'
        ORDER BY id DESC
        LIMIT 10
    """)

    latest_anomalies = cursor.fetchall()

    cursor.execute("""
        SELECT
            service,
            cost,
            timestamp
        FROM cloud_costs
        ORDER BY cost DESC
        LIMIT 10
    """)

    most_expensive_records = cursor.fetchall()
    
    cursor.execute("""
    SELECT
        service,
        COUNT(*) AS anomaly_count
    FROM cloud_costs
    WHERE status = 'anomaly'
    GROUP BY service
    ORDER BY anomaly_count DESC
    """)

    anomalies_by_service = cursor.fetchall()
    
    most_problematic_service = (
    anomalies_by_service[0][0]
)
    cursor.execute("""
        SELECT
            region,
            COUNT(*) AS anomaly_count
        FROM cloud_costs
        WHERE status = 'anomaly'
        GROUP BY region
        ORDER BY anomaly_count DESC
    """)

    anomalies_by_region = cursor.fetchall()

    most_problematic_region = (
        anomalies_by_region[0][0]
    )
    conn.close()

    return render_template(
        "index.html",
        total_records=total_records,
        anomalies=anomalies,
        anomaly_rate=anomaly_rate,
        average_cost=average_cost,
        highest_cost=highest_cost,
        latest_anomalies=latest_anomalies,
        most_expensive_records=most_expensive_records,
        anomalies_by_service=anomalies_by_service,
        most_problematic_service=most_problematic_service,
        most_problematic_region=most_problematic_region,
    )


if __name__ == "__main__":
    app.run(debug=True)