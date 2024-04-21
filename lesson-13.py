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
        # cursor.execute("select * from courses  WHERE price = 1000")
        result = cursor.execute("UPDATE courses SET title = AAAA WHERE price =1000")
        # result = cursor.fetchall()
        