# from tkinter import *
#
# root = Tk()
#
# Label(root, text="Red Sun", bg="red", fg="white").pack()
# Label(root, text="Green Grass", bg="green", fg="black").pack()
# Label(root, text="Blue Sky", bg="blue", fg="white").pack()
#
# mainloop()

# from tkinter import *
#
# root = Tk()
#
# w = Label(root, text="red", bg="red", fg="white")
# w.pack(padx=5, pady=20, side=RIGHT)
# w = Label(root, text="green", bg="green", fg="black")
# w.pack(padx=5, pady=20, side=LEFT)
# w = Label(root, text="blue", bg="blue", fg="white")
# w.pack(padx=5, pady=20, side=RIGHT)
#
# mainloop()

# '''https://www.python-course.eu/tkinter_layout_management.php
# http://zetcode.com/gui/tkinter/layout/
# http://effbot.org/tkinterbook/pack.htm '''
#
# import tkinter as tk
# import random
#
# root = tk.Tk()
# # width x height + x_offset + y_offset:
# root.geometry("170x200+30+30")
#
# languages = ['Python','Perl','C++','Java','Tcl/Tk']
# labels = range(5)
# for i in range(5):
#    ct = [random.randrange(256) for x in range(3)]
#    brightness = int(round(0.299*ct[0] + 0.587*ct[1] + 0.114*ct[2]))
#    ct_hex = "%02x%02x%02x" % tuple(ct)
#    bg_colour = '#' + "".join(ct_hex)
#    l = tk.Label(root,
#                 text=languages[i],
#                 fg='White' if brightness < 120 else 'Black',
#                 bg=bg_colour)
#    l.place(x = 20, y = 30 + i*30, width=120, height=25)
#
# root.mainloop()

import psycopg2 as psy
import pandas as p


# link = sqlite3.connect("flights.db") # link python to database file
# cur=link.cursor() #creates a cursor so we can select data
# cur.execute("SELECT * from airlines limit 5") # selects data
# results = cur.fetchall() # fetches selected database
# # print(results) # prints selected databace
# cur.close()  # closes cursor
# link.close() # closes database to avoid promblem later and avoid locking database

link =psy.connect("dbname='forumdb' user='postgres' password='post' host='localhost' port='5432'")
cur=link.cursor()
# cur.execute("DROP TABLE book")
cur.execute("CREATE TABLE IF NOT EXISTS Machines (id INTEGER PRIMARY KEY, Oddel TEXT, Broj INTEGER)")
cur.execute("CREATE TABLE IF NOT EXISTS Activity (id INTEGER PRIMARY KEY, Opis TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS Machine_Activity (id INTEGER PRIMARY KEY, Aktivsnot_id INTEGER, Mashina_id INTEGER, Frekfentnost INTEGER, Data TEXT, Operator TEXT)")
link.commit()
link.close()

# df = p.read_sql_query("SELECT * from Stored limit 5", link)
# print(df["Data"])
# type(df)
