# Cloud Cost Monitoring Tool with AI Anomaly Detection

A learning project focused on building a cloud cost monitoring system with AI-based anomaly detection.

The goal of this project is to understand how to design, build, debug, and gradually improve a real-world Python application using data analysis and machine learning.

---

## Project Goal

The main purpose of this project is **learning by building**.

Instead of following only tutorials, the goal is to understand how individual technologies work together in a practical project:

- generating data
- storing historical data
- analyzing data
- visualizing trends
- detecting anomalies using AI
- gradually improving architecture and code quality

This project is intentionally built step by step to understand how the whole system works and how to make it stable and maintainable.

---

## Current Features

### Data Generation
- Simulated cloud cost data generation
- Multiple cloud services and regions
- Random anomaly simulation

### Database
- SQLite database storage
- Historical data persistence
- Automatic data growth over time

### Data Analysis
- Cost aggregation by service
- Average cost calculation
- Highest cost detection

### Data Visualization
- Cloud costs by service (bar chart)
- Cloud cost trends over time (line chart)

### AI / Machine Learning
- Anomaly detection using Isolation Forest
- Detection of unusual cloud spending patterns

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

## Planned Technologies / Features

The project will gradually evolve and may include:

- Flask dashboard (web UI)
- Better anomaly visualization
- AI anomaly status stored in database
- Dashboard charts in browser
- Cost filtering by service/region
- Docker containerization
- Improved project architecture

---

## Installation

Clone repository:

```bash
git clone https://github.com/RPOstrava/Cloud-Cost-Monitoring-Tool-with-AI-Anomaly-Detection.git
cd Cloud-Cost-Monitoring-Tool-with-AI-Anomaly-Detection

Install dependencies: 
pip install -r requirements.txt

Run project:
python main.py

Learning Approach

This project is intentionally developed incrementally.

The goal is not only to build a working application, but also to understand:

debugging
refactoring
data analysis
machine learning basics
project structure
Git workflow
real development process
Project Status

Work in progress 🚀