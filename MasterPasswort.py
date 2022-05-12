import wx
import wx.xrc


class MasterPasswordFrame(wx.Frame):

    def __init__(self, parent, password):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Vertragsverwaltung", pos=wx.DefaultPosition,
                          size=wx.Size(423, 130), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.masterpassword = password
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(11, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial"))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.ueberschrift = wx.StaticText(self, wx.ID_ANY, u"Bitte geben sie das Masterpasswort ein, um fortzufahren!",
                                          wx.DefaultPosition, wx.DefaultSize,
                                          wx.TE_RICH2 | wx.TE_NO_VSCROLL | wx.TE_MULTILINE | wx.TE_BESTWRAP)
        self.ueberschrift.Wrap(-1)

        self.ueberschrift.SetFont(
            wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Arial"))

        bSizer1.Add(self.ueberschrift, 0, wx.ALL, 5)

        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.mpasswort_ctr = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TE_PASSWORD)
        self.mpasswort_ctr.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))

        bSizer4.Add(self.mpasswort_ctr, 0, wx.ALL | wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.anmelde_button = wx.Button(self, wx.ID_ANY, u"Anmelden", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.anmelde_button, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer4.Add(bSizer5, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer4, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Bind(wx.EVT_BUTTON, self.onSubmit)
        self.Bind(wx.EVT_TEXT_ENTER, self.onSubmit)

    def __del__(self):
        pass

    def onSubmit(self, event):
        submittedPassword = self.mpasswort_ctr.GetValue()
        if submittedPassword != self.masterpassword:
            self.ueberschrift.SetForegroundColour(wx.RED)
            self.ueberschrift.SetLabel(
                "Das Passwort war nicht korrekt.")
        else:
            pass
