import pymysql

class db:
    def __init__(self):

        
    def db_connect(self):
        self.connection = pymysql.connect(host='pro.freedb.tech',
                             user='qwallity',
                             password='6YJsZQk&##7J2?e',
                             database='qwallitydb')
    
    def db_close(self):
        self.connection.close()
        
    def db_update(self):
        self.db_connect()
        cursor = self.connection.cursor()
        my_query= "update courses title set title = 'update_hamest' where body = 'my_apdate_indicator"
        cursor.execute(my_query)
        if cursor.rowcount != 3:
            self.connection.rollback()
        else: 
            self.connection.commit()
        
        self.db_close()


            
