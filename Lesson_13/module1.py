# Create a program with two modules. One module, a .py file, contains the DB class where you implement three methods: db_connection, db_close, and update.

# The second module, another .py file, contains code where you declare a DB class object and call the update method and close method.

# The update method should update any 3 courses title, and in case reuslt is 3, commit, otherwise rollback changes
import pymysql
import mysql.connector

class DB:
    def db_connection(self):
        connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')
        return connection
    
    def db_close(self):
        self.db_connection().close()
        return 'DB closed'
    
    def db_update(self):

        cursor = self.db_connection().cursor()

        query_list = ["UPDATE courses SET title = 'RayaTitleUpdated' where id in (9000335, 9000336, 9000337)",
                 "SELECT * from courses where id in (9000335, 9000336, 9000337)"]
        for query in query_list:
            cursor.execute(query)
        if cursor.rowcount ==3:
            print('COMMITTED:    ',cursor.fetchall())
            self.db_connection().commit()
        else:
            print('NOT COMMITTED:    ',cursor.fetchall())
            self.db_connection().rollback()
        return 1
    
# Anna - everything is correct, only for avoid create connection several time for example in db_close()
# method you create connection  one more time and then close it
# Instead of it you could have connection in def __init__ () 
"""
def __init__(self):
    self.conn = None
    def create_connection(self):
        
        self.connection = pymysql.connect(host= 'pro.freedb.tech',
                             user = 'qwallity',
                             password = '6YJsZQk&##7J2?e',
                             database = 'qwallitydb')
        
     
And in other methods already use self.connection

"""
# I changed example in PPT also

# And one question why you need return 1 in db_update method?