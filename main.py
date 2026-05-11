from generator import generate_cloud_cost
from database import create_database, insert_cloud_cost


def main():
    create_database()

    sample_data = generate_cloud_cost()

    print(sample_data)

    insert_cloud_cost(sample_data)


if __name__ == "__main__":
    main()