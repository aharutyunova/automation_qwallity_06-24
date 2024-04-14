# Create a program with two modules. One module, a .py file, contains the DB class where you implement three methods: db_connection, db_close, and update.

import pymysql


class Db:
    def db_connection(self):
        self.connection = pymysql.connect(
            host="pro.freedb.tech",
            user="qwallity",
            password="6YJsZQk&##7J2?e",
            database="qwallitydb")
        print("Database connection established.", self.connection)

    def db_update(self):
        self.db_connection()
        cursor = self.connection.cursor()
        cursor.execute("UPDATE courses SET title='Test Lus' WHERE author='Admin'")
        result = cursor.rowcount
        # Whithout checking of row count it works but why it doesn't work with checking I couldn't understand, yet ))
        if result == 3:
            print(f"Rows updated: {result}")
            self.connection.commit()
        else:
            self.connection.rollback()
        cursor.close()

    def db_close(self):
        self.connection.close()
