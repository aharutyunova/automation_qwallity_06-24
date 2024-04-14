import pymysql

class DB:

    def create_connection(self):
           con = my

pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')

def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

def db_connection(self):
        self.connection = pymysql.connect(
           host=self.host,
           user=self.user,
           password=self.password,
           database=self.database
        )

def db_close(self):
        self.connection.close()
        print("Connection closed.")

def update(self, ....):