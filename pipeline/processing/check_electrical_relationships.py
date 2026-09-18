import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/synthetic_shelly_data.csv")

df = pd.read_csv(DATA_PATH)

# Calculate expected electrical relationships
df["calculated_apparent_power_VA"] = (
    df["voltage_V"] * df["current_A"]
)

df["calculated_power_factor"] = (
    df["active_power_W"] / df["apparent_power_VA"]
)

# Differences
df["apparent_power_error"] = (
    df["apparent_power_VA"]
    - df["calculated_apparent_power_VA"]
).abs()

df["power_factor_error"] = (
    df["power_factor"]
    - df["calculated_power_factor"]
).abs()

print("========== ELECTRICAL RELATIONSHIP CHECK ==========")

print("\nApparent power:")
print(
    f"Maximum error: "
    f"{df['apparent_power_error'].max():.4f} VA"
)

print(
    f"Mean error: "
    f"{df['apparent_power_error'].mean():.4f} VA"
)

print("\nPower factor:")
print(
    f"Maximum error: "
    f"{df['power_factor_error'].max():.4f}"
)

print(
    f"Mean error: "
    f"{df['power_factor_error'].mean():.4f}"
)

print("\nSample:")
print(
    df[
        [
            "voltage_V",
            "current_A",
            "active_power_W",
            "apparent_power_VA",
            "power_factor",
            "calculated_apparent_power_VA",
            "calculated_power_factor",
        ]
    ].head(10)
)