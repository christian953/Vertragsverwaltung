import wx
import wx.xrc


class Dialogerror(wx.Dialog):
    """Creates the GUI for Error warning. Ekrem"""
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"Vertragsverwaltung", pos=wx.DefaultPosition,
                           size=wx.Size(515, 114), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        bSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Die Eingabe ist ungültig, bitte versuchen sie es erneut!",
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        self.m_staticText3.SetFont(
            wx.Font(15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
        self.m_staticText3.SetForegroundColour(wx.Colour(255, 0, 0))

        bSizer11.Add(self.m_staticText3, 1, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer11)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
