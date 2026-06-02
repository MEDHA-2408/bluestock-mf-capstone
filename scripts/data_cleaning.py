import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

raw_path = BASE_DIR / "data" / "raw"
processed_path = BASE_DIR / "data" / "processed"

processed_path.mkdir(exist_ok=True)

csv_files = list(raw_path.glob("*.csv"))

print(f"Found {len(csv_files)} files")

for file in csv_files:

    print(f"\nCleaning: {file.name}")

    df = pd.read_csv(file)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    for col in df.columns:

        if df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown")

        else:
            df[col] = df[col].fillna(df[col].median())

    save_path = processed_path / file.name

    df.to_csv(save_path, index=False)

    print(f"Saved: {file.name}")

print("\nData Cleaning Complete")