import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

cursor = connection.cursor()
query = "SELECT Id FROM users ORDER BY account DESC LIMIT 1;"
cursor.execute(query)
res = cursor.fetchone()
my_list = list(res)
print(my_list[0])


query2 = "SELECT id FROM courses ORDER BY date_created LIMIT 1;"
cursor.execute(query2)
res1 = cursor.fetchone()
my_new_list = list(res1)
print(my_new_list[0])


query3 = "INSERT INTO courses (title, author, body, date_created, coursetype) VALUES ('Db_Anush', 'Anush', 'my_body', '2024-03-24 20:28:06", 2)"
cursor.execute(query3)
res2 = cursor.fetchone()
print(res2)
