import vez
import tkinter as tk
from tkinter import ttk
import datetime
import os
import csv

win = tk.Tk()
win.title("Vitek magacin")
win.geometry("500x300")
win.configure(background='gold')



aLabel=ttk.Label(win, text="Внесете го вашето име или број:")
aLabel.place(x=150, y=100)

user_list=['Darko','Dragi','Admin']

def check_user(): #funkcira za validacija na user
    if user.get() == 'Admin':
        print('Admin rights page: ')
    else:
        pass  #go to window with addmin previlage and functions.

    if user.get() not in user_list:
        aLabel.configure(background="red")
        aLabel.configure(text="Внесовте погрешно име ")
        # display error message window

    else:
        aLabel.configure(background="green")
        aLabel.configure(text="Дозволен пристап ")
        
        #continue to barcode checks


def gun_read():
    barcode1 = input("Please read the first barcode!?")
    print(barcode1)
    barcode2 = input("Plese read the secdon barcode?!")
    print(barcode2)
    today=datetime.datetime.now()
    if barcode1 == barcode2:
        print("TOCHNO!!")
        with open('log.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            export_tup1 = (user,barcode1,barcode2,str(today.strftime('%d-%m-%y')),str(today.strftime('%H:%M')),'Tochno')
            csv_writer.writerow(export_tup1)
        return True
    else:
        print("GRESHKA!!")
        with open('log.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            export_tup2 = (user,barcode1,barcode2,str(today.strftime('%d %m %y')),str(today.strftime('%H:%M')),'Ne tochno')
            csv_writer.writerow(export_tup2)
        return False

def _quit():
    win.quit()
    win.destroy()
    exit()

user = tk.StringVar()
userEntry = ttk.Entry(win, width=12, textvariable=user)
userEntry.place(x=175, y=125)
userEntry.focus()   # focuses start on this entrybox!!


AcceptUserButton = ttk.Button(win, text="Почни", command=check_user)
AcceptUserButton.place(x=177, y=150)

KillButton = ttk.Button(win, text="Exit", command=_quit)
KillButton.place(x=350, y=250)

# use one file for front and backend, define backend function, buttonfunctions, and GUI code

win.mainloop()
