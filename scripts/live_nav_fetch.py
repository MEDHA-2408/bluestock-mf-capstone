import pandas as pd
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

funds = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

for fund_name, scheme_code in funds.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        save_path = (
            BASE_DIR
            / "data"
            / "raw"
            / f"{fund_name}_nav.csv"
        )

        nav_df.to_csv(save_path, index=False)

        print(f"Downloaded: {fund_name}")

    else:
        print(f"Failed: {fund_name}")