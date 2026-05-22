from generator import generate_cloud_cost
from database import create_database, insert_cloud_cost
from config import (
    NUMBER_OF_RECORDS,
    USE_CSV_IMPORT
)
from csv_import import import_csv_data

from analysis import (
    basic_analysis,
    detect_anomalies,
    plot_service_costs,
    plot_costs_over_time,
    plot_anomalies
)


def generate_data():
    """
    Vygeneruje cloud cost data
    nebo importuje CSV.
    """

    if USE_CSV_IMPORT:
        import_csv_data()

    else:
        for _ in range(NUMBER_OF_RECORDS):
            sample_data = generate_cloud_cost()
            insert_cloud_cost(sample_data)

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

    generate_data()

    run_analysis()


if __name__ == "__main__":
    main()