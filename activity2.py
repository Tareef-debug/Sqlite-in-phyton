import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfullly')

import pandas as pd
tables = pd.read_sql(""""Select * FROM sqlite_master WHERE type='table;""",conn)

tables