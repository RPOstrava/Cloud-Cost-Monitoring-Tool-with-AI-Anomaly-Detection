import pandas as pd

from database import insert_cloud_cost


CSV_PATH = "data/sample_cloud_costs.csv"


def import_csv_data():
    """
    Načte cloud cost data z CSV
    a uloží je do SQLite.
    """

    df = pd.read_csv(CSV_PATH)

    for _, row in df.iterrows():

        cloud_cost = {
            "service": row["service"],
            "region": row["region"],
            "cost": row["cost"],
            "timestamp": row["timestamp"],
            "status": row["status"]
        }

        insert_cloud_cost(cloud_cost)

    print(
        f"{len(df)} CSV záznamů bylo importováno."
    )