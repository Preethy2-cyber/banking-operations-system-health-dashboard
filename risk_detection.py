import sqlite3
from config import DB_PATH,DETECTION_DATE
def calculate_alerts():
    c=sqlite3.connect(DB_PATH); alerts=[]; nid=c.execute("SELECT COALESCE(MAX(alert_id),0)+1 FROM risk_alerts").fetchone()[0]
    for customer,loan,missed in c.execute("""SELECT l.customer_id,l.loan_id,SUM(CASE WHEN p.payment_status='Missed' THEN 1 ELSE 0 END)
        FROM loans l JOIN payments p ON p.loan_id=l.loan_id GROUP BY l.customer_id,l.loan_id HAVING SUM(CASE WHEN p.payment_status='Missed' THEN 1 ELSE 0 END)>=2"""):
        a=c.execute("SELECT account_id FROM accounts WHERE customer_id=? LIMIT 1",(customer,)).fetchone()
        score=40 if missed>=3 else 25
        alerts.append((nid,customer,a[0] if a else None,"Consecutive Missed Payments",score,"High" if score>=40 else "Medium",DETECTION_DATE,"Open","Credit Operations")); nid+=1
    for customer,account,n,countries in c.execute("""SELECT a.customer_id,a.account_id,COUNT(*),COUNT(DISTINCT t.country)
        FROM accounts a JOIN transactions t ON t.account_id=a.account_id WHERE t.country<>'New Zealand' AND t.transaction_date>=date(?,'-7 day')
        GROUP BY a.customer_id,a.account_id HAVING COUNT(*)>=5 AND COUNT(DISTINCT t.country)>=3""",(DETECTION_DATE,)):
        score=45 if countries>=4 else 35
        alerts.append((nid,customer,account,"Rapid Cross-Border Activity",score,"High" if score>=40 else "Medium",DETECTION_DATE,"Open","Financial Crime Operations")); nid+=1
    for customer,account,debits in c.execute("""SELECT a.customer_id,a.account_id,SUM(CASE WHEN t.transaction_type='Debit' THEN t.amount ELSE 0 END)
        FROM accounts a JOIN transactions t ON t.account_id=a.account_id WHERE t.transaction_date>=date(?,'-7 day')
        GROUP BY a.customer_id,a.account_id HAVING SUM(CASE WHEN t.transaction_type='Debit' THEN t.amount ELSE 0 END)>=15000""",(DETECTION_DATE,)):
        alerts.append((nid,customer,account,"Overdraft Activity Spike",35,"Medium",DETECTION_DATE,"Open","Customer Operations")); nid+=1
    unique={(x[1],x[3]):x for x in alerts}
    c.executemany("INSERT OR IGNORE INTO risk_alerts VALUES (?,?,?,?,?,?,?,?,?)",list(unique.values()))
    c.commit(); c.close(); return list(unique.values())
if __name__=="__main__": print(len(calculate_alerts()))
