import wx
import wx.xrc


class DeadlineFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Vertragsverwaltung", pos=wx.DefaultPosition,
                          size=wx.Size(427, 212), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Frist einstellen", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetFont(
            wx.Font(17, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        bSizer1.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Tage:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        self.m_staticText2.SetFont(
            wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer2.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.textdays = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        bSizer2.Add(self.textdays, 0, wx.ALL, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.checkbox = wx.CheckBox(self, wx.ID_ANY, u"Aktivieren/Deaktivieren", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.checkbox, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        bSizer8.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer2.Add(bSizer8, 1, wx.ALIGN_BOTTOM | wx.EXPAND, 5)

        bSizer9.Add(bSizer2, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer9, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
