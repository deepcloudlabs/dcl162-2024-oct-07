from mysql import connector

mysql_connection = connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Secret_123',
    database='world'
)
cursor = mysql_connection.cursor()
cursor.execute("show tables")
for table_name, *rest in cursor:
    print(table_name)