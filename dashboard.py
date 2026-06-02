from flask import Flask
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

    conn.close()

    return f"""
    <h1>Cloud Cost Monitoring Dashboard</h1>

    <p>Total Records: {total_records}</p>

    <p>Detected Anomalies: {anomalies}</p>

    <p>Average Cost: {average_cost}</p>

    <p>Highest Cost: {highest_cost}</p>
    """


if __name__ == "__main__":
    app.run(debug=True)