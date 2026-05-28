# počet generovaných záznamů při spuštění
NUMBER_OF_RECORDS = 100

# pravděpodobnost anomálie (5 %)
ANOMALY_CHANCE = 0.05

# normální cenové rozpětí
NORMAL_COST_MIN = 5
NORMAL_COST_MAX = 50

# podezřelé (anomaly) rozpětí
ANOMALY_COST_MIN = 300
ANOMALY_COST_MAX = 1000

# AI anomaly detection
AI_CONTAMINATION = 0.05
AI_RANDOM_STATE = 42

# data source
USE_CSV_IMPORT = False

# simulated time interval
GENERATION_INTERVAL_HOURS = 3

# database reset
RESET_DATABASE = False

# application mode
APP_MODE = "dev"

if APP_MODE == "dev":
    MONITORING_DELAY_SECONDS = 0.1
else:
    MONITORING_DELAY_SECONDS = 1

# application mode, da se prepnout na "demo" 
APP_MODE = "dev"

