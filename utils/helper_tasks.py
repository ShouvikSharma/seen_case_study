import sqlite3
import os
import pandas as pd
from datetime import datetime, timedelta
import time
import pyarrow

class DateHelpers:

    def __init__(self, monitor_config):
        self.monitor_run_date = monitor_config.get('monitor_run_date')
        self.query_name = monitor_config.get('sql_file')
        self.database_name = monitor_config.get('database')
        self.database_path = os.path.join(os.getcwd(), 'database', self.database_name)

    def retry(times, exceptions):
        def decorator(func):
            def newfn(*args, **kwargs):
                attempt = 0
                while attempt < times:
                    try:
                        return func(*args, **kwargs)
                    except exceptions:
                        print(
                            f"ERROR - Exception thrown when attempting to run {func}, attempt {attempt} of {times}"
                        )
                        print(f"Retrying in 3 minutes...")
                        time.sleep(180)
                        attempt += 1
                return func(*args, **kwargs)

            return newfn

        return decorator

    def date_parameter(self):
        if self.monitor_run_date == '':
            return datetime.now().strftime('%Y-%m-%d')
        else:
            return datetime.strptime(self.monitor_run_date, '%Y-%m-%d').date().strftime('%Y-%m-%d')

    @retry(times=2, exceptions=(pyarrow._flight.FlightCancelledError))
    def get_sql_data(self):
        with sqlite3.connect(self.database_path) as conn:
            query_path = os.path.join(os.getcwd(), 'scripts', self.query_name)
            with open(query_path, 'r') as f:
                sql_query = f.read().format(date=self.date_parameter())
            return pd.read_sql_query(sql_query, conn)

    def validate_account_ids(self):
        dataframe = self.get_sql_data()
        account_ids = dataframe['account_id'].unique().tolist()
        query = 'SELECT account_id FROM accounts WHERE account_id IN ({})'.format(', '.join(['?']*len(account_ids)))
        
        with sqlite3.connect(self.database_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, account_ids)
            existing_account_ids = {row[0] for row in cursor.fetchall()}
            missing_ids = set(account_ids) - existing_account_ids

        return existing_account_ids, missing_ids

    def validate_dataframe(self, monitor_df, monitor):
        required_columns = monitor.get('required_columns', [])
        if not all(col in monitor_df.columns for col in required_columns):
            return False, "The dataframe does not have the required columns."
        if monitor_df[required_columns].isnull().any().any():
            return False, "The dataframe has missing values in the required columns."
        if monitor_df.duplicated().any():
            monitor_df.drop_duplicates(inplace=True)
            print("Error: The dataframe has duplicates and deduplication has been performed.")

        existing_account_ids, missing_ids = self.validate_account_ids()
        if missing_ids:
            return False, f"Warning: The following account IDs do not exist in the accounts table: {missing_ids}"

        print("All account IDs from the monitor exist in the accounts table.")
        return True, None
    
    def get_start_of_period(self,period):
        now = datetime.now()
        if period == 'day':
            return now.replace(hour=0, minute=0, second=0, microsecond=0)
        elif period == 'week':
            start_of_week = now - timedelta(days=now.weekday())
            return start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
        elif period == 'month':
            return now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        else:
            raise ValueError("Unsupported time period. Choose 'day', 'week', or 'month'.")

    def has_notification_been_sent_in_period(self,database_path, monitor_name, account_id, period):
        start_of_period = self.get_start_of_period(period)
        with sqlite3.connect(database_path) as conn:
            query = """
            SELECT EXISTS(
                SELECT 1 FROM notification_logs
                WHERE monitor_name = ? AND account_id = ? AND sent_at >= ?
            )
            """
            cursor = conn.cursor()
            cursor.execute(query, (monitor_name, account_id, start_of_period.strftime('%Y-%m-%d %H:%M:%S')))
            result = cursor.fetchone()
        return result[0] == 1
