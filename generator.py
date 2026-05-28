import random
from datetime import (
    datetime,
    timedelta
)

from config import (
    ANOMALY_CHANCE,
    NORMAL_COST_MIN,
    NORMAL_COST_MAX,
    ANOMALY_COST_MIN,
    ANOMALY_COST_MAX,
    GENERATION_INTERVAL_HOURS
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

    base_time = datetime.now().replace(
        minute=0,
        second=0,
        microsecond=0
    )

    interval_steps = random.randint(
        0,
        56
    )

    simulated_time = base_time + timedelta(
        hours=(
            interval_steps *
            GENERATION_INTERVAL_HOURS
        )
    )

    return {
        "service": random.choice(SERVICES),
        "region": random.choice(REGIONS),
        "cost": cost,
        "timestamp": simulated_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "status": "normal"
    }