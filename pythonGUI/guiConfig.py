
import psycopg2 as pd

conn = pd.connect(**DB.dbconfig)
cur = conn.cursor

try:
    cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(GUIDB))
except pd.Error as err:
    print("Failed to create DB:{}"".format(err))

print(conn)
conn.close
