from mysql import connector

mysql_connection = connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Secret_123',
    database='banking'
)

cursor = mysql_connection.cursor()
accounts = [
    ("tr1", 10_000, 'ACTIVE'),
    ("tr2", 20_000, 'ACTIVE'),
    ("tr3", 30_000, 'CLOSED'),
    ("tr4", 40_000, 'BLOCKED'),
    ("tr5", 50_000, 'ACTIVE'),
    ("tr6", 60_000, 'CLOSED'),
    ("tr7", 70_000, 'ACTIVE'),
    ("tr8", 90_000, 'BLOCKED')
]
for iban, balance, status in accounts:
    cursor.execute(f"insert into accounts values ('{iban}',{balance},'{status}')")
mysql_connection.commit()
"""
mysql> select * from accounts;
+------+---------+---------+
| iban | balance | status  |
+------+---------+---------+
| tr1  |   10000 | ACTIVE  |
| tr2  |   20000 | ACTIVE  |
| tr3  |   30000 | CLOSED  |
| tr4  |   40000 | BLOCKED |
| tr5  |   50000 | ACTIVE  |
| tr6  |   60000 | CLOSED  |
| tr7  |   70000 | ACTIVE  |
| tr8  |   90000 | BLOCKED |
+------+---------+---------+
8 rows in set (0.00 sec)
"""
