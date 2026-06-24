--------------------------------------------------
-- Query 1 : Top 5 Funds by AUM
--------------------------------------------------

SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;


--------------------------------------------------
-- Query 2 : Average NAV per Month
--------------------------------------------------

SELECT 
strftime('%m', date) AS month,
AVG(nav) AS average_nav

FROM fact_nav

GROUP BY month;


--------------------------------------------------
-- Query 3 : SIP Year over Year Growth
--------------------------------------------------

SELECT 
year,
sip_amount,
yoy_growth_pct

FROM monthly_sip_inflows;


--------------------------------------------------
-- Query 4 : Transactions by State
--------------------------------------------------

SELECT 
state,
COUNT(*) AS total_transactions

FROM fact_transactions

GROUP BY state;


--------------------------------------------------
-- Query 5 : Funds with Expense Ratio < 1%
--------------------------------------------------

SELECT *

FROM fact_performance

WHERE expense_ratio < 1;


--------------------------------------------------
-- Query 6 : Highest Return Funds
--------------------------------------------------

SELECT 
scheme_name,
return_1yr

FROM fact_performance

ORDER BY return_1yr DESC;


--------------------------------------------------
-- Query 7 : Number of Funds by Category
--------------------------------------------------

SELECT
category,
COUNT(*) AS total_funds

FROM dim_fund

GROUP BY category;


--------------------------------------------------
-- Query 8 : Average AUM Across Funds
--------------------------------------------------

SELECT
AVG(aum_crore) AS average_aum

FROM fact_aum;


--------------------------------------------------
-- Query 9 : Redemption Transaction Count
--------------------------------------------------

SELECT
COUNT(*) AS redemption_count

FROM fact_transactions

WHERE transaction_type = 'REDEMPTION';


--------------------------------------------------
-- Query 10 : Highest NAV Recorded
--------------------------------------------------

SELECT
MAX(nav) AS highest_nav

FROM fact_nav;