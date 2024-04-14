import sqlite3
from collections import namedtuple 
import pandas as pd

conn = sqlite3.connect('./database/sample.db') 


# transactions
query = '''select * from transactions limit 3'''
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Show the Dataframe
print(df)