# Monitors Processing Script Instruction Manual

## Overview
This manual provides detailed instructions on how to use the Python script designed for processing data monitors. The script automates data queries, validates results, and manages notifications based on configurations specified in a YAML file.


## Setup

These installation instructions assume that you have [Python 3](https://www.python.org/downloads/)
and [pip](https://pip.pypa.io/en/stable/cli/pip_install/) installed.


### 1. Clone this repository

```bash
cd && git clone https://github.com/ShouvikSharma/seen_case_study.git
```

### 2. Go to root of directory

```bash
cd seen_case_study
```

### 3. Create a Python virtual environment


Sourcing the `dependencies.sh` script sets the python virtual env and installs the requirements.txt.

```bash
python3 -m venv venv
source venv/bin/activate
chmod +x dependencies.sh
./dependencies.sh
```

### 4. Set the monitor specific parameters in the .yaml file
If we want to manually input a run date for a specific monitor then we can update the monitors.yaml, and set the run_type as manual.

```bash
run_type: "manual" 
```
Then we can run the main script with a simple command in the terminal.
```bash
python main.py
```

## Specific Monitor Execution

- To execute a specific monitor by name, provide the monitor's name as an argument when calling the `process_monitors` function within the `main` function. Replace `monitor_name=None` with `monitor_name='YourMonitorName'` where `'YourMonitorName'` is the name of the monitor you wish to run. This allows for targeted processing of individual monitors, which can be useful for testing or specific data monitoring needs.

  Example:
  
  ```python main.py "Transaction Monitor"```


  ## Prior Notification Time Period

- The `prior_notification_time_period` property in the monitor configuration is crucial for managing the frequency of notifications sent to avoid redundancy. This property defines a specific timeframe (e.g., daily, weekly, monthly) during which a notification for the same monitor should not be sent again if it has already been triggered.

### Configuration
- Set this property in the `monitors.yaml` file for each monitor as needed based on the desired alert frequency. Here is a basic example of how it might look in a YAML configuration:

  ```yaml
  monitors:
    - name: TransactionAlertMonitor
      description: Sends alerts for high-value transactions.
      prior_notification_time_period: 'monthly'
      ...

## Contributing 

### 1. Create a git branch

   ```bash
   git checkout main
   git fetch origin
   git pull origin main
   git checkout -b feature/my-dev-branch
   ```

# Project Instructions

## Overview
- After setting up the required libraries and functions, this document   provides an overview of the code structure and explains how to use the provided scripts and database.

- This manual provides instructions on how to use the Python script designed for processing monitors based on a configurable YAML file. The script performs data queries, validates results, and sends notifications according to specific monitor configurations.

## Directory and File Structure

- **database/**: Contains the sample database file `sample.db` used for storing and retrieving data required for monitoring tasks.

- **scripts/**: Contains SQL files which are executed to fetch data from the database.

- **utils/**: Contains essential utility functions that support the main application logic. This includes:
  - `helper_tasks.py`: Provides date manipulation and data validation functionalities.
  - `notification_manager.py`: Manages the sending of notifications based on the monitor outputs.

- **main.py**: The main script that executes the required actions for monitoring tasks. This file orchestrates the data fetching, processing, and notification sending.

- **dependencies.sh**: A shell script file that automates the installation of all required libraries.

- **requirements.txt**: Lists all the Python libraries needed for the project. Use this file to install dependencies via pip.


### Configuration File (monitors.yaml)

- The `monitors.yaml` file is essential for defining the behavior of various monitoring tasks. Each monitor defined in this file contains several properties that dictate how each task should operate. Below is an explanation of the key properties used within each monitor configuration:

  - `name`: A unique identifier for the monitor.
  - `owner`: The owner or responsible party for the monitor.
  - `description`: A brief description of what the monitor does.
  - `communication_channel`: The method used to communicate the results (e.g., email, Jira).
  - `monitor type`: The type of monitoring being performed (e.g., Transaction, Monthly Review).
  - `schedule`: The schedule on which the monitor runs, specified in cron format.
  - `sql_file`: The SQL file that contains the query to execute.
  - `prior_notification_time_period`: Specifies the time period to check before sending a new notification to avoid duplicates.
  - `database`: The database file to connect to when executing the SQL query.
  - `columns`: A list of columns that are expected to be in the result set of the SQL query.
  - `monitor_run_date`: Optionally specifies a fixed date to run the monitor query; if empty, the current date is used.
  - `recipients`: A list of email addresses to which the notifications should be sent.
  - `run_type`: Specifies whether the monitor run is manual or regular, allowing for flexibility in execution.

- This YAML configuration allows for precise control over monitoring and notification mechanisms based on varying requirements, enabling both daily transaction checks and specialized monitoring such as monthly spend patterns.

## Requirements
- Python 3.x
- Libraries: SQLite3, PyYAML, Pandas
- `sample.db` database file located in a `database` directory
- Python scripts `helper_tasks.py` and `notification_manager.py` in the `utils` directory

## Project Structure
- Ensure your project directory is structured as follows:

```bash
/project
|-- main_script.py   (the main Python script)
|-- monitors.yaml    (YAML configuration file)
/-- /database
   |-- sample.db    (SQLite database)
/-- /utils
   |-- helper_tasks.py
   |-- notification_manager.py
```

# Transaction Database Query Tests 

## Overview
- This script tests SQL queries on an SQLite in-memory database focusing on transaction data.
- It is built using Python's `unittest` framework.

## Requirements
- Python 3.x
- `sqlite3` module
- `pandas` library

## Running Tests
- Execute the test suite via the command line:
  ```bash
  pytest
  ```
