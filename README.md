
# Real-time User Login Data Pipeline with Kafka

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![Kafka](https://img.shields.io/badge/Apache_Kafka-2.8+-red)](https://kafka.apache.org/)

A Kafka-based data pipeline that processes user login events, filters them by platform (iOS/Android), and handles missing data. Built with Python, Docker, and Confluent Kafka.


## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Data Flow](#data-flow)
- [Code Explanation](#code-explanation)
- [License](#license)

## Features
- Real-time message streaming with Kafka
- Automated Docker container setup
- Data filtering by device type (iOS/Android)
- Missing data handling
- Multi-topic message routing

## Prerequisites
- [Python](https://www.python.org/) 3.6+
- [Docker](https://www.docker.com/) Desktop
- pip package manager

## Installation
Clone the repository:
   ```bash
   git clone https://github.com/vijayrampatel/Data-pipeline-Kafka.git
   cd Data-pipeline-Kafka
   ```

## Quick Start
1. Start Kafka infrastructure:
   ```bash
   docker-compose -f docker-compose.yml up -d
   ```
   This initializes Kafka, Zookeeper, and starts the producer sending messages to the `user-login` topic.

2. Run the main consumer:
   ```bash
   python user-login-consumer.py
   ```
   This script consumes messages from the `user-login` topic and routes them to platform-specific topics.

3. In separate terminals, run platform-specific consumers:
   ```bash
   python ios-user-login.py
   python android-user-login.py
   python missing-data-login.py
   ```
   These scripts consume and display messages from their respective topics.

## Data Flow
1. **Producer**: Generates simulated user login events with:
   - User ID
   - Device type
   - Timestamp
   - Location data

2. **Main Consumer** (`user-login-consumer.py`):
   - Processes raw messages
   - Routes data to appropriate topics:
     - `ios-user-login`
     - `android-user-login`
     - `missing-data-login`

3. **Platform Consumers**:
   - Display filtered results from their respective topics

## Flow Chart
![Data Pipeline Flowchart](https://github.com/vijayrampatel/Data-pipeline-Kafka/assets/145386038/52db37eb-7b2c-4c36-a678-13fd01a4b576)

## Code Explanation
1. **Kafka Configuration**: Setup Kafka Producer and Consumer.
2. **Message Processing**:
   - Convert incoming string messages to dictionaries.
   - Filter data based on the device type.
   - Route messages to corresponding partitions/topics.
   - Convert timestamps to readable datetime format.
3. **Data Segmentation**: Users are categorized into three topics:
   - `ios-user-login` for iOS users.
   - `android-user-login` for Android users.
   - `missing-data-login` for users missing platform details.

## Running Consumers
Execute the following scripts from the project directory:

- **iOS User Consumer:**
  ```bash
  python ios-user-login.py
  ```
  This script consumes and displays only iOS user logins.

- **Android User Consumer:**
  ```bash
  python android-user-login.py
  ```
  This script consumes and displays only Android user logins.

- **Missing Data Consumer:**
  ```bash
  python missing-data-login.py
  ```
  This script consumes and displays logins where the platform type is missing.

These consumers will continuously listen for messages and display them once data arrives in their respective partitions.

## License
This project is licensed under the [MIT License](LICENSE).

