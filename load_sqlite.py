from sqlalchemy import create_engine
import pandas as pd

# create database
engine = create_engine("sqlite:///bluestock_mf.db")

# load cleaned csv files

fund = pd.read_csv("data/raw/01_fund_master.csv")

nav = pd.read_csv("data/processed/nav_history_clean.csv")

transactions = pd.read_csv("data/processed/investor_transactions_clean.csv")

performance = pd.read_csv("data/processed/scheme_performance_clean.csv")


# save into sqlite

fund.to_sql("dim_fund", engine, if_exists="replace", index=False)

nav.to_sql("fact_nav", engine, if_exists="replace", index=False)

transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)

performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Fund rows:", len(fund))
print("NAV rows:", len(nav))
print("Transaction rows:", len(transactions))
print("Performance rows:", len(performance))
print("Database Loaded Successfully")