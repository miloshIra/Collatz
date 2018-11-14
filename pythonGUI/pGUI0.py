import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title('Radica i farmerkite so visok struk')

monty = ttk.LabelFrame(window, text = "Monty Py")
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

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(monty, text='UnChecked', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(monty, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W) #sticky = tk.W means stuck to the west (left), it is a positional setting

chVarEn = tk.IntVar()
check3=tk.Checkbutton(monty, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(monty, width=scrolW, height=scrolH, wrap=tk.WORD)
#scr.grid(column=0, sticky='WE', columnspan=3)
scr.grid(column=0, columnspan=3)

colors = ["Blue", "Gold","Red"]

def radCall():
    radSel = radVar.get()
    if    radSel == 0: monty.configure(background=colors[0])
    elif  radSel == 1: monty.configure(background=colors[1])
    elif  radSel == 2: monty.configure(background=colors[2])

#Radio buttons example

radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(monty, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

# Adding label frame with labels

labelsFrame = ttk.LabelFrame(monty, text='Labels in a Frame ')
labelsFrame.grid(column=1, row=7, padx=20, pady=40)

ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=4)


# Place cursor into name Entry

nameEntered.focus()
monty.mainloop()
