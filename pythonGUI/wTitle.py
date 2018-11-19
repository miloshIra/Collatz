import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

window = tk.Tk()

window.title('Python GUI')


# Tab Control introduced here -----------------------------------

tabControl = ttk.Notebook(window)           # Create Tab Control

tab1 = ttk.Frame(tabControl)                # Creat tab
tabControl.add(tab1, text='Tab 1')          # Add the tab

tab2 = ttk.Frame(tabControl)                # Add second tab
tabControl.add(tab2, text='Tab 2')          # Make second tab visible

tabControl.pack(expand=1, fill='both')      # Pack to make visible

# Tab Control introduced here ----------------------------------


# we are creating a contariner frame to hold all other widgets

monty = ttk.LabelFrame(tab1, text = 'Monty')
