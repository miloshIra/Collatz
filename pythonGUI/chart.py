from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize = (12, 8), facecolor='white')

axis = fig.add_subplot(211)

xValues = [1,2,3,4]
yValues = [5,7,6,8]

axis.plot(xValues, yValues)

axis.set_xlabel('Horizontal label')
axis.set_ylabel('Vertical label')

axis.grid(linestyle='-')

def _destroyWindow():
    root.quit()
    root.destroy()

root= tk.Tk()
root.withdraw()
root.protocol('WM_DELETE_WINDOW', _destroyWindow)
root.mainloop()

canvas = FigureCanvasTkAgg(fig, master=root)
