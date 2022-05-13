import wx
import wx.xrc

import sqldb


class FrameChangempw(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Vertragsverwaltung", pos=wx.DefaultPosition,
                          size=wx.Size(600, 311), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.parent = parent
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"Masterpasswort", wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        self.m_staticText1.SetFont(
            wx.Font(15, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        bSizer1.Add((0, 0), 2, 0, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"Aktuelles Masterpasswort:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        self.m_staticText8.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer9.Add(self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.textpassword = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(160, -1),
                                        wx.TE_PASSWORD)
        bSizer9.Add(self.textpassword, 1, wx.ALL, 5)

        bSizer7.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer7.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"Neues Masterpasswort:", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        self.m_staticText11.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer10.Add(self.m_staticText11, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.textNewpassword = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                           wx.TE_PASSWORD)
        bSizer10.Add(self.textNewpassword, 1, wx.ALL, 5)

        bSizer7.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText111 = wx.StaticText(self, wx.ID_ANY, u"Masterpasswort bestätigen:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText111.Wrap(-1)

        self.m_staticText111.SetFont(
            wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        bSizer11.Add(self.m_staticText111, 0, wx.ALL, 5)

        self.textnewpassword2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1),
                                            wx.TE_PASSWORD)
        bSizer11.Add(self.textnewpassword2, 1, wx.ALL, 5)

        bSizer7.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer7.Add((0, 0), 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.textnowpasswordinvalid = wx.StaticText(self, wx.ID_ANY,
                                                    u"Ihr aktuelles Masterpasswort, das Sie eingegeben haben, ist falsch!",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.textnowpasswordinvalid.Wrap(-1)

        self.textnowpasswordinvalid.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))
        self.textnowpasswordinvalid.SetForegroundColour(wx.Colour(255, 0, 0))
        self.textnowpasswordinvalid.Hide()

        bSizer13.Add(self.textnowpasswordinvalid, 0, wx.ALL, 5)
        self.textnowpasswordinvalid.Hide()

        self.textnewpasswordinvalid = wx.StaticText(self, wx.ID_ANY,
                                                    u"Ihr neues Masterpasswort, das Sie eingegeben haben, stimmt nicht überein!",
                                                    wx.DefaultPosition, wx.DefaultSize, 0)
        self.textnewpasswordinvalid.Wrap(-1)

        self.textnewpasswordinvalid.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))
        self.textnewpasswordinvalid.SetForegroundColour(wx.Colour(255, 0, 0))

        bSizer13.Add(self.textnewpasswordinvalid, 0, wx.ALL, 5)
        self.textnewpasswordinvalid.Hide()

        bSizer7.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Speichern", wx.DefaultPosition, wx.Size(100, 30), wx.BORDER_NONE)
        self.m_button2.SetFont(
            wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.m_button2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.m_button2.SetBackgroundColour(wx.Colour(108, 154, 4))

        bSizer12.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button21 = wx.Button(self, wx.ID_ANY, u"Abbrechen", wx.DefaultPosition, wx.Size(100, 30),
                                    0 | wx.BORDER_NONE)
        self.m_button21.SetFont(
            wx.Font(8, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))
        self.m_button21.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        self.m_button21.SetBackgroundColour(wx.Colour(171, 171, 171))

        bSizer12.Add(self.m_button21, 0, wx.ALL, 5)

        bSizer7.Add(bSizer12, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_button2.Bind(wx.EVT_BUTTON, self.onSubmit)

        self.Centre(wx.BOTH)


    def onSubmit(self, event):
        """Changes masterpassword in database if entered password is correct and new passwords are identical"""
        if self.textpassword.GetValue() != self.parent.masterPassword:
            self.textnowpasswordinvalid.Show()
        elif self.textNewpassword.GetValue() != self.textnewpassword2.GetValue():
            self.textnewpasswordinvalid.Show()
        else:
            sqldb.updatePassword(self.textNewpassword.GetValue())
            print(sqldb.getPassword())
            self.Close()

    def __del__(self):
        pass
