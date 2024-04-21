# Find out the user id with maximum account
# Find out the earliest crieted course ID
# Insert new course as author insert your name

import pymysql

class DB:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        connection = pymysql.connect(host='pro.freedb.tech',
                                     user='qwallity',
                                     password='6YJsZQk&##7J2?e',
                                     database='qwallitydb')
        return connection
    
def find_earliest_created_course_id(self):
    cursor = self.connection.cursor()
    query = "SELECT id FROM courses ORDER BY created_on ASC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    if result:
        course_id = result[0]
        print("Earliest created course ID:", course_id)
        return course_id
    else:
        print("No courses found")

    def find_earliest_created_course_id(self):
        cursor = self.connection.cursor()
        query = "SELECT id FROM courses ORDER BY created_on ASC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            course_id = result[0]
            print("Earliest created course ID:", course_id)
            return course_id
        else:
            print("No courses found")

    def insert_new_course(self, author_name, course_title):
        cursor = self.connection.cursor()
        query = "INSERT INTO courses (author, title) VALUES (%s, %s)"
        try:
            cursor.execute(query, (author_name, course_title))
            self.connection.commit()
            print("New course inserted successfully.")
        except pymysql.Error as e:
            print(f"Error inserting new course: {e}")
            self.connection.rollback()

    def close_connection(self):
        self.connection.close()

# Example usage:
db = DB()
max_user_id = db.find_user_with_max_account()
earliest_course_id = db.find_earliest_created_course_id()
if max_user_id:
    db.insert_new_course("Lianna", "Auto_QA")
db.close_connection()
