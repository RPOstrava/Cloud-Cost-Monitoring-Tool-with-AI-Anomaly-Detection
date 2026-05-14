from generator import generate_cloud_cost
from database import create_database, insert_cloud_cost
from analysis import (
    basic_analysis,
    plot_service_costs,
    plot_costs_over_time,
    detect_anomalies
)
from config import NUMBER_OF_RECORDS


def main():
    create_database()

    number_of_records = NUMBER_OF_RECORDS

    for _ in range(number_of_records):
        sample_data = generate_cloud_cost()
        insert_cloud_cost(sample_data)

    print(f"{number_of_records} záznamů bylo uloženo.")

    basic_analysis()    
    detect_anomalies()
    plot_service_costs()
    plot_costs_over_time()
    


if __name__ == "__main__":
    main()

