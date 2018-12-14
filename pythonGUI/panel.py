import wx

class GUI(wx.Panel):

    def __init__(self, parent):
        wx.Panel__init__(self, parent):

        parent.CreateStatusBar()

        menu = wx.Menu()

        menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "Exit", "Exit the GUI")

        menuBar = wx.MenuBar()

        menuBar.Append(menu,"File")

        button = wx.Button(self, label="Print", pos=(0,60))
        self.Bind(wx.EVT_BUTTON, self.writeToSharedQueue, button)

        self.textBox = wx.TextCtrl(self, size=(280,50), style=wx.TE_MULTILINE)

    def writeToSharedQueue(self, event):

        self.textBox.AppendText("Yea gj retard u clicked")

app = wx.App()
frame = wx.Frame(None, title = "python GUI using wx", size=(300,180))
GUI(Frame)
frame.Show()
app.MainLoop()
