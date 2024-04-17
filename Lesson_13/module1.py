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
        result = cursor.execute("SELECT DISTINCT user_id FROM user_courses;")
        result = cursor.fetchall()
        my_list = []
        for i in result:
            my_list.append(i[0])
        print(my_list) 
    def connection_close(self):
        connection = self.create_connection()
        connection.close()

obj = DB()
obj.create_connection()
obj.update_courses()
obj.connection_close()

# Anna - everything is correct, only for avoid create connection several time for example in connection_close()
# method you create connection  one more time and then close it
# Instead of it you could have connection in def __init__ () 
"""
def __init__(self):
    self.conn = None
    def create_connection(self):
        
        self.conn = pymysql.connect(host= 'pro.freedb.tech',
                             user = 'qwallity',
                             password = '6YJsZQk&##7J2?e',
                             database = 'qwallitydb')
    
     
And in other methods already use self.connection

"""

# I will change example in ppt too