import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

# standardize transaction type
df["transaction_type"] = df["transaction_type"].str.upper()

# convert date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# validate amount
invalid = df[df["amount_inr"] <= 0]

print("Invalid Amount Rows:", len(invalid))

# check KYC values
print("KYC Status Values:")
print(df["kyc_status"].unique())

# save
df.to_csv("data/processed/investor_transactions_clean.csv", index=False)

print("Saved")