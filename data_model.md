# Power BI Data Model
Dimensions: DimCustomer, DimAccount, DimLoan, DimDate, DimRiskType.
Facts: FactTransaction, FactPayment, FactLoan, FactAlert, FactEscalation, FactValidation.

Relationships:
- DimCustomer[customer_id] 1:* DimAccount[customer_id]
- DimCustomer[customer_id] 1:* FactLoan[customer_id]
- DimLoan[loan_id] 1:* FactPayment[loan_id]
- DimAccount[account_id] 1:* FactTransaction[account_id]
- DimCustomer[customer_id] 1:* FactAlert[customer_id]
- FactAlert[alert_id] 1:* FactEscalation[alert_id]
- DimDate[date] 1:* transaction/payment/alert dates
