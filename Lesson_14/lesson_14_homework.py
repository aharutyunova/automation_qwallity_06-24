import pymysql
# Find out the user id with maximum account
# Find out the earliest crieted course ID
# Insert new course as author insert your name


connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')


query_max_account_id = "select id from users ORDER BY account desc LIMIT 1"
query_earliest_course_id = "select id from courses where date_created <> '0000-00-00 00:00:00' ORDER BY date_created asc limit 1"
query_insert_my_course = "INSERT INTO courses (title, body, author, date_created, coursetype, price) VALUES ('TestAnn','body','Anna_Avt', CURRENT_TIMESTAMP, (select id from coursetype limit 1), 100)"


def print_select_result(query):
    cursor = connection.cursor()
    cursor.execute(query)
    row = cursor.fetchall()
    print(row[0][0])
    cursor.close()


def insert_data(query):
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()


print_select_result(query_max_account_id)
print_select_result(query_earliest_course_id)
insert_data(query_insert_my_course)


connection.close()
