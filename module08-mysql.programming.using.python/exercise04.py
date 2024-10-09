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
select iban,balance,status
from accounts
where status = 'ACTIVE'
limit 0,20
""")
for iban, balance, status in cursor:
    print(iban, balance, status)
