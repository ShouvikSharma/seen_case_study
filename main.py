from utils.helper_tasks import DateHelpers
from utils.notification_manager import NotificationManager
import sqlite3
from collections import namedtuple 
import pandas as pd
import os
from datetime import datetime

datahelpers = DateHelpers(None,'transactions.sql','sample.db')

# Reading the base sql
monitor_df = datahelpers.get_sql_data()


# Usage
notification_manager = NotificationManager("user@example.com",)
notification_manager.send_email("Hello", "This is a test email.")
notification_manager.send_slack("#general", "This is a test Slack message.")
notification_manager.create_jira_ticket("Issue 123", "Here is a problem that needs attention.")