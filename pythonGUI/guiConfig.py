
import psycopg2 as ps
import GUIDB

DB = 'GUIDB'

conn = ps.connect("dbname='GUIDB' user='postgres' password='post' host='localhost' port='5432'")
cursor = conn.cursor()
cursor.execute("CREATE TABLE Quotations (Quote_ID INT, Quoatation VARCHAR(250),
                                        Books_Book_ID INT,
                                        SERIAL (Quote_ID),
                                        FOREGIN KEY (Books_Book_ID)
                                        ON DELETE CASCADE")
cursor.execute("SELECT * FROM BOOKS")
print(cursor.fetchall())

print(conn)
conn.close
