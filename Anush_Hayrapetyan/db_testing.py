import pymysql


class DB:
    def db_connection(self):
        return pymysql.connect(
            host='pro.freedb.tech',
            user='qwallity',
            password='6YJsZQk&##7J2?e',
            database='qwallitydb')

    def db_close(self):
        self.db_connection().close()

    def update(self):
        db_con = self.db_connection()
        cursor = db_con.cursor()
        update_query = '''update users set email = 'anushikkk@gmail.com' where id = 1'''
        cursor.execute(update_query)
        db_con.commit()
