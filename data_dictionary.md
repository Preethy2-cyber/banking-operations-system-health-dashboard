# Data Dictionary
| Table | Key fields | Purpose |
|---|---|---|
| customers | customer_id | Customer master |
| accounts | account_id, customer_id | Account data |
| loans | loan_id, customer_id | Lending exposure |
| payments | payment_id, loan_id | Payment performance |
| transactions | transaction_id, account_id | Transaction activity |
| risk_alerts | alert_id, customer_id | Simulated risk events |
| escalations | escalation_id, alert_id | Operational workflow |
