import MasterPasswort
import wx

app = wx.App()
masterPasswordFrame = MasterPasswort.MasterPasswordFrame(None)
masterPasswordFrame.Show()
app.MainLoop()
