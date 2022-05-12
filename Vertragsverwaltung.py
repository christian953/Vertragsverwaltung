import MasterPasswort
from Hauptmenu import Hauptname_frame
import wx

masterPassword = "123456789101"
app = wx.App()
masterPasswordFrame = MasterPasswort.MasterPasswordFrame(None, masterPassword)
masterPasswordFrame.Show()
app.MainLoop()
