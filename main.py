from generator import generate_cloud_cost
from database import create_database, insert_cloud_cost
from analysis import basic_analysis


def main():
    create_database()

    number_of_records = 100

    for _ in range(number_of_records):
        sample_data = generate_cloud_cost()
        insert_cloud_cost(sample_data)

    print(f"{number_of_records} záznamů bylo uloženo.")

    basic_analysis()    


if __name__ == "__main__":
    main()

