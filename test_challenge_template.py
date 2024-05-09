import unittest
import sqlite3
import os
import yaml
from challenge_template import run_query, load_config
from unittest.mock import patch

class TestLoadConfig(unittest.TestCase):
    def test_load_config(self):
        # Test loading configuration from YAML file
        with open("monitors.yaml", "w") as file:
            yaml.dump({"monitors": [
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
        ]}, file)
        config = load_config()
        self.assertIsInstance(config, list)
        self.assertEqual(len(config), 1)
        self.assertEqual(config[0].name, "Monitor 1")
        os.remove("monitors.yaml")

if __name__ == '__main__':
    unittest.main()
