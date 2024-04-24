
# Find out the user id with maximum account
# Find out the earliest crieted course ID
# Insert new course as author insert your name
import pymysql
import mysql.connector


connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

#connection.close()

cursor = connection.cursor()

query_max_acc_user = ("SELECT Id FROM users order by account desc limit 1")
query_earliest_course = ("SELECT Id FROM courses ORDER BY date_created asc limit 1")
query_courses_count = ("SELECT * FROM courses")
query_insert = ("INSERT INTO courses(title, body, author, date_created, coursetype, price) values('motivation_course', 'body', 'Raya', '2024-04-21 21:52:51', 1, 500)")

cursor.execute(query_max_acc_user)
print('The user id with maximum account is: ',cursor.fetchall()[0][0])

cursor.execute(query_earliest_course)
print('The earliest created course ID is: ',cursor.fetchall()[0][0])

cursor.execute(query_courses_count)
courses_count = cursor.rowcount

cursor.execute(query_insert)
connection.commit()

cursor.execute(query_courses_count)
courses_count_increated = cursor.rowcount

if courses_count_increated > courses_count:
    print('The insert operation is successfull')
else:
    print('The insert operation is not successfull')

cursor.close()


# Anna - Good solution, please also don't forget to close connetion - connection.close()