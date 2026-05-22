# Cloud Cost Monitoring Tool with AI Anomaly Detection

A learning project focused on building a cloud cost monitoring system with AI-based anomaly detection.

The goal of this project is to understand how to design, build, debug, and gradually improve a real-world Python application using data analysis, machine learning, and software engineering practices.

---

## Project Goal

The main purpose of this project is **learning by building**.

Instead of following only tutorials, the goal is to understand how individual technologies work together in a practical project:

- generating data
- importing external datasets
- storing historical data
- analyzing trends
- visualizing cloud costs
- detecting anomalies using AI
- improving architecture and code quality

This project is intentionally built step by step to better understand how to design systems that are maintainable, testable, and scalable.

---

## Current Features

### Data Generation
- Simulated cloud cost data generation
- Multiple cloud services and regions
- Random anomaly simulation
- Simulated timestamps for monitoring scenarios

### CSV Import
- Import cloud cost data from CSV files
- External dataset support
- AI anomaly detection on imported data

### Database
- SQLite database storage
- Historical data persistence
- AI anomaly status stored in database
- Optional database reset for testing

### Data Analysis
- Cost aggregation by service
- Average cost calculation
- Highest cost detection
- AI anomaly statistics

### Data Visualization
- Cloud costs by service (bar chart)
- Cloud cost trends over time
- AI anomaly visualization

### AI / Machine Learning
- Anomaly detection using Isolation Forest
- Detection of unusual cloud spending patterns
- Statistical anomaly analysis
- Automatic anomaly labeling

---

## Technologies Used

### Backend
- Python

### Database
- SQLite

### Data Analysis
- pandas
- NumPy

### Data Visualization
- matplotlib

### Machine Learning
- scikit-learn

### Version Control
- Git
- GitHub

---

## Project Structure

```text
cloud-cost-monitor/
│
├── database/
│   └── cloud_costs.db
│
├── data/
│   └── sample_cloud_costs.csv
│
├── analysis.py
├── config.py
├── csv_import.py
├── database.py
├── generator.py
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone repository

```bash
git clone https://github.com/RPOstrava/Cloud-Cost-Monitoring-Tool-with-AI-Anomaly-Detection.git
cd Cloud-Cost-Monitoring-Tool-with-AI-Anomaly-Detection
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run project

```bash
python main.py
```

---

## Configuration

The project can be configured through `config.py`.

Example settings:

- simulated data generation
- CSV import mode
- AI anomaly sensitivity
- database reset for testing
- number of generated records

---

## Learning Approach

This project is intentionally developed incrementally.

The goal is not only to build a working application, but also to understand:

- debugging
- refactoring
- data analysis
- machine learning basics
- project structure
- Git workflow
- real development process

---

## Planned Technologies / Features

The project will gradually evolve and may include:

- Flask dashboard (web UI)
- Browser-based charts
- Better anomaly visualization
- Cost filtering by service/region
- Real-time monitoring simulation
- Docker containerization
- Improved project architecture
- Cloud deployment experiments

---

## Project Status

**Work in progress 🚀**

This repository is actively developed step by step as part of a practical learning journey.