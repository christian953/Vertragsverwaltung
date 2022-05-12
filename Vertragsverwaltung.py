from Hauptmenu import Hauptname_frame
import wx

masterPassword = "123"
app = wx.App()
hauptmenuFrame = Hauptname_frame(None)
hauptmenuFrame.Show()
app.MainLoop()
