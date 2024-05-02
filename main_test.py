import unittest
from unittest.mock import patch
import sqlite3
import yaml
from main import process_monitors, DateHelpers
from unittest.mock import patch

class TestProcessMonitors(unittest.TestCase):
    '''
    Class for testing different components of the process monitor program.

    Args:
        unittest.TestCase: Base class for all test cases.
    '''

    @classmethod
    def setUpClass(cls) -> None:
        with open("monitors.yaml","r") as file:
            cls.config = yaml.safe_load()

    @patch('builtins.input',side_effect = ['2023-01-01'])
    def test_manual_run_date_entry(self,mock_input) -> None:
        # mock database connect
        conn = sqlite3.connect(':memory')

        # Test with a monitor configured for a manual run
        process_monitors(self.config,conn,monitor_name ='ManualMonitor')

        # verify that the run date was correctly populated for the given date.
        mock_input.assert_called_once_with("Enter the run date for Manual Monitor (YYYY-MM-DD): ")

        # Close database connection
        conn.close()

    def test_get_sql_data(self):
        # Define a sample monitor configuration
        monitor = {
            'sql_file': 'sample_query.sql',  # Assuming the SQL file exists and contains valid query
            # Other necessary fields for the DateHelpers class initialization
        }

        # Initialize DateHelpers with the sample monitor configuration
        datahelpers = DateHelpers(monitor)

        # Call the get_sql_data() function
        monitor_df = datahelpers.get_sql_data()

        # Check if the returned DataFrame is not None and has some data
        self.assertIsNotNone(monitor_df)
        self.assertNotEqual(len(monitor_df), 0)  # Assuming the query returns some data

    @classmethod
    def setUpClass(cls) -> None:
        with open("monitors.yaml","r") as file:
            cls.config = yaml.safe_load(file)


if __name__ == '__main__':
    unittest.main()
