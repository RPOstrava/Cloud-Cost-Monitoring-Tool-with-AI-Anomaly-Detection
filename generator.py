import random
from datetime import datetime


SERVICES = [
    "compute",
    "storage",
    "database",
    "network",
    "ai-service"
]

REGIONS = [
    "eu-central",
    "us-east",
    "asia-east"
]


def generate_cloud_cost():

    #Vygeneruje jeden cloud cost záznam.


    # 5 % šance na anomálii
    anomaly = random.random() < 0.05

    if anomaly:
        cost = round(random.uniform(300, 1000), 2)
    else:
        cost = round(random.uniform(5, 50), 2)

    return {
        "service": random.choice(SERVICES),
        "region": random.choice(REGIONS),
        "cost": cost,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "normal"
    }