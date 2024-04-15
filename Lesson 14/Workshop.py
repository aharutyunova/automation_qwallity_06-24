'''
import pymysql

from credentials import DB_HOST, DB_USER, DB_DATABASE, DB_PASSWORD


class DB:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def create_connection(self):
        self.connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)
        self.cursor = self.connection.cursor()

    def get_user_ids_without_email(self):
        query = "SELECT ID FROM users WHERE email NOT LIKE '%@%'"
        self.cursor.execute(query)
        result = [row[0] for row in self.cursor.fetchall()]
        return result


db = DB()
db.create_connection()
ids_without_email = db.get_user_ids_without_email()
print(ids_without_email)

import pymysql
from credentials import DB_HOST, DB_USER, DB_DATABASE, DB_PASSWORD


class DB:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def create_connection(self):
        self.connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)
        self.cursor = self.connection.cursor()

    def get_user_ids_without_email(self):
        query = "SELECT id FROM users WHERE email NOT LIKE '%@%'"
        self.cursor.execute(query)
        result = [row[0] for row in self.cursor.fetchall()]
        return result



db = DB()
db.create_connection()
ids_without_email = db.get_user_ids_without_email()

# Print each ID on a separate line
for user_id in ids_without_email:
    print(user_id)
'''
import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

cursor = connection.cursor()
query = "select ID from users where email NOT like '%@%'"

cursor.execute(query)
result = cursor.fetchall()
my_list = list(result)
new_list = []
for i in my_list:
    new_list.append(i[0])
print(new_list)