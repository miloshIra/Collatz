import psycopg2 as psy
import guiDBconfig as gDB

GUIDB = 'guiDB'

conn = psy.connect(**gDB.dbConfig)
cursor = conn.cursor()

try:
    cursor.execute("SET AUTOCOMMIT ON") # this is not working try to find a way to set autocommit on!
    cursor.execute("CREATE DATABASE {} ".format(GUIDB))
except psy.Error as err:
    print("Failed to create DB: {}".format(err))

conn.close
