import sqlite3,random
from datetime import datetime,timedelta
from config import DB_PATH,DETECTION_DATE
def create_escalations():
    random.seed(42); c=sqlite3.connect(DB_PATH); alerts=c.execute("SELECT alert_id,severity FROM risk_alerts").fetchall()
    nid=c.execute("SELECT COALESCE(MAX(escalation_id),0)+1 FROM escalations").fetchone()[0]; rows=[]; base=datetime.fromisoformat(DETECTION_DATE+"T08:00:00")
    for aid,sev in alerts:
        created=base+timedelta(minutes=random.randint(0,300)); started=created+timedelta(minutes=random.randint(5,60))
        hours=random.uniform(2,36) if sev=="Medium" else random.uniform(4,48); complete=started+timedelta(hours=hours)
        status=random.choice(["Open","In Progress","Resolved"])
        rows.append((nid,aid,created.isoformat(timespec="minutes"),started.isoformat(timespec="minutes"),complete.isoformat(timespec="minutes"),round(hours,2),status,"Validated and routed for review" if status!="Open" else None)); nid+=1
    c.executemany("INSERT OR IGNORE INTO escalations VALUES (?,?,?,?,?,?,?,?)",rows); c.commit(); c.close(); return len(rows)
if __name__=="__main__": print(create_escalations())
