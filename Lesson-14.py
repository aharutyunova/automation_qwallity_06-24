# 1 Find out the user id with maximum account


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
        cur.execute("select id from users where account=2147483647")
        result1=cur.fetchall()
        print(result1[0][0])

# 2 Find out the earliest crieted course ID     

cur2 = connection.cursor()
cur2.execute("select id from courses order by date_created ASC")
result3 = cur2.fetchall()
print(result3) 

# 3 Insert new course as author insert your name

cur3 = 'connection'.cursor()
