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
delete from accounts
where status = 'CLOSED' or status = 'BLOCKED'
""")
mysql_connection.commit()
print(f"{cursor.rowcount} rows removed!")

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

mysql> select * from accounts;
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