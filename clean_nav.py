import pandas as pd

# load csv
df = pd.read_csv("data/raw/02_nav_history.csv")

print("Original Shape:", df.shape)

# convert date
df["date"] = pd.to_datetime(df["date"])

# sort
df = df.sort_values(["amfi_code", "date"])

# fill missing NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# remove duplicates
df = df.drop_duplicates()

# check invalid nav
invalid = df[df["nav"] <= 0]

print("Invalid NAV rows:", len(invalid))

# save
df.to_csv("data/processed/nav_history_clean.csv", index=False)

print("Cleaned file saved")