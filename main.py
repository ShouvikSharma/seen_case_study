from utils.helper_tasks import DateHelpers
from utils.notification_manager import NotificationManager
import yaml
import importlib.util
import os
import sqlite3
from collections import namedtuple 
import pandas as pd
import os
from datetime import datetime


with open("monitors.yaml", "r") as file:
    config = yaml.safe_load(file)

for monitor in config["monitors"]:
    print("Monitor:", monitor['name'])
    print("Monitor date:", monitor.get('monitor_run_date'))

    ## Load the underlying sql script
    datahelpers = DateHelpers(monitor)
    monitor_df = datahelpers.get_sql_data()

    print(monitor_df.shape[0])

    ## Send notification base on the communication channel
    # notification_manager = NotificationManager("user@example.com",communication_channel=monitor['communication_channel'])
    # notification_manager.send_notification("Monitor Run", f"Monitor {monitor['name']} has run successfully.")
