from mysql import connector

mysql_connection = connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Secret_123',
    database='banking'
)

cursor = mysql_connection.cursor()
cursor.execute("""
update accounts 
set balance = balance - 500 
where status = 'ACTIVE'
""")
mysql_connection.commit()
print(f"{cursor.rowcount} rows updated!")
"""
mysql> select iban,balance,status
    -> from accounts
    -> where status = 'ACTIVE'
    -> limit 0,20;
+------+---------+--------+
| iban | balance | status |
+------+---------+--------+
| tr1  |   10000 | ACTIVE |
| tr2  |   20000 | ACTIVE |
| tr5  |   50000 | ACTIVE |
| tr7  |   70000 | ACTIVE |
+------+---------+--------+
4 rows in set (0.00 sec)

mysql> select iban,balance,status from accounts where status='ACTIVE';
+------+---------+--------+
| iban | balance | status |
+------+---------+--------+
| tr1  |    9500 | ACTIVE |
| tr2  |   19500 | ACTIVE |
| tr5  |   49500 | ACTIVE |
| tr7  |   69500 | ACTIVE |
+------+---------+--------+
4 rows in set (0.00 sec)
"""