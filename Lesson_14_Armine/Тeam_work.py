
import mysql.connector



con = mysql.connector.connect(host='pro.freedb.tech',
                              user='qwallity',
                              password='6YJsZQk&##7J2?e',
                              database='qwallitydb')

cursor = con.cursor()

cursor.execute("select Id from users where email not like '%@%'")

result = cursor.fetchall()

for i in result:
    print(i[0])