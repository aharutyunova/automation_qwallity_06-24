#Please also check the task results in lesson 13.

# Find out the user id with maximum account

import pymysql

class DB:
    def get_connection(self):
        connector = pymysql.connect(host='pro.freedb.tech',
                                    user='qwallity',
                                    password='6YJsZQk&##7J2?e',
                                    database='qwallitydb')
        return connector
    
    def max_account_id(self):
        connector = self.get_connection()
        cursor = connector.cursor()
        sql_data = """SELECT id FROM users ORDER BY account DESC LIMIT 1"""
        cursor.execute(sql_data)
        result = cursor.fetchone()
        if result is not None:
            print("Max Account ID", result)
            return result
            
        else:
            print("No user found")
            return None
        
    def close_db(self):
        self.get_connection().close()
        

database = DB()
database.max_account_id()


# Find out the earliest crieted course ID

class DB_1:
    def get_connection_1(self):
        connector = pymysql.connect(host='pro.freedb.tech',
                                    user='qwallity',
                                    password='6YJsZQk&##7J2?e',
                                    database='qwallitydb')
        return connector
    
    def earliest_course_id(self):
        connector = self.get_connection_1()
        cursor = connector.cursor()
        sql_data_1 = """SELECT id FROM courses ORDER BY date_created ASC LIMIT 1"""
        cursor.execute(sql_data_1)
        result = cursor.fetchone()
        if result:
            print("Earliest crieted course ID", result)
            return result
            
        else:
            print("No result found")
            return None
        
    def close_db(self):
        self.get_connection_1().close()
        

database_1 = DB_1()
database_1.earliest_course_id()



# Insert new course as author insert your name


class DB_2:
    def get_connection_2(self):
        connector = pymysql.connect(host='pro.freedb.tech',
                                    user='qwallity',
                                    password='6YJsZQk&##7J2?e',
                                    database='qwallitydb')
        return connector
    
    def new_course_title(self):
        connector = self.get_connection_2()
        cursor = connector.cursor()
        sql_data_2 = """Insert into courses (title, body, author, coursetype) values ("Test", "any description", "Shushan", 1 )"""
        cursor.execute(sql_data_2)
        connector.commit()
       
        
    def close_db_2(self):
        self.get_connection_1().close()
        

database_1 = DB_2()
database_1.new_course_title()

# Anna - very good solution, only in first and second methods you should use result[0] to get id as integer, not tuple
# You could also use 3 methods in the same class