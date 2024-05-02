import sqlite3
import yaml
import os
from utils.helper_tasks import DateHelpers
from utils.notification_manager import NotificationManager
import sys
from typing import Any, Dict
import datetime
from dataclasses import dataclass

def process_monitors(config: Dict[str,Any], db_connection:sqlite3.Connection, monitor_name: str =None) -> None:
    for monitor in config["monitors"]:

        if monitor_name is not None and monitor['name'] != monitor_name:
            continue 

        # Handle manual run date entry
        if monitor['run_type'] == "manual":
            monitor['monitor_run_date'] = input(f"Enter the run date for {monitor['name']} (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(monitor['monitor_run_date'], "%Y-%m-%d")
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD format.")
                continue

        # Load the underlying sql script
        datahelpers = DateHelpers(monitor)
        monitor_df = datahelpers.get_sql_data()

        print("Monitor:", monitor['name'])
        print("Description:", monitor['description'])
        print("Monitor Date:", datahelpers.date_parameter())
        print("Initial Audience size:", len(monitor_df))

        # Validate the dataframe
        valid: bool
        error_message: str
        valid, error_message = datahelpers.validate_dataframe(monitor_df, monitor)
        if not valid:
            print(error_message)
            continue
        
        
        # Update monitor_df to exclude account_ids where notification has already been sent in the specified period
        monitor_df = monitor_df[monitor_df['account_id'].apply(lambda account_id: not datahelpers.has_notification_been_sent_in_period(os.path.join(os.getcwd(), 'database', 'sample.db'), monitor['name'], account_id, period = monitor.get('prior_notification_time_period')))]

        # If there are no account_ids left to process, skip to next monitor
        if monitor_df.empty:
            print("All accounts have already received notifications for this period.")
            print('\n')
            continue

        ## Send notification base on the communication channel
        notification_manager = NotificationManager(monitor['recipients'],communication_channel=monitor['communication_channel'],db_connection = db_connection,dataframe = monitor_df, monitor_name = monitor['name'])
        notification_manager.send_notification("Monitor Run", f"Monitor {monitor['name']} has created alerts successfully.")
        print('\n')

def main():

    monitor_name = sys.argv[1] if len(sys.argv) > 1 else None

    with open("monitors.yaml", "r") as file:
        config: Dict[str,Any] = yaml.safe_load(file)

    # Process each monitor defined in the YAML configuration
    conn = sqlite3.connect(os.path.join(os.getcwd(), 'database', 'sample.db'))
    process_monitors(config, conn ,monitor_name=monitor_name) 

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
