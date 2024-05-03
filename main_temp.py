import sqllite3
from dataclasses import dataclass
import yaml
from utils.helper_tasks import Datahelpers
from utils.notification_manager import NotificationManager
from typing import Any, Dict, List
import sys
import os
import datetime
from utils.helper_tasks import DateHelpers

@dataclass
class MonitorConfig:
    name: str
    owner: str
    monitor_type: str
    description: str
    run_type: str
    schedule: str
    sql_file: str
    recipients: List[str]
    database: str
    columns: str
    communication_channel: str
    monitor_run_date: str = None
    prior_notification_time_period: int = None


def process_monitors(config: List[MonitorConfig], monitor_name: str, conn: sqllite3.Connection) -> None:

    for monitor in config:
        if monitor_name is not None and monitor_name != config.name:
            continue

        if monitor.run_type == 'manual':
            monitor.monitor_run_date = input("Enter run date for manual run for {monitor.name}: '{YYYY-MM-DD}'")

            try:
                datetime.datetime.strptime(monitor.monitor_run_date,
                                           '%Y-%m-%d')
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD format.")
                continue
            
            ### Get the data
            datahelpers = DateHelpers(monitor)
            monitor_df = datahelpers.get_sql_data()

            # validate the dataframe
            valid: bool
            error_message: str  
            valid = datahelpers.validate_dataframe()








# Modularize
# Reusability

def main():

    monitor_name = sys.arg[1] if len(sys.arg[1])>1 else None

    with open("monitors.yaml","r") as file:
        config: List[MonitorConfig] = [MonitorConfig(**monitor) for monitor in yaml.safe_load(file)["monitors"]]


    with open("monitors.yaml","r") as file:
        config: List[MonitorConfig] = [MonitorConfig(**monitor) for monitor in yaml.safe_load(file)]
    conn = sqllite3.connect(os.path.join(os.getcwd(),'database','sample.db'))
    process_monitors(config,monitor_name, conn)

    conn.close()