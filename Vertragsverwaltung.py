from Hauptmenu import Hauptname_frame
import wx
import MasterPasswort



masterPassword = "123"
app = wx.App()
hauptmenuFrame = Hauptname_frame(None)
hauptmenuFrame.Show()
app.MainLoop()
