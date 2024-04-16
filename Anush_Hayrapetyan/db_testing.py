import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

cursor = connection.cursor()

cursor.execute("select * from users")
result = cursor.fetchone
print(result)

