# dbt-silver

This repository contains a seen case study project that defines "Silver" data models that are built in Databricks Unity Catalog. Learn more about how we model our data at Avant in [_Medallion Architecture + dbt_](https://avantinc.atlassian.net/wiki/spaces/DL/pages/3132522555/Medallion+Architecture+dbt). Continue reading to learn how to contribute to the `dbt_silver` project.


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
After setting up the required libraries and functions, this document provides an overview of the code structure and explains how to use the provided scripts and database.

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

- This YAML configuration allows for precise control over monitoring and notification mechanisms based on varying requirements, enabling both daily transaction checks and specialized monitoring such as monthly spend patterns.

