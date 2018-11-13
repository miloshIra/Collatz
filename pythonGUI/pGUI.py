import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title('Python GUI')


aLabel = ttk.Label(window, text="A Labal")
aLabel.grid(column=0, row=0)

def clickMe():
    action.configure(text='Hello ' + name.get() + ' ' + numberChosen.get())
ttk.Label(window, text="Enter a name:").grid(column=0, row=0)

name = tk.StringVar()
nameEntered = ttk.Entry(window, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

action = ttk.Button(window, text="Click Me", command = clickMe)
action.grid(column=2, row=1)

ttk.Label(window, text="Choose a number: ").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(window, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 3, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(window, text='UnChecked', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(window, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W) #sticky = tk.W means stuck to the west (left), it is a positional setting

chVarEn = tk.IntVar()
check3=tk.Checkbutton(window, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

colors = ["Blue", "Gold","Red"]

def radCall():
    radSel = radVar.get()
    if    radSel == 0: window.configure(background=colors[0])
    elif  radSel == 1: window.configure(background=colors[1])
    elif  radSel == 2: window.configure(background=colors[2])

#Radio buttons example

radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(window, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)

#scrolled text control widget ..

scrolW = 30
ScrolH =  3
src = scrolledtext.ScrolledText(window, width =scrolW, height=ScrolH, wrap=tk.WORD)
src.grid(column=0, columnspan=3)


nameEntered.focus()
window.mainloop()
