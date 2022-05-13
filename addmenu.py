import wx
import wx.xrc

import errorfenster
import sqldb
import datetime


class AddFrame(wx.Frame):
"""Creates the GUI for adding data. Ekrem"""
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Vertragsverwaltung", pos=wx.DefaultPosition,
                          size=wx.Size(506, 359), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.kategorie = wx.StaticText(self, wx.ID_ANY, u"Kategorie:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.kategorie.Wrap(-1)

        self.kategorie.SetFont(
            wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer9.Add(self.kategorie, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.m_textCtrl6, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer12 = wx.BoxSizer(wx.HORIZONTAL)

        self.bezeichnung = wx.StaticText(self, wx.ID_ANY, u"Bezeichnung:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bezeichnung.Wrap(-1)

        self.bezeichnung.SetFont(
            wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer12.Add(self.bezeichnung, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl7 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer12.Add(self.m_textCtrl7, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add(bSizer12, 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

        self.startdatum = wx.StaticText(self, wx.ID_ANY, u"Startdatum:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.startdatum.Wrap(-1)

        self.startdatum.SetFont(
            wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer13.Add(self.startdatum, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl8 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_textCtrl8, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.enddatum = wx.StaticText(self, wx.ID_ANY, u"Enddatum:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.enddatum.Wrap(-1)

        self.enddatum.SetFont(
            wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer14.Add(self.enddatum, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl9 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer14.Add(self.m_textCtrl9, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer15 = wx.BoxSizer(wx.HORIZONTAL)

        self.kuendigungsdatum = wx.StaticText(self, wx.ID_ANY, u"Letztes Kündigungsdatum:", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.kuendigungsdatum.Wrap(-1)

        self.kuendigungsdatum.SetFont(
            wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer15.Add(self.kuendigungsdatum, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl10 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer15.Add(self.m_textCtrl10, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add(bSizer15, 1, wx.EXPAND, 5)

        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

        self.webseite = wx.StaticText(self, wx.ID_ANY, u"Webseite:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.webseite.Wrap(-1)

        self.webseite.SetFont(
            wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer19.Add(self.webseite, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl11 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer19.Add(self.m_textCtrl11, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add(bSizer19, 1, wx.EXPAND, 5)

        bSizer20 = wx.BoxSizer(wx.HORIZONTAL)

        self.nutzername = wx.StaticText(self, wx.ID_ANY, u"Nutzername:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.nutzername.Wrap(-1)

        self.nutzername.SetFont(
            wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer20.Add(self.nutzername, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl12 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer20.Add(self.m_textCtrl12, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add(bSizer20, 1, wx.EXPAND, 5)

        bSizer21 = wx.BoxSizer(wx.HORIZONTAL)

        self.passwort = wx.StaticText(self, wx.ID_ANY, u"Passwort:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.passwort.Wrap(-1)

        self.passwort.SetFont(
            wx.Font(10, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer21.Add(self.passwort, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textCtrl13 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TE_PASSWORD)
        bSizer21.Add(self.m_textCtrl13, 1, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer2.Add(bSizer21, 1, wx.EXPAND, 5)

        bSizer23 = wx.BoxSizer(wx.VERTICAL)

        self.add_button = wx.Button(self, wx.ID_ANY, u"Hinzufügen", wx.DefaultPosition, wx.DefaultSize, 0)
        self.add_button.SetFont(
            wx.Font(20, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        bSizer23.Add(self.add_button, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        bSizer2.Add(bSizer23, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)
        self.add_button.Bind(wx.EVT_BUTTON, self.onSubmit)

    def onSubmit(self, event):
        """Submits entered values to database. Christian"""
        values = [self.m_textCtrl6.GetValue(), self.m_textCtrl7.GetValue(), self.m_textCtrl8.GetValue(),
                  self.m_textCtrl9.GetValue(),
                  self.m_textCtrl10.GetValue(), self.m_textCtrl11.GetValue(),
                  self.m_textCtrl12.GetValue(), self.m_textCtrl13.GetValue()]
        try:
            datetime.datetime.strptime(self.m_textCtrl8.GetValue(), "%Y-%m-%d")
            datetime.datetime.strptime(self.m_textCtrl9.GetValue(), "%Y-%m-%d")
            datetime.datetime.strptime(self.m_textCtrl10.GetValue(), "%Y-%m-%d")
            sqldb.add(values)
            self.Close()
        except ValueError:
            self.wrongFormatWarning()

    def wrongFormatWarning(self):
        """Shows warning that entered date is in wrong format. Christian"""
        errorfenster.Dialogerror(None).Show()

    def __del__(self):
        pass
