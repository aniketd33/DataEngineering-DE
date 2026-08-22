from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]


def extract_data():
    file_path = BASE_DIR / "raw" / "employees.csv"

    print(f"Reading file: {file_path}")

    df = pd.read_csv(file_path)

    return df