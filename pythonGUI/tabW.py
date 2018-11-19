import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Python GUI")

tabControl = ttk.Notebook(window)        # Create tab control
tab1 = ttk.Frame(tabControl)             # Create a tab
tabControl.add(tab1, text='Tab 1')       # Add a tab

tab2=ttk.Frame(tabControl)               # Add second tab
tabControl.add(tab2, text='Tab 2')       # Make second tab visible ?

tabControl.pack(expand=1, fill="both")   # Pack to make it visible

Monty = ttk.LabelFrame(tab1, text="Monty")
Monty.grid(column=0, row=0, padx=8, pady=4)
ttk.Label(Monty, text="Enter a name:").grid(column=0, row=0, sticky='W')


window.mainloop()
