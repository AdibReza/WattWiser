import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/raw/synthetic_shelly_data.csv")
OUTPUT_PATH = Path("data/processed/synthetic_shelly_processed.csv")

# Load raw data
df = pd.read_csv(INPUT_PATH)

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Sort chronologically
df = df.sort_values("timestamp").reset_index(drop=True)

# Calculate useful electrical features
df["calculated_apparent_power_VA"] = (
    df["voltage_V"] * df["current_A"]
)

df["calculated_power_factor"] = (
    df["active_power_W"] / df["apparent_power_VA"]
)

# Power change between consecutive measurements
df["power_change_W"] = df["active_power_W"].diff()

# Current change
df["current_change_A"] = df["current_A"].diff()

# Remove the first row because diff() produces NaN there
df = df.dropna().reset_index(drop=True)

# Create output directory if necessary
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# Save processed data
df.to_csv(OUTPUT_PATH, index=False)

print("========== PROCESSING COMPLETE ==========")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Output: {OUTPUT_PATH}")

print("\nProcessed columns:")
for column in df.columns:
    print(f"- {column}")