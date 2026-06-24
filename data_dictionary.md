# DATA DICTIONARY

## 1. fund_master

| Column | Type | Meaning |
|----------|------|---------|
| amfi_code | Integer | Unique fund identifier |
| scheme_name | String | Mutual fund name |
| fund_house | String | AMC company |
| category | String | Equity/Debt/Hybrid |
| sub_category | String | Fund subtype |

---

## 2. nav_history

| Column | Type | Meaning |
|----------|------|---------|
| amfi_code | Integer | Fund identifier |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

## 3. investor_transactions

| Column | Type | Meaning |
|----------|------|---------|
| investor_id | Integer | Investor unique id |
| amount_inr | Float | Investment amount |
| transaction_type | String | SIP/Lumpsum/Redemption |
| transaction_date | Date | Transaction date |
| kyc_status | String | Verified/Pending |

---

## 4. scheme_performance

| Column | Type | Meaning |
|----------|------|---------|
| return_1yr | Float | One year return |
| return_3yr | Float | Three year return |
| expense_ratio_pct | Float | Fund management fee |