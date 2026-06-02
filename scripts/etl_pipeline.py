import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

fund_master = pd.read_csv(
    BASE_DIR / "data" / "raw" / "01_fund_master.csv"
)

print("\n========== FUND MASTER OVERVIEW ==========\n")

print("Rows, Columns:")
print(fund_master.shape)

print("\nColumns:")
print(fund_master.columns.tolist())

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nNumber of Fund Houses:")
print(fund_master["fund_house"].nunique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Grades:")
print(fund_master["risk_category"].unique())
print("\n========== AMFI CODE VALIDATION ==========")

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print(f"Fund Master Codes : {len(fund_codes)}")
print(f"NAV History Codes : {len(nav_codes)}")

if len(missing_codes) == 0:
    print("\nSUCCESS: All AMFI codes exist in NAV history.")
else:
    print("\nMissing Codes:")
    print(missing_codes)