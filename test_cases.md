# Test Cases
| ID | Scenario | Expected result |
|---|---|---|
| TC001 | Load customers | Records load |
| TC002 | Foreign-key mismatch | Validation identifies issue |
| TC003 | Duplicate key | Validation identifies duplicate |
| TC004 | Missing key | Validation identifies null |
| TC005 | 2 missed payments | Payment alert |
| TC006 | 3 missed payments | High-severity payment alert |
| TC007 | High recent debit activity | Activity alert |
| TC008 | 5 international txns / 3 countries | Cross-border alert |
| TC009 | Re-run pipeline | Duplicate alert prevented |
| TC010 | Create escalation | Escalation links to alert |
| TC011 | Resolution time | Hours recorded |
| TC012 | +0.50% parameter | Scenario rate changes by 0.50 pp |
| TC013 | Region filter | Dashboard responds |
