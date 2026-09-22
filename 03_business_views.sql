
CREATE VIEW vw_loan_risk_exposure AS
SELECT l.loan_id,l.customer_id,c.region,c.customer_segment,l.loan_type,l.outstanding_balance,l.interest_rate,l.monthly_repayment,l.loan_status
FROM loans l JOIN customers c ON c.customer_id=l.customer_id;
CREATE VIEW vw_payment_risk AS
SELECT l.loan_id,l.customer_id,
SUM(CASE WHEN p.payment_status='Missed' THEN 1 ELSE 0 END) missed_payments,
SUM(CASE WHEN p.payment_status='Partial' THEN 1 ELSE 0 END) partial_payments,
MAX(p.days_overdue) max_days_overdue
FROM loans l LEFT JOIN payments p ON p.loan_id=l.loan_id GROUP BY l.loan_id,l.customer_id;
CREATE VIEW vw_transaction_summary AS
SELECT a.account_id,a.customer_id,COUNT(t.transaction_id) transaction_count,
SUM(CASE WHEN t.transaction_type='Debit' THEN t.amount ELSE 0 END) debit_value,
SUM(CASE WHEN t.transaction_type='Credit' THEN t.amount ELSE 0 END) credit_value,
SUM(CASE WHEN t.country<>'New Zealand' THEN 1 ELSE 0 END) international_transactions
FROM accounts a LEFT JOIN transactions t ON t.account_id=a.account_id GROUP BY a.account_id,a.customer_id;
