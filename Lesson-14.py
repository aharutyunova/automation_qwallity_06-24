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
        cur.execute("select id from users where account=2147483647") #Anna cursor.execute not cur.execute, as in line 16 you put variable name as cursor
        result1=cur.fetchall()
        print(result1[0][0])

# 2 Find out the earliest crieted course ID     

cur2 = connection.cursor() #Anna - connection is not accessed here, you should write it as you did it in step 16
cur2.execute("select id from courses order by date_created ASC")
result3 = cur2.fetchall()
print(result3) 

# 3 Insert new course as author insert your name

cur3 = 'connection'.cursor()






#I didn’t finish Anna jan, I couldn’t write my name)) I think I registered in the database, but it didn’t work

# Mariam jan you try to solve but as you use varaible names not in correct way code doesn't work

# Please pull from github any solution, and on working code change query so it return your name, 
# and then startr change something in the code and check
# Pull code, be sure it works, change something and run, and repeat this flow several time with different changes