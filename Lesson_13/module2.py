from module1 import DB
obj = DB()
obj.create_connection()
obj.update_courses()
obj.connection_close()