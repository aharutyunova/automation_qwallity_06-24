
# Find out the user id with maximum account


import pymysql

class DB:
    def __init__(self):
        self.connection = None

    def create_connection(self):
            self.connection = pymysql.connect(host= 'pro.freedb.tech',
                                    user = 'qwallity',
                                    password = '6YJsZQk&##7J2?e',
                                    database = 'qwallitydb')
            
       
            
    def max_count(self):
        cursor  = self.connection.cursor() 
        result = cursor.execute("SELECT id,MAX(account) FROM users")
        result = cursor.fetchall()
        print(f'userID = {result[0][0]}, max_count = {result[0][1]}')

    def connection_close(self):
        self.connection.close()

obj = DB()
obj.create_connection()
obj.max_count()
obj.connection_close()

# Find out the earliest crieted course ID


class DB:
    def __init__(self):
        self.connection = None
    def create_connection(self):
            
        self.connection = pymysql.connect(host= 'pro.freedb.tech',
                                    user = 'qwallity',
                                    password = '6YJsZQk&##7J2?e',
                                    database = 'qwallitydb')
            
        
            
    def earliest_created_courseID(self):
        cursor  = self.connection.cursor() 
        result = cursor.execute("SELECT MIN(date_created) FROM courses")
        result = cursor.fetchall()
        print(f'The earliest crieted course ID = {result[0][0]}')

    def connection_close(self):
        self.connection.close()

obj = DB()
obj.create_connection()
obj.earliest_created_courseID()
obj.connection_close()

# # Insert new course as author insert your name

class DB:
    def __init__(self):
        self.connection = None
    def create_connection(self):
            
        self.connection = pymysql.connect(host= 'pro.freedb.tech',
                                    user = 'qwallity',
                                    password = '6YJsZQk&##7J2?e',
                                    database = 'qwallitydb')
            
        
            
    def add_new_course(self):
        cursor  = self.connection.cursor() 
        result = cursor.execute("INSERT INTO courses (title,body,author,date_created,coursetype,price) VALUES ('NewCourse','testbodynew','Juli','2024-03-25 21:52:51',1,1)")
        self.connection.commit()
        

    def connection_close(self):
        self.connection.close()

obj = DB()
obj.create_connection()
obj.add_new_course()
obj.connection_close()
