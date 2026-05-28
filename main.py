from generator import generate_cloud_cost
from database import create_database, insert_cloud_cost
from config import (
    NUMBER_OF_RECORDS,
    USE_CSV_IMPORT,
    MONITORING_DELAY_SECONDS,
    APP_MODE
)
from csv_import import import_csv_data

from analysis import (
    basic_analysis,
    detect_anomalies,
    plot_service_costs,
    plot_costs_over_time,
    plot_anomalies
)
import time


def generate_data():
    """
    Vygeneruje cloud cost data
    nebo importuje CSV.
    """

    if USE_CSV_IMPORT:
        import_csv_data()

    else:
        for index in range(NUMBER_OF_RECORDS):

            sample_data = generate_cloud_cost()

            insert_cloud_cost(sample_data)

            print(
                f"Monitoring record "
                f"{index + 1}/"
                f"{NUMBER_OF_RECORDS}"
            )

            time.sleep(
                MONITORING_DELAY_SECONDS
            )

        print(
            f"{NUMBER_OF_RECORDS} "
            f"záznamů bylo uloženo."
        )


def run_analysis():
    """
    Spustí analýzu a grafy.
    """

    basic_analysis()

    detect_anomalies()

    plot_service_costs()

    plot_costs_over_time()

    plot_anomalies()


def main():
    create_database()

    print(
        f"Running in "
        f"{APP_MODE.upper()} "
        f"mode"
    )

    generate_data()

    run_analysis()

if __name__ == "__main__":
    main()