import sqlite3
from collections import namedtuple 
import pandas as pd
import os
from datetime import datetime


class DateHelpers:
    def __init__(self, monitor_config):
        self.monitor_run_date = monitor_config.get('monitor_run_date')
        self.query_name = monitor_config.get('sql_file')
        self.database_name = monitor_config.get('database')

    def date_parameter(self):
        if  self.monitor_run_date == '':
            current_datetime = datetime.now()
            self.current_date = current_datetime.strftime('%Y-%m-%d')
            return self.current_date
        else: 
            self.current_date = datetime.strptime(self.monitor_run_date,'%Y-%m-%d').date()
            return self.current_date
        

    def get_sql_data(self):

        # Connect to the database
        conn = sqlite3.connect(os.path.join(os.getcwd(), 'database', self.database_name))

        # Read SQL file
        def rs(fname, conn, **params ):
            """ Returns a pandas dataframe from external file. """
            with open(fname, 'r') as f:
                # Read the SQL query from the file        
                sql_query = f.read()
                
                # Format the query with provided parameters
                # This assumes that you have placeholders in your SQL file like {placeholder_name}
                formatted_query = sql_query.format(**params)

                # Execute the query and return a DataFrame
                return pd.read_sql_query(formatted_query, conn)

        # transactions
        query = os.path.join(os.path.join(os.getcwd(), 'scripts', self.query_name )) 
        df = rs(query, conn, date = self.date_parameter())

        # Close the connection
        conn.close()

        # Show the Dataframe
        return df