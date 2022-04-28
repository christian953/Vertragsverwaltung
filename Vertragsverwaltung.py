from MasterPasswort import MasterPasswordFrame
from Hauptmenu import Hauptname_frame
import wx



masterPassword = "123"
app = wx.App()
masterPasswordPanel = MasterPasswordFrame(None, masterPassword)
hauptmenuFrame = Hauptname_frame(None)
hauptmenuFrame.Show()
# masterPasswordPanel.Show()
app.MainLoop()
