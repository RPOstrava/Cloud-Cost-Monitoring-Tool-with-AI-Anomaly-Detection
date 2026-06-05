from flask import (
    Flask,
    render_template
)
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():

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
            region,
            cost,
            timestamp
        FROM cloud_costs
        WHERE status = 'anomaly'
        ORDER BY id DESC
        LIMIT 10
    """)

    latest_anomalies = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        total_records=total_records,
        anomalies=anomalies,
        anomaly_rate=anomaly_rate,        
        average_cost=average_cost,
        highest_cost=highest_cost,
        latest_anomalies=latest_anomalies
    )


if __name__ == "__main__":
    app.run(debug=True)