# Create a program with two modules. One module, a .py file, contains the DB class where you implement three methods: db_connection, db_close, and update.

# The second module, another .py file, contains code where you declare a DB class object and call the update method and close method.

# The update method should update any 3 courses title, and in case reuslt is 3, commit, otherwise rollback changes

import pymysql

class DB:

    def create_connection(self):
        connection = pymysql.connect(host= 'pro.freedb.tech',
                             user = 'qwallity',
                             password = '6YJsZQk&##7J2?e',
                             database = 'qwallitydb')
        
        return connection
        
    def update_courses(self):
        connection = self.create_connection()
        cursor  = connection.cursor() 
        # cursor.execute("select * from courses  WHERE price = 15")
        result = cursor.execute("UPDATE courses SET title = 'aaaaaaabbbb' WHERE price = 15")
        # result = cursor.fetchall()
    
        if result == 1:
           connection.commit()
        else:
           connection.rollback()

    def connection_close(self):
        connection = self.create_connection()
        connection.close()



