
# 1 Find out the user id with maximum account

import mysql.connector


connection = mysql.connector.connect(host='pro.freedb.tech',
                                             user='qwallity',
                                             password='6YJsZQk&##7J2?e',
                                             database='qwallitydb')
                    
cur = connection.cursor()
cur.execute("select MAX(account) FROM users")
result=cur.fetchall()
cur.execute("select id from users where account=2147483647")
result1=cur.fetchall()
# print(result1[0][0])

# Anna - you hardcoded amount in the query )) you could write query like this select * from users order by account desc limit 1

# 2 Find out the earliest crieted course ID

cur2 = connection.cursor()
cur2.execute("select id from courses order by date_created ASC")
result3 = cur2.fetchall() #or fetchone()
print(result3[0][0])

# Anna - you could also use limit 1 in the query to get only one row

# 3 Insert new course as author insert your name

cur3 = connection.cursor()
cur3.execute("INSERT INTO courses (title, body, author, coursetype, price) Values('Fundamental', 'Python', 'Armine', '2', '234000')")
connection.commit()

connection.close()


# Anna - correct

#Anna jan, please also check Lesson_13, thank you, in advance)) - Checked :)