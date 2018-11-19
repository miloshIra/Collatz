import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import Spinbox


window = tk.Tk()
window.title('Radica i farmerkite so visok struk')

tabControl = ttk.Notebook(window)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tabControl.pack(expand=1, fill='both')

monty = ttk.LabelFrame(tab1, text = "Monty Py")
monty.grid(column=0, row=0)

aLabel = ttk.Label(monty, text="A Labal")
aLabel.grid(column=0, row=0)

def clickMe():
    action.configure(text='Hello ' + name.get() + ' ' + numberChosen.get())
ttk.Label(monty, text="Enter a name:").grid(column=0, row=0, sticky='W')

name = tk.StringVar()
nameEntered = ttk.Entry(monty, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky=tk.W)

action = ttk.Button(monty, text="Click Me", command = clickMe)
action.grid(column=2, row=1)

ttk.Label(monty, text="Choose a number: ").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 3, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Adding a spinbox widget
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')


spin = Spinbox(monty, values=[1,2,3,4,12,42], width=5, bd=8, command=_spin)
spin.grid(column=0, row=2)

spin = Spinbox(monty, values=(0, 50, 100), width=5, bd=8, command=_spin, relief=tk.RIDGE)
spin.grid(column=1, row=2)

monty2 = ttk.LabelFrame(tab2, text="The snake")
monty2.grid(column=0, row=0, padx=8, pady=4)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty2, text='UnChecked', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=0, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=0, sticky=tk.W) #sticky = tk.W means stuck to the west (left), it is a positional setting

chVarEn = tk.IntVar()
check3=tk.Checkbutton(monty2, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)
#scr.grid(column=0, columnspan=3)

colors = ["Blue", "Gold","Red"]

def radCall():
    radSel = radVar.get()
    if    radSel == 0: monty2.configure(text="Blue")
    elif  radSel == 1: monty2.configure(text="Gold")
    elif  radSel == 2: monty2.configure(text="Red")

#Radio buttons example

radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty2, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)



# Adding label frame with labels

labelsFrame = ttk.LabelFrame(monty2, text='Labels in a Frame ')
labelsFrame.grid(column=1, row=7, padx=20, pady=40)

ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)

# Exit GUI cleanly

def _quit():
    window.quit()
    window.destroy()
    exit()

#Creating Menu bar

menuBar = Menu(window)
window.config(menu=menuBar)

#Adding menu items

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

def _msgBox():
    # mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter: \n             The year is 2016')
    # mBox.showwarning('Python message warning box', 'There might be a bug in this code, happy hunting :).')
    mBox.showerror('Python Message Error Box', 'A Python GUI created using tkinter: \n                   Error')
    answer = mBox.askyesno('Pyton Message Dual Choice Box', 'Are you really wish to o this ?')
    print(answer)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)

# Place cursor into name Entry
window.iconbitmap(r'C:\Users\Ira\AppData\Local\Discord\app-0.0.301\app.ico')

nameEntered.focus()
monty.mainloop()
