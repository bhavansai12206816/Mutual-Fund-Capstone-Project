import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# numeric conversion
df["expense_ratio_pct"] = pd.to_numeric(df["expense_ratio_pct"])

# invalid expense ratio
invalid = df[
   (df["expense_ratio_pct"] < 0.1) |
   (df["expense_ratio_pct"] > 2.5)
]

print("Invalid Expense Ratio:", len(invalid))

# save
df.to_csv("data/processed/scheme_performance_clean.csv", index=False)

print("Saved")