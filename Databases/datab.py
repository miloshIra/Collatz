import psycopg2 as ps
#
# class Database(object):
#
#     def __init__(self):
#         self._db_link = ps.connect("dbname='maintenace',  user='postgres', password='post', host='localhost', post='5432'")
#         self._db_cur = self._db_link.cursor()
#         print('asdasdasd')
#         self._db_cur.execute("CREATE TABLE IF NOT EXISTS Accounts(User TEXT, Password TEXT, Status TEXT)")
#         self._db_link.commit()
#
#     def query(self, query, params):
#         return self._db_cur.execute(query, params)
#
#     def kill():
#         self._db_link.close()
#
# class MyDB(object):
#
#     def __init__(self):
#         self._db_connection = ps.connect("dbname='maintenancedb' user='postgres' password='post' host='localhost' port='5432'")
#         self._db_cur = self._db_connection.cursor()
#         self._db_cur.execute("CREATE TABLE IF NOT EXISTS Acc(User TEXT, Pass TEST, Status TEXT)")
#         priint("Connected...")
#
#     def query(self, query, params):
#         return self._db_cur.execute(query, params)
#
#     def __del__(self):
#         self._db_connection.close()

class DB(object):

    def __init__(self):
        self.link = ps.connect("dbname='postgres' user='postgres' password='post' host='localhost' port='5432'")
        self.cur = self.link.cursor()
        self.cur.execute("DROP TABLE Acc")
        #self.cur.execute("CREATE TABLE IF NOT EXISTS Acc (Users TEXT, AA INTEGER )")"
        self.link.commit()
        self.link.close()


# shit dont work don't  know why fcking crazy .. -.- wtf wtf wtf -.-
