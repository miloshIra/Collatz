
import tkinter as tk
from tkinter import ttk
import time
import datetime
import os
import csv

win = tk.Tk()
win.title("Vitek magacin v1.0")
win.geometry("500x270")
win.configure(background='gold')

frame1=ttk.LabelFrame(win, text="  Логирање  ", width=300, height=150)
frame1.place(x=15, y=15)

user_list=['Darko1234','Dragi4321','Inzeneradmin']



def open_work_window():
    workwindow=tk.Toplevel(win)
    workwindow.geometry("500x300")
    workwindow.title("Споредвање кутии")
    workwindow.focus_force()

    frame2=ttk.LabelFrame(workwindow, text="  Споредување кутии  ", width=220, height=262)
    frame2.place(x=5, y=18)

    bLabel=ttk.Label(workwindow, text="Прва кутија:")
    bLabel.place(x=50, y=65)


    barcode1 = tk.StringVar()
    barcode1Entry=ttk.Entry(workwindow, width=11, textvariable=barcode1)
    barcode1Entry.place(x=50, y=85)
    barcode1Entry.focus()

    cLabel=ttk.Label(workwindow, text="Втора кутија:")
    cLabel.place(x=50, y=120)

    barcode2 = tk.StringVar()
    barcode2Entry=ttk.Entry(workwindow, width=11, textvariable=barcode2)
    barcode2Entry.place(x=50, y=140)

    canvas = tk.Canvas(workwindow, bg="gold", width=280, height=260)
    canvas.place(x=200,y=20)



    def gun_read():
        bar1 = barcode1.get()
        print(bar1)
        bar2 = barcode2.get()
        print(bar2)
        today=datetime.datetime.now()
        if bar1 == bar2:
            print("TOCHNO!!")
            with open('log.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                export_tup1 = (user.get(),bar1,bar2,str(today.strftime('%d-%m-%y')),str(today.strftime('%H:%M')),'Tochno')
                csv_writer.writerow(export_tup1)
            barcode1Entry.delete(0,tk.END)
            barcode2Entry.delete(0,tk.END)
            canvas.configure(bg="green")
            barcode1Entry.focus()
            return True

        else:
            print("GRESHKA!!")
            with open('log.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                export_tup2 = (user.get(),bar1,bar2,str(today.strftime('%d %m %y')),str(today.strftime('%H:%M')),'Ne tochno')
                csv_writer.writerow(export_tup2)
            barcode1Entry.delete(0,tk.END)
            barcode2Entry.delete(0,tk.END)
            canvas.configure(bg="red")
            barcode1Entry.focus()
            return False

    def clear_fields():
        barcode1Entry.delete(0,tk.END)
        barcode2Entry.delete(0,tk.END)
        barcode1Entry.focus()


    checkbutton = ttk.Button(workwindow, text="Провери", command=gun_read)
    checkbutton.place(x=50, y=220)

    clearentrybutton = ttk.Button(workwindow, text="Избриши", command=clear_fields)
    clearentrybutton.place(x=50, y= 250)

    def checker(event):
        if len(barcode1.get())==11:
            barcode2Entry.focus()
        if len(barcode2.get())==11:
            gun_read()

    workwindow.bind('<Key>', checker)


def check_user(): #funkcira za validacija na user
    if user.get() == 'Admin':
        print('Admin rights page: ')
    else:
        pass  #go to window with addmin previlage and functions.

    if user.get()+password.get() not in user_list:
        aLabel.configure(background="red")
        aLabel.configure(text="Внесовте погрешно име или лозинка")
        userEntry.delete(0,tk.END)
        passwordEntry.delete(0,tk.END)
        # display error message window

    else:
        aLabel.configure(background="green")
        aLabel.configure(text="Дозволен пристап ")
        time.sleep(0.5)
        win.withdraw()             #Hide loging window! <3
        open_work_window()




def _quit():
    win.quit()
    win.destroy()
    exit()

#---------- MAIN WINDOW WIDGETS!!!!----------------------------#


aLabel=ttk.Label(frame1, text="Име на корисник:")
aLabel.place(x=2, y=2)

bLabel=ttk.Label(frame1, text="Лозинка на корисник:")
bLabel.place(x=2, y=65)

user = tk.StringVar()
userEntry = ttk.Entry(frame1, width=12, textvariable=user)
userEntry.place(x=2, y=30)
userEntry.focus()   # focuses start on this entrybox!!


password = tk.StringVar()
passwordEntry = ttk.Entry(frame1, show="*", width=12, textvariable=password)
passwordEntry.place(x=2, y=90)

AcceptUserButton = ttk.Button(win, text="Почни", command=check_user)
AcceptUserButton.place(x=15, y=180)

KillButton = ttk.Button(win, text="Затвори", command=_quit)
KillButton.place(x=370, y=180)



# use one file for front and backend, define backend function, buttonfunctions, and GUI code
#win.iconbitmap(r'c:\Python32\DLLs\py.ico')
win.mainloop()
