import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

# Find out the user id with maximum account
cursor = connection.cursor()
query = "SELECT id FROM users ORDER BY account DESC "
cursor.execute(query)
resultat = cursor.fetchone()
cursor.close()
maxvalue = resultat[0]
print("Id of the user which has the max account number is \n", maxvalue)

# Find out the earliest crieted course ID
cursor1 = connection.cursor()
query1 = "SELECT id FROM courses  where date_created > '0000-00-00 00:00:00' ORDER BY date_created "
cursor1.execute(query1)
resultat1 = cursor1.fetchone()
cursor1.close()
earliest_curs = resultat1[0]
print("Earliest crieted course ID is \n", earliest_curs)

# Insert new course as author insert your name
cursor2 = connection.cursor()
query2 = "INSERT into courses (title, body, author,date_created, coursetype, price) VALUES ('Hamest_QA', 'body', 'Hamest', DATE_ADD(NOW(), INTERVAL 4 HOUR), '2', '1000')"
cursor2.execute(query2)
connection.commit()

my_check = "SELECT * from courses ORDER BY id DESC limit 1"
cursor2.execute(my_check)
resultat2 = cursor2.fetchone()
cursor2.close()
#my_added_id = resultat2[0]
print("Instered the cours with \n", resultat2, "\nData.")

# Anna - good job!!!