import pymysql
from credentials import DB_HOST, DB_USER, DB_DATABASE, DB_PASSWORD


class DB:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def create_connection(self):
        self.connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)
        self.cursor = self.connection.cursor()

    def db_update(self):
        self.create_connection()
        try:
            self.cursor.execute("UPDATE courses SET title='Izabella_courses5' where id in (9000334,9000335,9000336)")
            if self.cursor.rowcount == 3:
                self.connection.commit()
                print("Changes committed")
            else:
                self.connection.rollback()
                print("Rollback changes")
        except pymysql.Error as e:
            print("Error:", e)
            self.connection.rollback()


# Create a program with two modules. One module, a .py file, contains the DB class where you implement
# three methods: db_connection, db_close, and update.

# The second module, another .py file, contains code where you declare a DB class object and call the
# update method and close method.

# The update method should update any 3 courses title, and in case reuslt is 3, commit, otherwise rollback changes
