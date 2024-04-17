
# Find out the user id with maximum account
# Find out the earliest crieted course ID
# Insert new course as author insert your name

# Find out the user id with maximum account.

import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

cursor = connection.cursor()
query = ("select * from account order by account_balance desc ")

cursor.execute(query)
result = cursor.fetchone()
print("The user id with maximum account:", result[0])
cursor.close()
connection.close()

# Find out the earliest crieted course ID

import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

cursor = connection.cursor()
query = ("select * from courses order by date_created asc ")

cursor.execute(query)
result = cursor.fetchone()
print(" The earliest crieted course ID:", result[0])
cursor.close()
connection.close()

# Insert new course as author insert your name.

import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')


cursor = connection.cursor()
query = """
    INSERT INTO courses (title, body, author, date_created, coursetype, price)
    VALUES ('New course','Test', 'Liana', DATE_ADD(NOW(), INTERVAL 4 HOUR), 2, 10000)
"""

cursor.execute(query)
connection.commit()
cursor.close()
connection.close()


# Anna - very good job!!!