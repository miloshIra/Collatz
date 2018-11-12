import tkinter as tk
from tkinter import ttk

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
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3=tk.Checkbutton(window, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

nameEntered.focus()

window.mainloop()
# print(type(window))
