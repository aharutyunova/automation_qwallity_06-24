import pymysql


connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')


cursor = connection.cursor()
query = "select * from users"

cursor.execute(query)
res = cursor.fetchone()
res = cursor.fetchone()
res = cursor.fetchone()
rowcount = cursor.rowcount
print(rowcount)
print(res)
connection.close()


