import unittest
import sqlite3
import pandas as pd

class TestDatabaseQueries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Connect to an in-memory SQLite database for testing
        cls.conn = sqlite3.connect(':memory:')
        cls.setup_database(cls.conn)

    @classmethod
    def setup_database(cls, conn):
        # Create table and insert data
        conn.execute('''
            CREATE TABLE transactions (
                transaction_id INTEGER PRIMARY KEY,
                account_id TEXT,
                transaction_date TEXT,
                transaction_amount REAL
            );
        ''')
        # Insert test data
        transactions = [
            (1, '001', '2023-04-13', 500),
            (2, '002', '2023-04-13', 100),
            (3, '001', '2023-04-13', 350),
            (4, '003', '2023-04-13', 700),
            (5, '002', '2023-04-12', 450),
        ]
        conn.executemany('''
            INSERT INTO transactions (transaction_id, account_id, transaction_date, transaction_amount)
            VALUES (?, ?, ?, ?);
        ''', transactions)
        conn.commit()

    def test_high_value_transactions(self):
        # Test SQL to find transactions above $300
        df = pd.read_sql_query('''
            SELECT * FROM transactions
            WHERE ABS(transaction_amount) > 300;
        ''', self.conn)

        # Verify correct transactions are retrieved
        expected_results = {1, 3, 4, 5}  # transaction IDs that should match
        retrieved_results = set(df['transaction_id'].tolist())
        self.assertEqual(retrieved_results, expected_results)

    def test_no_high_value_transactions(self):
        # Test with a threshold too high to find any transactions
        df = pd.read_sql_query('''
            SELECT * FROM transactions
            WHERE ABS(transaction_amount) > 800;
        ''', self.conn)

        # Expect no results
        self.assertTrue(df.empty)

    def test_null_transactions(self):
        # Test with a threshold too high to find any transactions
        df = pd.read_sql_query('''
            SELECT * FROM transactions
            WHERE ABS(transaction_amount) = null;
        ''', self.conn)

        # Expect no results
        self.assertTrue(df.empty)

    @classmethod
    def tearDownClass(cls):
        # Close the database connection
        cls.conn.close()

if __name__ == '__main__':
    unittest.main()
