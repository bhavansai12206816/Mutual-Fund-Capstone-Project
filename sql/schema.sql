CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    scheme_name TEXT,

    fund_house TEXT,

    category TEXT,

    sub_category TEXT

);

CREATE TABLE dim_date (

    date_id INTEGER PRIMARY KEY,

    full_date DATE

);

CREATE TABLE fact_nav (

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    date_id INTEGER,

    nav REAL,

    FOREIGN KEY(amfi_code)
    REFERENCES dim_fund(amfi_code)

);

CREATE TABLE fact_transactions (

    txn_id INTEGER PRIMARY KEY AUTOINCREMENT,

    investor_id INTEGER,

    amfi_code INTEGER,

    amount_inr REAL,

    transaction_type TEXT

);

CREATE TABLE fact_performance (

    perf_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    expense_ratio REAL,

    return_1yr REAL

);

CREATE TABLE fact_aum (

    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER,

    aum_crore REAL

);