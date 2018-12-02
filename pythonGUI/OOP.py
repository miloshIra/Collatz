#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
import OOP_ToolTip as tt
from threading import Thread
import time
from queue import Queue
import Queues as bq


GLOBAL_CONST = 42

#===================================================================
class OOP():
    def __init__(self):
        # Create instance
        self.win = tk.Tk()

        #Create a Queue
        self.guiQueue = Queue()

        tt.createToolTip(self.win, 'Hello GUI.')

        # Add a title
        self.win.title("Python GUI")
        self.createWidgets()

    def createThread(self):
        self.runT = Thread(target=self.useQue)
        self.runT.setDaemon(True)
        self.runT.start()
        print(runT)
        print('createThread():', self.runT.isAlive())

    def useQue(self):

    #     guiQue = Queue() # creating que instance ..
    #     print(guiQue)
    #     for idx in range(10):
    #         guiQue.put('Message in a que: ' + str(idx))

        while True:
            print(self.guiQue.get())

    # Button callback
    def clickMe(self):
        self.action.configure(text='Hello ' + self.name.get())
        # for idx in range(10):
        #     time.sleep(5)
        #     self.scr.insert(tk.INSERT, str(idx) + '\n')
        # self.createThread()
        print(self)
        bq.writeToScrol(self)

    # Spinbox callback
    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scr.insert(tk.INSERT, value + '\n')

    # Checkbox callback
    def checkCallback(self, *ignoredArgs):
        # only enable one checkbutton
        if self.chVarUn.get(): self.check3.configure(state='disabled')
        else:             self.check3.configure(state='normal')
        if self.chVarEn.get(): self.check2.configure(state='disabled')
        else:             self.check2.configure(state='normal')

    # Radiobutton callback function
    def radCall(self):
        radSel=self.radVar.get()
        if   radSel == 0: self.monty2.configure(text='Blue')
        elif radSel == 1: self.monty2.configure(text='Gold')
        elif radSel == 2: self.monty2.configure(text='Red')

    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def methodInAThread(self, numOfLoops=10):
        print('supprise motherfcker ...')
        for idx in range(numOfLoops):
            time.sleep(1)
            self.scr.insert(tk.INSERT, str(idx) + '\n')
            print('methodInAThread():', self.runT.isAlive())
        time.sleep(1)
        print('methodInAThread:', self.runT.isAlive())


    def usingGlobal(self):
        GLOBAL_CONST = 777
        print(GLOBAL_CONST)

    #####################################################################################
    def createWidgets(self):
        # Tab Control introduced here --------------------------------------
        tabControl = ttk.Notebook(self.win)     # Create Tab Control

        tab1 = ttk.Frame(tabControl)            # Create a tab
        tabControl.add(tab1, text='Tab 1')      # Add the tab

        tab2 = ttk.Frame(tabControl)            # Add a second tab
        tabControl.add(tab2, text='Tab 2')      # Make second tab visible

        tabControl.pack(expand=1, fill="both")  # Pack to make visible
        # ~ Tab Control introduced here -----------------------------------------

        # We are creating a container frame to hold all other widgets
        self.monty = ttk.LabelFrame(tab1, text=' Monty Python ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)

        # Changing our Label
        ttk.Label(self.monty, text="Enter a name:").grid(column=0, row=0, sticky='W')

        # Adding a Textbox Entry widget
        self.name = tk.StringVar()
        nameEntered = ttk.Entry(self.monty, width=24, textvariable=self.name)
        nameEntered.grid(column=0, row=1, sticky='W')

        # Adding a Button
        self.action = ttk.Button(self.monty, text="Click Me!", command=self.clickMe)
        self.action.grid(column=2, row=1)

        ttk.Label(self.monty, text="Choose a number:").grid(column=1, row=0)
        number = tk.StringVar()
        numberChosen = ttk.Combobox(self.monty, width=14, textvariable=number)
        numberChosen['values'] = (1, 2, 4, 42, 100)
        numberChosen.grid(column=1, row=1)
        numberChosen.current(0)

        # Adding a Spinbox widget using a set of values
        self.spin = Spinbox(self.monty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=self._spin)
        self.spin.grid(column=0, row=2, sticky='W')

        # Using a scrolled Text control
        scrolW  = 40; scrolH  =  10
        self.scr = scrolledtext.ScrolledText(self.monty, width=scrolW, height=scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)

        # Tab Control 2 refactoring  -----------------------------------------
        # We are creating a container frame to hold all other widgets -- Tab2
        self.monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.monty2.grid(column=0, row=0, padx=8, pady=4)
        # Creating three checkbuttons
        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.monty2, text="Disabled", variable=chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)

        self.chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.monty2, text="UnChecked", variable=self.chVarUn)
        self.check2.deselect()
        self.check2.grid(column=1, row=0, sticky=tk.W )

        self.chVarEn = tk.IntVar()
        self.check3 = tk.Checkbutton(self.monty2, text="Toggle", variable=self.chVarEn)
        self.check3.deselect()
        self.check3.grid(column=2, row=0, sticky=tk.W)



        # trace the state of the two checkbuttons
        self.chVarUn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())
        self.chVarEn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())
        # ~ Tab Control 2 refactoring  -----------------------------------------

        # Radiobutton list
        colors = ["Blue", "Gold", "Red"]

        self.radVar = tk.IntVar()

        # Selecting a non-existing index value for radVar
        self.radVar.set(99)

        # Creating all three Radiobutton widgets within one loop
        for col in range(3):
            curRad = 'rad' + str(col)
            curRad = tk.Radiobutton(self.monty2, text=colors[col], variable=self.radVar, value=col, command=self.radCall)
            curRad.grid(column=col, row=6, sticky=tk.W, columnspan=3)
            # And now adding tooltips
            tt.createToolTip(curRad, 'This is a Radiobutton control.')

        # Create a container to hold labels
        labelsFrame = ttk.LabelFrame(self.monty2, text=' Labels in a Frame ')
        labelsFrame.grid(column=0, row=7)

        # Place labels into the container element - vertically
        ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
        ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)

        # Add some space around each label
        for child in labelsFrame.winfo_children():
            child.grid_configure(padx=6, pady=6)

        def copyFile():
            import shutil
            src = self.fileEntry.get()
            file = src.split('/')[-1]
            dst = self.netwEntry.get() + '\\' + file
            try:
                shutil.copy(src, dst)
                mBox.showinfo('Copy File to Network', 'Succes: File copied.')
            except FileNotFoundError as err:
                mBox.showerror('Copy File to Network', '*** Failed to copy file! *** \n\n\')
            except Exception as ex:
                mBox.showerror('Copy file to network', '*** Failed *** \n\n')

        cb.ttk.Button(mngFilesFrame, text= 'Copy file to:', command = copyFile)
        cb.grid(column=0, row=1, sticky=tk.E)

        # Creating a Menu Bar
        menuBar = Menu(tab1)
        self.win.config(menu=menuBar)

        # Add menu items
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="File", menu=fileMenu)

        # Add another Menu to the Menu Bar and an item
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About")
        menuBar.add_cascade(label="Help", menu=helpMenu)

        # Change the main windows icon
        #self.win.iconbitmap(r'C:\Python34\DLLs\pyc.ico')

        # Using tkinter Variable Classes
        strData = tk.StringVar()
        strData.set('Hello StringVar')
        print(strData.get())

        # Default tkinter Variable Classes
        intData = tk.IntVar()
        print(intData.get())
        print(tk.DoubleVar())
        print(tk.BooleanVar())

        # It is not necessary to create a tk.StringVar()
        strData = tk.StringVar()
        strData = self.spin.get()
        print("Hello " + strData)

        # Printing the Global works
        print(GLOBAL_CONST)

        # call method
        self.usingGlobal()

        # Place cursor into name Entry
        nameEntered.focus()

        # Add a Tooltip to the Spinbox
        tt.createToolTip(self.spin, 'This is a Spin control.')

        # Add Tooltips to more widgets
        tt.createToolTip(nameEntered, 'This is an Entry control.')
        tt.createToolTip(self.action, 'This is a Button control.')
        tt.createToolTip(self.scr,    'This is a ScrolledText control.')

#======================
# Start GUI
#======================
oop = OOP()

#Runnung methods in treads
runT = Thread(target=oop.methodInAThread)

#oop.useQue()
oop.win.mainloop()
