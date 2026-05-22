from generator import generate_cloud_cost
from database import create_database, insert_cloud_cost
from config import NUMBER_OF_RECORDS

from analysis import (
    basic_analysis,
    detect_anomalies,
    plot_service_costs,
    plot_costs_over_time,
    plot_anomalies
)


def generate_data():
    """
    Vygeneruje cloud cost data.
    """

    for _ in range(NUMBER_OF_RECORDS):
        sample_data = generate_cloud_cost()
        insert_cloud_cost(sample_data)

    print(f"{NUMBER_OF_RECORDS} záznamů bylo uloženo.")


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