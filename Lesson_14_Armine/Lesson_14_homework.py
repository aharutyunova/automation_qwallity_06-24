
# 1 Find out the user id with maximum account

import mysql.connector


connection = mysql.connector.connect(host='pro.freedb.tech',
                                             user='qwallity',
                                             password='6YJsZQk&##7J2?e',
                                             database='qwallitydb')
                    
cur = connection.cursor()
cur.execute("select MAX(account) FROM users")
result=cur.fetchall()
print(result)
cur.execute("select id from users where account=2147483647")
result1=cur.fetchall()
print(result1[0][0])



# 2 Find out the earliest crieted course ID

cur2 = connection.cursor()
cur2.execute("select id from courses order by date_created ASC")
result3 = cur2.fetchall() #or fetchone()
print(result3[0][0])



# 3 Insert new course as author insert your name

cur3 = connection.cursor()
cur3.execute("INSERT INTO courses (title, body, author, coursetype, price) Values('Fundamental', 'Python', 'Armine', '2', '234000')")
connection.commit()

connection.close()

#Anna jan, please also check Lesson_13, thank you, in advance))