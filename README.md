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
