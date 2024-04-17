# Find out the user id with maximum account

'''
import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

cursor = connection.cursor()
query = "SELECT id FROM users ORDER BY account DESC LIMIT 1;"
cursor.execute(query)
result = cursor.fetchall()
my_list = list(result)
new_list = []
for i in my_list:
    new_list.append(i[0])
print(new_list)



# another way of solving this task

import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

cursor = connection.cursor()
query = "SELECT id FROM users ORDER BY account DESC LIMIT 1;"
cursor.execute(query)
result = cursor.fetchone()
if result:
    max_user_id = int(result[0])
    print(max_user_id)
else:
    print("No user found with max account")

connection.close()


# Find out the earliest crieted course ID

import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

cursor = connection.cursor()
query = "SELECT id FROM courses ORDER BY date_created ASC LIMIT 1"
cursor.execute(query)
result = cursor.fetchone()
if result:
    earliest_course_id = int(result[0])
    print("Earliest course ID:", earliest_course_id)
else:
    print("No such course is found")


connection.close()


# another solution

import pymysql

try:
    connection = pymysql.connect(
        host='pro.freedb.tech',
        user='qwallity',
        password='6YJsZQk&##7J2?e',
        database='qwallitydb'
    )

    cursor = connection.cursor()
    query = 'SELECT id FROM courses ORDER BY date_created ASC LIMIT 1'
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        earliest_course_id = int(result[0])
        print("Earliest course ID:", earliest_course_id)
    else:
        print("No such course is found")

except pymysql.Error as e:
    print("Error:", e)

finally:
    if 'connection' in locals():
        connection.close()

'''
# Insert new course as author insert your name

import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

cursor = connection.cursor()
query = "INSERT INTO courses (title, body, Author, date_created, coursetype, price) Values ('DB_Izabella', " \
        "'course_body', 'Izabella', '2024-03-24 20:28:06', 1, 34000); "
cursor.execute(query)
connection.commit()
print("Course inserted successfully!")
connection.close()

'''

import pymysql

try:
    connection = pymysql.connect(
        host='pro.freedb.tech',
        user='qwallity',
        password='6YJsZQk&##7J2?e',
        database='qwallitydb'
    )

    cursor = connection.cursor()
    query = "INSERT INTO courses (title, body, Author, date_created, coursetype, price) VALUES ('DB_Izabella', 'Course_body', 'Izabella', '2024-03-24 20:28:06', 1, 34000)"
    cursor.execute(query)
    connection.commit()

    print("Course inserted successfully!")

except pymysql.Error as e:
    connection.rollback()
    print("Error:", e)

finally:
    if 'connection' in locals():
        connection.close()
'''