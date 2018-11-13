

COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

def radCall():
    radSel = radVar.get()
    if    radSel == 1: window.configure(background=COLOR1)
    elif  radSel == 2: window.configure(background=COLOR2)
    elif  radSel == 3: window.configure(background=COLOR3)

radVar = tk.IntVar()
rad1 = tk.Radiobutton(window, text=COLOR1, variable=radVar, value =1, command=radCall)
rad1.grid(column =0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(window, text=COLOR2, variable=radVar, value =1, command=radCall)
rad2.grid(column =1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(window, text=COLOR3, variable=radVar, value =1, command=radCall)
rad3.grid(column =2, row=5, sticky=tk.W, columnspan=3)

nameEntered.focus()
