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
        print(result)
        if result == 3:
           
            print(f"Rows updated: {result}")
            self.connection.commit()
        else:
            self.connection.rollback()
        cursor.close()

    def db_close(self):
        self.connection.close()


# Anna - correct, you could also define connection as variable in def __init__ ()

"""
def __init__(self):
    self.connection = None

def db_connection(self):
    self.connection = pymysql.connect(
        host="pro.freedb.tech",
        user="qwallity",
        password="6YJsZQk&##7J2?e",
        database="qwallitydb")
    print("Database connection established.", self.connection)


"""
# This part was not so good described in ppt, I will change this example

# What about result, yes it is get the same value of effected row, 
# in your example 263 row effected, so result==3 doesn't work, if you mean this part
