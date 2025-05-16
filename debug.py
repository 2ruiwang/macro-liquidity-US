# debug.py

from fetch_data import fetch_all_fred
import pandas as pd

print("🔍 Starting FRED Data Debugging...\n")

try:
    fred_data = fetch_all_fred()

    # Check top-level keys
    print("🧩 Fetched series IDs:")
    for key in fred_data.keys():
        print(f"   • {key}")

    print("\n📊 Series Diagnostics:")

    # Loop through each series and inspect structure + values
    for key, df in fred_data.items():
        print(f"\n--- {key} ---")
        print(f"Type: {type(df)}")

        if not isinstance(df, pd.DataFrame):
            print(f"⚠️  {key} is not a DataFrame.")
            continue

        if df.empty:
            print(f"⚠️  {key} is EMPTY.")
            continue

        if "value" not in df.columns:
            print(f"⚠️  {key} has no 'value' column.")
            print(f"Columns present: {df.columns.tolist()}")
            continue

        print(f"✅ Shape: {df.shape}")
        print("Last 5 rows:")
        print(df.tail())

        latest_val = df["value"].dropna().astype(float).iloc[-1]
        print(f"Latest value: {latest_val:.4f}")

except Exception as e:
    print(f"\n🚨 Error during FRED fetch or processing:\n{e}")
