import pymysql

connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')
cursor = connection.cursor()
query = "select * from users"
cursor.execute(query)
result = cursor.fetchone()
rowcount = cursor.rowcount
print(rowcount)
print(result)

# ---------------------------------------------------------

class DB:
    def __init__(self):
        self.create_conection 

    def create_conection(self):
        connection = pymysql.connect(host='pro.freedb.tech',
                                     user='qwallity',
                                     password='6YJsZQk&##7J2?e',
                                     database='qwallitydb')
        return connection
    
    def update(self):
        cursor = connection.cursor()
        query = "SELECT * FROM table_name WHERE Name LIKE '%Test%'"
        query = "UPDATE table_name SET name = 'Anna' WHERE id = 10"
        cursor.execute(query)
        result = cursor.fetchone()
        print(result)

    def close_connection(self):
        self.create_conection().close()


# ----------------------------------------------------------------

class DB2(DB):
        def __init__(self):
            super().__init__()
            self.update_sql_info = None
        
    
def update_sql_info(self, course_id, new_title):
        try:
            self.cursor.execute("UPDATE courses SET title = AUTOMATION WHERE id = 20", (new_title, course_id))
        except pymysql.Error as e:
            print(f"Error updating course: {e}")
            self.connection.rollback()
        else:
            self.connection.commit()
            print("Succsess message")



# Create a program with two modules. One module, a .py file, contains the DB class where you implement three methods: db_connection, db_close, and update.

# The second module, another .py file, contains code where you declare a DB class object and call the update method and close method.

# The update method should update any 3 courses title, and in case reuslt is 3, commit, otherwise rollback changes