-- Payment risk
SELECT l.customer_id,l.loan_id,SUM(CASE WHEN p.payment_status='Missed' THEN 1 ELSE 0 END) AS missed_payments
FROM loans l JOIN payments p ON p.loan_id=l.loan_id GROUP BY l.customer_id,l.loan_id HAVING missed_payments>=2;
-- Recent debit activity
SELECT a.customer_id,a.account_id,SUM(CASE WHEN t.transaction_type='Debit' THEN t.amount ELSE 0 END) AS recent_debits
FROM accounts a JOIN transactions t ON t.account_id=a.account_id WHERE t.transaction_date>='2026-09-13'
GROUP BY a.customer_id,a.account_id HAVING recent_debits>=15000;
-- Cross-border activity
SELECT a.customer_id,a.account_id,COUNT(*) AS international_count,COUNT(DISTINCT t.country) AS country_count
FROM accounts a JOIN transactions t ON t.account_id=a.account_id
WHERE t.country<>'New Zealand' AND t.transaction_date>='2026-09-13'
GROUP BY a.customer_id,a.account_id HAVING international_count>=5 AND country_count>=3;
