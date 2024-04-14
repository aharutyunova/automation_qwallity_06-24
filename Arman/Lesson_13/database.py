import mysql.connector


class DB:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor()

    def db_connection(self):
        return self.conn

    def db_close(self):
        self.conn.close()

    def update(self, course_id, new_title):
        try:
            self.cursor.execute("UPDATE courses SET title = %s WHERE id = %s", (new_title, course_id))
            self.conn.commit()
            return 3  # Success
        except mysql.connector.Error as e:
            self.conn.rollback()
            return str(e)  # Error message
