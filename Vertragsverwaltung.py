from MasterPasswort import MasterPasswordFrame
from Hauptmenu import Hauptname_frame
from addmenu import AddFrame
import wx



masterPassword = "123"
app = wx.App()
masterPasswordPanel = MasterPasswordFrame(None, masterPassword)
addFrame = AddFrame(None)
addFrame.Show()
hauptmenuFrame = Hauptname_frame(None)
hauptmenuFrame.Show()
app.MainLoop()
