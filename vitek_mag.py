import vez
import tkinter as tk
from tkinter import ttk
import time
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

def open_work_window():
    workwindow=tk.Toplevel(win)
    workwindow.geometry("500x300")
    workwindow.title("Споредвање кутии")
    workwindow.focus()
    bLabel=ttk.Label(workwindow, text="Прва кутија")
    bLabel.place(x=50, y=95)

    barcode1 = tk.StringVar()
    barcode1Entry=ttk.Entry(workwindow, width=12, textvariable=barcode1)
    barcode1Entry.place(x=50, y=115)
    barcode1Entry.focus()

    cLabel=ttk.Label(workwindow, text="Втора кутија")
    cLabel.place(x=50, y=150)

    barcode2 = tk.StringVar()
    barcode2Entry=ttk.Entry(workwindow, width=12, textvariable=barcode2)
    barcode2Entry.place(x=50, y=170)

    canvas = tk.Canvas(workwindow, bg="blue", width=280, height=260)
    canvas.place(x=200,y=20)


    def gun_read():
        bar1 = barcode1.get()
        print(bar1)
        bar2 = barcode2.get()
        print(bar2)
        today=datetime.datetime.now()
        if bar1 == bar2:
            print("TOCHNO!!")
            canvas.itemconfig(fill="green")
            with open('log.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                export_tup1 = (user,bar1,bar2,str(today.strftime('%d-%m-%y')),str(today.strftime('%H:%M')),'Tochno')
                csv_writer.writerow(export_tup1)
            barcode1Entry.delete(0,tk.END)
            barcode2Entry.delete(0,tk.END)
            return True
        else:
            print("GRESHKA!!")
            canvas.itemconfig(fill="red")
            with open('log.csv', 'a', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                export_tup2 = (user,bar1,bar2,str(today.strftime('%d %m %y')),str(today.strftime('%H:%M')),'Ne tochno')
                csv_writer.writerow(export_tup2)
            barcode1Entry.delete(0,tk.END)
            barcode2Entry.delete(0,tk.END)
            return False

    checkbutton = ttk.Button(workwindow, text="Провери", command=gun_read)
    checkbutton.place(x=50, y=220)




def check_user(): #funkcira za validacija na user
    if user.get() == 'Admin':
        print('Admin rights page: ')
    else:
        pass  #go to window with addmin previlage and functions.

    if user.get() not in user_list:
        aLabel.configure(background="red")
        aLabel.configure(text="Внесовте погрешно име, Обидете се повторно ")
        userEntry.delete(0,tk.END)
        # display error message window

    else:
        aLabel.configure(background="green")
        aLabel.configure(text="Дозволен пристап ")
        time.sleep(0.5)
        win.withdraw() #Hide loging window! <3
        open_work_window()


        #continue to barcode checks



# def gun_read():
#     bar1 = barcode1.get()
#     print(bar1)
#     bar2 = barcode2.get()
#     print(bar2)
#     today=datetime.datetime.now()
#     if bar1 == bar2:
#         print("TOCHNO!!")
#         with open('log.csv', 'a', newline='') as csv_file:
#             csv_writer = csv.writer(csv_file)
#             export_tup1 = (user,bar1,bar2,str(today.strftime('%d-%m-%y')),str(today.strftime('%H:%M')),'Tochno')
#             csv_writer.writerow(export_tup1)
#         return True
#     else:
#         print("GRESHKA!!")
#         with open('log.csv', 'a', newline='') as csv_file:
#             csv_writer = csv.writer(csv_file)
#             export_tup2 = (user,bar1,bar2,str(today.strftime('%d %m %y')),str(today.strftime('%H:%M')),'Ne tochno')
#             csv_writer.writerow(export_tup2)
#         return False

def _quit():
    win.quit()
    win.destroy()
    exit()

#---------- MAIN WINDOW WIDGETS!!!!----------------------------#

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
