import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

db_path = BASE_DIR / "data" / "db" / "mutual_fund.db"

conn = sqlite3.connect(db_path)

raw_path = BASE_DIR / "data" / "raw"

csv_files = list(raw_path.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files\n")

for file in csv_files:

    table_name = file.stem

    try:
        df = pd.read_csv(file)

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"Loaded: {table_name}")
        print(f"Rows: {len(df)}")

    except Exception as e:
        print(f"Error loading {table_name}")
        print(e)

print("\n==========================")
print("DATABASE LOADING COMPLETE")
print("==========================")

tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table';",
    conn
)

print("\nTables Created:")
print(tables)

conn.close()