import sqlite3

link=sqlite3.connect("Cookies")
cursor=link.cursor()
cursor.execute("SELECT host_key FROM Cookies limit 10")
results=cursor.fetchall()
print(results)
link.close()
