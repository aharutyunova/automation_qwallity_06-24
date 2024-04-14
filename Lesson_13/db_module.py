import pymysql


# Create a program with two modules. One module, a .py file, contains the DB class where you implement three methods: db_connection, db_close, and update.

# The second module, another .py file, contains code where you declare a DB class object and call the update method and close method.

# The update method should update any 3 courses title, and in case reuslt is 3, commit, otherwise rollback changes.


class DB:
    def db_connection(self):
        connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')
        return connection
    
    def db_close(self):
        self.db_connection().close()
        return "DB connection closed"
    
    def db_update(self):
        cursor = self.db_connection().cursor()

        query_list = ["UPDATE courses SET title = 'AnnUpdated' WHERE id IN (9000349, 9000350, 9000346)",
"SELECT * from courses where id IN (9000349, 9000350, 9000346)"]
        for query in query_list:
            cursor.execute(query)
        if cursor.rowcount == 3:
            print('Changes commeted to DB:    ', cursor.fetchall())
            self.db_connection().commit()
        else:
            self.db_connection().rollback()
            print('Changes not commeted to DB:    ', cursor.fetchall())


# Anna - everything is correct, only for avoid create connection several time for example in db_close()
# method you create connection  one more time and then close it
# Instead of it you could have connection in def __init__ () 
"""
def __init__(self):
    self.conn = None
    def db_connection(self):
        
        self.conn = pymysql.connect(host= 'pro.freedb.tech',
                             user = 'qwallity',
                             password = '6YJsZQk&##7J2?e',
                             database = 'qwallitydb')
        
     
And in other methods already use self.connection

"""

# I will change example in ppt too, this part was not well described there