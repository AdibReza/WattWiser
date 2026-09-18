import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/synthetic_shelly_data.csv")

df = pd.read_csv(DATA_PATH)

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)