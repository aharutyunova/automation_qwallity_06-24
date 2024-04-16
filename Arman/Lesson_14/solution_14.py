import logging
from datetime import datetime

import mysql.connector

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='database.log',
    filemode='w+',
    encoding='utf-8'
)


# 1. Find out the user id with maximum account
def connect_to_db():
    try:
        connection = mysql.connector.connect(
            host='pro.freedb.tech',
            user='qwallity',
            password='6YJsZQk&##7J2?e',
            database='qwallitydb'
        )
        return connection
    except mysql.connector.Error as err:
        logging.error(f"Error connecting to the database: {err}")
        return None


def get_user_with_max_account():
    # Connect to the database
    try:
        db_connection = connect_to_db()
        cursor = db_connection.cursor()

        query = "SELECT Id FROM users ORDER BY account DESC LIMIT 1"
        cursor.execute(query)

        result = cursor.fetchone()
        if result:
            user_id = result[0]
            print(f"User ID with maximum account: {user_id}")
        else:
            print("No user found")

    except mysql.connector.Error as e:
        logging.error(f"Error connecting to the database: {e}")

    finally:
        if db_connection.is_connected():
            cursor.close()
            db_connection.close()


get_user_with_max_account()


# 2. Find out the earliest created course ID

def get_earliest_created_course():
    db_connection = connect_to_db()
    if db_connection:
        cursor = db_connection.cursor()
        query = "SELECT MIN(date_created) FROM courses"
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            earliest_date = result[0]
            print(f"Earliest date in the table: {earliest_date}")
        else:
            print("No date found")

        cursor.close()
        db_connection.close()


get_earliest_created_course()


# 3. Insert new course as author insert your name

def insert_new_course(new_course):
    db_connection = connect_to_db()
    if db_connection:
        cursor = db_connection.cursor()
        query = "INSERT INTO courses (title, body, author, date_created, coursetype, price) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (new_course['title'], new_course['body'], new_course['author'], new_course['date_created'],
                  new_course['coursetype'], new_course['price'])
        cursor.execute(query, values)
        db_connection.commit()
        print("Course inserted successfully")
        cursor.close()
        db_connection.close()


current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

new_course = {
    'title': 'qa_automation_course',
    'body': 'new_course',
    'author': 'Arman',
    'date_created': current_datetime,
    'coursetype': 3,
    'price': 250_000
}

insert_new_course(new_course)
