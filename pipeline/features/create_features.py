import pandas as pd
from pathlib import Path

INPUT_PATH = Path("data/processed/synthetic_shelly_processed.csv")
OUTPUT_PATH = Path("data/processed/synthetic_shelly_features.csv")

df = pd.read_csv(INPUT_PATH)

df["timestamp"] = pd.to_datetime(df["timestamp"])

# --------------------------------------------------
# 1. Time-based features
# --------------------------------------------------

df["hour"] = df["timestamp"].dt.hour
df["minute"] = df["timestamp"].dt.minute

# Cyclic representation of time
df["hour_sin"] = (
    __import__("numpy").sin(2 * __import__("numpy").pi * df["hour"] / 24)
)

df["hour_cos"] = (
    __import__("numpy").cos(2 * __import__("numpy").pi * df["hour"] / 24)
)

# --------------------------------------------------
# 2. Electrical features
# --------------------------------------------------

# Difference between apparent and active power
df["reactive_power_estimate_VAR"] = (
    (df["apparent_power_VA"] ** 2 - df["active_power_W"] ** 2)
    .clip(lower=0)
    .pow(0.5)
)

# Power/current relationship
df["power_per_amp"] = (
    df["active_power_W"] / df["current_A"]
)

# Apparent power/current relationship
df["apparent_power_per_amp"] = (
    df["apparent_power_VA"] / df["current_A"]
)

# --------------------------------------------------
# 3. Change-based features
# --------------------------------------------------

df["power_change_W"] = df["active_power_W"].diff()

df["current_change_A"] = df["current_A"].diff()

df["voltage_change_V"] = df["voltage_V"].diff()

df["power_factor_change"] = df["power_factor"].diff()

# --------------------------------------------------
# 4. Rolling features
# --------------------------------------------------

# 1 minute = 12 samples because sampling is every 5 seconds
df["power_1min_mean"] = (
    df["active_power_W"]
    .rolling(window=12)
    .mean()
)

df["power_1min_std"] = (
    df["active_power_W"]
    .rolling(window=12)
    .std()
)

df["power_1min_max"] = (
    df["active_power_W"]
    .rolling(window=12)
    .max()
)

df["power_1min_min"] = (
    df["active_power_W"]
    .rolling(window=12)
    .min()
)

# --------------------------------------------------
# Remove rows created by rolling/difference operations
# --------------------------------------------------

df = df.dropna().reset_index(drop=True)

# --------------------------------------------------
# Save
# --------------------------------------------------

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print("========== FEATURE ENGINEERING COMPLETE ==========")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print(f"Output: {OUTPUT_PATH}")

print("\nFeatures created:")

features = [
    "hour",
    "minute",
    "hour_sin",
    "hour_cos",
    "reactive_power_estimate_VAR",
    "power_per_amp",
    "apparent_power_per_amp",
    "power_change_W",
    "current_change_A",
    "voltage_change_V",
    "power_factor_change",
    "power_1min_mean",
    "power_1min_std",
    "power_1min_max",
    "power_1min_min",
]

for feature in features:
    print(f"- {feature}")