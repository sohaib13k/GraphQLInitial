import sqlite3
import pandas as pd

conn = sqlite3.connect('')  # your path
df = pd.read_csv('') # your path
df['id'] = df.index
df = df[[ 'id', 'segment', 'country', 'product', 'units', 'sales', 'date_sold']]
df.to_sql('gqlapp_productmodel', conn, if_exists='replace', index=False)