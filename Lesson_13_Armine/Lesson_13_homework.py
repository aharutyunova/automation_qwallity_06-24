# Create a program with two modules. One module, a .py file, contains the DB class where you implement three methods: db_connection, db_close, and update.

# The second module, another .py file, contains code where you declare a DB class object and call the update method and close method.

# The update method should update any 3 courses title, and in case reuslt is 3, commit, otherwise rollback changes



import mysql.connector


class working_with_DB:
    def __init__(self):
        self.connection = None

    def DB_connection(self):
        self.connection = mysql.connector.connect(host='pro.freedb.tech',
                                             user='qwallity',
                                             password='6YJsZQk&##7J2?e',
                                             database='qwallitydb')
        
        return self.connection
    
    
    def DB_update(self):
        self.DB_connection()  #Anna - you should call this method to create connection
        cursor = self.connection.cursor()
        cursor.execute("update courses set title = 'Katrina5' where id IN (9000404, 9000405, 9000406)")
      
        if cursor.rowcount == 3:
            print("Here are your updates")
            self.connection.commit()
        else:
            print("Something went wrong, your changes are rollback")
            self.connection.rollback()
    
    def DB_close(self):
        self.DB_connection().close()  # Anna -you could use self.connect.close() as you already assign connection to self.connection variable

working_with_DB().DB_update()


#Anna jan, but I do not understand why 'else' is being printed, and no updates in Database, but when I try to update one ID,
# where rowcount = 1, in this casedata base is being updated and 'If' statement is being printed))
# Look if you update same ids with same values, second time no rows are effected and else branch is work
# If you change updated value, for example Katrin15, you will get  - Here are your updates message