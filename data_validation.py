import sqlite3
from config import DB_PATH
TABLES={"customers":"customer_id","accounts":"account_id","loans":"loan_id","payments":"payment_id","transactions":"transaction_id"}
def validate_database():
    c=sqlite3.connect(DB_PATH); out=[]
    for t,k in TABLES.items():
        total=c.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        nulls=c.execute(f"SELECT COUNT(*) FROM {t} WHERE {k} IS NULL").fetchone()[0]
        dup=c.execute(f"SELECT COUNT(*) FROM (SELECT {k} FROM {t} GROUP BY {k} HAVING COUNT(*)>1)").fetchone()[0]
        out.append((t,total,nulls,dup))
    c.close(); return out
if __name__=="__main__":
    [print(x) for x in validate_database()]
