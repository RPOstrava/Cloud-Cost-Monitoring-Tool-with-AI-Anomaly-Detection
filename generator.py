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

SERVICE_COST_RANGES = {
    "network": (5, 25),
    "storage": (10, 40),
    "compute": (20, 80),
    "database": (40, 120),
    "ai-service": (60, 200)
}

def generate_cloud_cost():
    """
    Vygeneruje jeden cloud cost záznam.
    """

    anomaly = random.random() < ANOMALY_CHANCE

    service = random.choice(SERVICES)

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
    hour = simulated_time.hour

    if 0 <= hour < 6:

        load_multiplier = 0.7

    elif 6 <= hour < 18:

        load_multiplier = 1.0

    else:

        load_multiplier = 1.3

    if anomaly:

        cost = round(
            random.uniform(
                ANOMALY_COST_MIN,
                ANOMALY_COST_MAX
            ),
            2
        )

    else:

        min_cost, max_cost = (
            SERVICE_COST_RANGES[service]
        )

        cost = round(
            random.uniform(
                min_cost,
                 max_cost
            ) * load_multiplier,
            2
        )
    

    return {
        "service": service,
        "region": random.choice(REGIONS),
        "cost": cost,
        "timestamp": simulated_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "status": "normal"
    }