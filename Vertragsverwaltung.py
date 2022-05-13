import MasterPasswort
import sqldb
from Hauptmenu import Hauptname_frame
import wx

sqldb.checkTables()
masterPassword = sqldb.getPassword()
app = wx.App()
masterPasswordFrame = MasterPasswort.MasterPasswordFrame(None, masterPassword)
masterPasswordFrame.Show()
app.MainLoop()
