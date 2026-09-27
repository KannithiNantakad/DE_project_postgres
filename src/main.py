import pandas as pd

from database import engine

query = "SELECT * FROM customers"

df = pd.read_sql(query, engine)

print(df)