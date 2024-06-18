import pymysql


class Db:
    def __init__(self):
        self.connection = None

    def db_connection(self):
        self.connection = pymysql.connect(
            host="pro.freedb.tech",
            user="qwallity",
            password="6YJsZQk&##7J2?e",
            database="qwallitydb")
        print("Database connection established.", self.connection)

    def get_max_account(self):
        if self.connection is None:
            self.db_connection()
        cursor = self.connection.cursor()
        cursor.execute("select account, id from users order by account desc limit 1")
        result = cursor.fetchone()
        account, id = result
        print(f"Max account: {account}, User ID: {id}")
        cursor.close()

    def get_earliest_course(self):
        if self.connection is None:
            self.db_connection()
        cursor = self.connection.cursor()
        cursor.execute("select id, title, author, date_created from courses order by date_created limit 1")
        result = cursor.fetchone()
        id, title, author, date_created = result
        print(f"User ID: {id}, title: {title}, author: {author}, created date: {date_created}")
        cursor.close()

    def new_course(self):
        if self.connection is None:
            self.db_connection()
        cursor = self.connection.cursor()
        cursor.execute("insert into courses (title, body, author, date_created, coursetype, price) values ('Mindful Living', '', 'Lusine', now(), 1, '5000');")
        self.connection.commit()
        id = cursor.lastrowid
        cursor.execute("select id, title, author, date_created, coursetype, price from courses where id = %s", (id,))
        result = cursor.fetchone()
        id, title, author, date_created, coursetype, price = result
        print(f"Newly inserted course ID: {id}, title: {title}, author: {author}, created date: {date_created}, coursetype: {coursetype}, price: {price}")
        cursor.close()

    def db_close(self):
        self.connection.close()
        print("Database connection closed.")
