import sqlite3
import os

def setup_database():
    # Define the path to your SQLite database
    db_path = os.path.join(os.getcwd(), 'database', 'sample.db')

    # Connect to SQLite database
    conn = sqlite3.connect(db_path)

    # Create cursor object to execute SQL commands
    cursor = conn.cursor()

    # SQL to create a table if it does not exist
    create_table_query = """
    CREATE TABLE IF NOT Exists notification_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        communication_channel TEXT,
        message TEXT,
        account_id INTEGER,
        sent_at DATETIME,
        monitor_name TEXT,
        FOREIGN KEY (account_id) REFERENCES accounts(account_id)  -- Assuming you have an accounts table
    );
    """

    # Execute the query
    cursor.execute(create_table_query)

    # Commit the changes
    conn.commit()

    # Close cursor and connection
    cursor.close()
    conn.close()

def main():
    # Set up the database (ensure the logging table is ready)
    setup_database()

if __name__ == '__main__':
    main()
