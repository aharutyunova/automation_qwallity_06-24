# Create a program with two modules. One module, a .py file, contains the DB class where you implement three methods: db_connection, db_close, and update.
import logging 

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='my_log.log', 
                    filemode='w+', 
                    encoding='utf-8')


import pymysql

class DB:
    def db_connection(self):
        connector = pymysql.connect(host='pro.freedb.tech',
                                    user='qwallity',
                                    password='6YJsZQk&##7J2?e',
                                    database='qwallitydb')
        return connector
    
    def update(self):
        connector = self.db_connection()
        cursor = connector.cursor()
        try:
            sql_data = """UPDATE account SET account_balance = 555 WHERE account_balance = 0"""
            cursor.execute(sql_data)
            connector.commit()
        except Exception as e:
            print("Error:", e)
            connector.rollback()
        finally:
            cursor.close()
            connector.close()

database = DB()
database.update()

#Another example

class Database_name:
    def create_connection(self):
         conn = pymysql.connect(host='pro.freedb.tech',
                                    user='qwallity',
                                    password='6YJsZQk&##7J2?e',
                                    database='qwallitydb')
         return conn
   
    def db_update(self):
        db = self.create_connection()
        cursor = db.cursor()
        sql_data1 = """UPDATE account set account_name = "Unknown member" WHERE account_balance = 555"""
        cursor.execute(sql_data1)
        db.commit()
        
    def db_close(self):
        self.create_connection().close()


db = Database_name()
db.db_update()   



# The update method should update any 3 courses title, and in case reuslt is 3, commit, otherwise rollback changes

class DB_update_courses_titles_1:
    def db_connection1(self):
        connect = pymysql.connect(host='pro.freedb.tech',
                                    user='qwallity',
                                    password='6YJsZQk&##7J2?e',
                                    database='qwallitydb')
        return connect
    
    def db_update_courses_1(self):
        db_1 = self.db_connection1()
        cursor = db_1.cursor()
        sql_data_1 = """UPDATE courses set title = "Shushan's change" WHERE price = 3000"""
        cursor.execute(sql_data_1)
        if cursor.rowcount == 3:
                db_1.commit()
                print("Changes committed.")
        else:
                db_1.rollback()
                print("Rolling back changes.")

    def db_close_courses_1(self):
        self.db_connection1().close()



db1 = DB_update_courses_titles_1()
db1.db_update_courses_1() 