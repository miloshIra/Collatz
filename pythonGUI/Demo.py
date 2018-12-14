import wx


class GUI(wx.Frame):

    def __init__(self, parent, title, size=(200,100)):

        wx.Frame.__init__(self,parent, title=title, size=size)
        self.SetBackgroundColour('white')
        self.CreateStatusBar()
        menu = wx.Menu()

        menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "Exit", "Exit GUI")

        menuBar = wx.MenuBar()
        menuBar.Append(menu, "File")

        self.SetMenuBar(menuBar)
        self.Show()
        
app = wx.App()

GUI(None, "Python GUI using wxPython", (300,150))

# frame = wx.Frame(None, -1, "Practise..")
# frame.Show()

app.MainLoop()
