import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/synthetic_shelly_data.csv")

df = pd.read_csv(DATA_PATH)

print("========== BASIC INFORMATION ==========")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(f"Duplicates: {df.duplicated().sum():,}")

print("\n========== TIMESTAMP CHECK ==========")

df["timestamp"] = pd.to_datetime(df["timestamp"])

time_diff = df["timestamp"].diff().dropna()

print(f"First timestamp: {df['timestamp'].min()}")
print(f"Last timestamp:  {df['timestamp'].max()}")

print("\nTime interval distribution:")
print(time_diff.value_counts().head(10))

print("\n========== NUMERICAL RANGE CHECK ==========")

numeric_columns = [
    "voltage_V",
    "current_A",
    "active_power_W",
    "apparent_power_VA",
    "power_factor",
    "frequency_Hz",
    "cumulative_energy_Wh",
]

for column in numeric_columns:
    print(
        f"{column:25} "
        f"min={df[column].min():10.2f} "
        f"max={df[column].max():10.2f} "
        f"mean={df[column].mean():10.2f}"
    )

print("\n========== NEGATIVE VALUES ==========")

for column in numeric_columns:
    negative_count = (df[column] < 0).sum()
    print(f"{column:25}: {negative_count:,}")

print("\n========== APPLIANCE STATES ==========")

state_columns = [
    "kettle_on",
    "fridge_on",
    "microwave_on",
    "washing_machine_on",
]

for column in state_columns:
    print(f"\n{column}:")
    print(df[column].value_counts())

print("\n========== VALIDATION COMPLETE ==========")