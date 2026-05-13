import random
from datetime import datetime

from config import (
    ANOMALY_CHANCE,
    NORMAL_COST_MIN,
    NORMAL_COST_MAX,
    ANOMALY_COST_MIN,
    ANOMALY_COST_MAX
)

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
    """
    Vygeneruje jeden cloud cost záznam.
    """

    anomaly = random.random() < ANOMALY_CHANCE

    if anomaly:
        cost = round(
            random.uniform(
                ANOMALY_COST_MIN,
                ANOMALY_COST_MAX
            ),
            2
        )
    else:
        cost = round(
            random.uniform(
                NORMAL_COST_MIN,
                NORMAL_COST_MAX
            ),
            2
        )

    return {
        "service": random.choice(SERVICES),
        "region": random.choice(REGIONS),
        "cost": cost,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "normal"
    }