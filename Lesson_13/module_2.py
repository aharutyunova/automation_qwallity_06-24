# The second module, another .py file, contains code where you declare a DB class object and call the update method and close method.

# The update method should update any 3 courses title, and in case reuslt is 3, commit, otherwise rollback changes


from module_1 import Db


my_db = Db()
my_db.db_update()
my_db.db_close()
