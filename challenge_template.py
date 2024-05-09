import argparse
from dataclasses import dataclass
from datetime import datetime
import sqlite3
import os
import yaml
from typing import List, Tuple, Any, Dict, Optional

@dataclass
class Monitor:
    name: str
    owner: str
    monitor_type: str
    description: str
    prior_notification_time_period: str
    database: str
    columns: str
    monitor_run_date: str
    sql: str
    schedule: str
    communication_channel: str
    recipients: List[str]
    run_type: str

def load_config() -> List[Monitor]:
    with open("monitors.yaml","r") as file:
        config: List[Monitor] = [Monitor(**monitor) for monitor in yaml.safe_load(file)["monitors"]]
    return config

def run_query(sql: str, params: List[Any], run_date: str = None) -> List[Tuple]:    
    with sqlite3.connect(os.path.join(os.getcwd(),'database','sample.db')) as conn:
        cursor = conn.cursor()
        cursor.execute(sql.format(date = run_date))
        list_object = cursor.fetchall()
    return list_object  

def notify(channel: str, message: str) -> None:
    print(f"Channel :'{channel},message = '{message}")
    pass

def main(run_date: str) -> None:

    # run_date definition
    if run_date is None:
        run_date = datetime.today().strftime('%Y-%m-%d')

    configs = load_config()
    for config in configs:
        monitor_result = run_query(config.sql,config,run_date)
        print(monitor_result)
        if monitor_result :
            notify(config.communication_channel,message = 'Account Alert')
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run monitoring alerts for fraud detection.")
    parser.add_argument('-d', '--date', type=str, default=datetime.now().strftime("%Y-%m-%d"),
                        help='The date to run the monitors for, format YYYY-MM-DD. Defaults to today.')

    args = parser.parse_args()
    main(args.date)
