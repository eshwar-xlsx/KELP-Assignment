import sqlite3
import pandas as pd
file_CIN = pd.read_excel("Credit Rating Details.xlsx")
file = pd.read_excel("Screener CIN Mapping (1).xlsx")

conn = sqlite3.connect(':memory:')

file_CIN.to_sql('file_CIN', conn, index=False)
file.to_sql('file', conn, index=False)

sql_query = """
SELECT 
    fc.CIN, f.*
FROM 
    "file_CIN" AS fc
JOIN 
    "file" AS f
ON 
    fc.CIN = f.CIN;
"""
result_df = pd.read_sql_query(sql_query, conn)

# Display the resulting DataFrame
print(result_df)
