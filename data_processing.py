import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")
OUTPUT_PATH = DATA_DIR / "formatted_sales_data.csv"

# Load all three input CSVs and combine them
input_files = [
    DATA_DIR / "daily_sales_data_0.csv",
    DATA_DIR / "daily_sales_data_1.csv",
    DATA_DIR / "daily_sales_data_2.csv",
]
df = pd.concat([pd.read_csv(f) for f in input_files], ignore_index=True)

# 1. Keep only Pink Morsel rows
df = df[df["product"] == "pink morsel"]

# 2. Combine quantity and price into a single "sales" field
# Price comes in as a string like "$3.00", so strip the $ before casting
df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
df["sales"] = df["price"] * df["quantity"]

# 3 & 4. Keep only sales, date, and region
df = df[["sales", "date", "region"]]

# Write the output
df.to_csv(OUTPUT_PATH, index=False)

print(f"Wrote {len(df)} rows to {OUTPUT_PATH}")
