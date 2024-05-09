import unittest
import os
from unittest.mock import patch, mock_open
from challenge_template import load_config

class TestLoadConfig(unittest.TestCase):
    def setUp(self):
        # Create a temporary YAML file with sample data
        self.temp_yaml = "temp_monitors.yaml"
        with open(self.temp_yaml, "w") as file:
            file.write("""
                monitors:
                    - name: Monitor 1
                      owner: Owner 1
                      monitor_type: Type 1
                      description: Description 1
                      prior_notification_time_period: Period 1
                      database: Database 1
                      columns: Columns 1
                      monitor_run_date: Date 1
                      sql: SQL 1
                      schedule: Schedule 1
                      communication_channel: Channel 1
                      recipients:
                        - Recipient 1
                      run_type: Type 1
            """)

    def tearDown(self):
        # Remove the temporary YAML file
        if os.path.exists(self.temp_yaml):
            os.remove(self.temp_yaml)

    @patch("builtins.open", new_callable=mock_open)
    @patch("yaml.safe_load")
    def test_load_config(self, mock_yaml_load, mock_open):
        
        # Configure mock to return sample data
        mock_yaml_load.return_value = {"monitors": [
            {
                "name": "Monitor 1",
                "owner": "Owner 1",
                "monitor_type": "Type 1",
                "description": "Description 1",
                "prior_notification_time_period": "Period 1",
                "database": "Database 1",
                "columns": "Columns 1",
                "monitor_run_date": "Date 1",
                "sql": "SQL 1",
                "schedule": "Schedule 1",
                "communication_channel": "Channel 1",
                "recipients": ["Recipient 1"],
                "run_type": "Type 1"
            }
        ]}

        # Call load_config function
        config = load_config()
        
        # Assertions
        self.assertIsInstance(config, list)
        self.assertEqual(len(config), 1)  # Check for single monitor
        self.assertEqual(config[0].name, "Monitor 1")

if __name__ == '__main__':
    unittest.main()