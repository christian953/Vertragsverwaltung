import wx
import wx
import wx.xrc
import wx.grid

import Fristfeld
import MasterpasswortChange
import addmenu
import sqldb
import MasterPasswort
import datetime


class Hauptname_frame(wx.Frame):
    """Creates the GUI for main menu. Ekrem"""
    def __init__(self, parent, masterPassword):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Vertragsverwaltung", pos=wx.DefaultPosition,
                          size=wx.Size(1000, 350), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.orderBy = 0
        self.highlight = True
        self.deadLine = 40
        self.masterPassword = masterPassword
        self.tableContents = []
        self.selection = []
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black"))

        self.settings_button = wx.MenuBar(0)
        self.m_menu5 = wx.Menu()
        self.datetime = wx.MenuItem(self.m_menu5, wx.ID_ANY, u"Frist einstellen", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu5.Append(self.datetime)

        self.passwordButton = self.m_menu5.Append(wx.ID_ANY, u"Masterpasswort ändern", u"Masterpasswort ändern")

        self.settings_button.Append(self.m_menu5, u"Einstellungen")

        self.SetMenuBar(self.settings_button)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.main_grid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE)

        # Grid
        self.main_grid.CreateGrid(8, 8)
        self.main_grid.EnableEditing(True)
        self.main_grid.EnableGridLines(True)
        self.main_grid.EnableDragGridSize(False)
        self.main_grid.SetMargins(0, 0)

        # Headers
        self.main_grid.SetColLabelValue(0, "Kategorie")
        self.main_grid.SetColLabelValue(1, "Bezeichnung")
        self.main_grid.SetColLabelValue(2, "Startdatum")
        self.main_grid.SetColLabelValue(3, "Enddatum")
        self.main_grid.SetColLabelValue(4, "Letztes Kündigungsdatum")
        self.main_grid.SetColLabelValue(5, "Webseite")
        self.main_grid.SetColLabelValue(6, "Nutzername")
        self.main_grid.SetColLabelValue(7, "Passwort")

        # Columns
        self.main_grid.SetColSize(2, 120)
        self.main_grid.SetColSize(3, 120)
        self.main_grid.SetColSize(4, 150)
        self.main_grid.EnableDragColMove(False)
        self.main_grid.EnableDragColSize(True)
        self.main_grid.SetColLabelSize(30)
        self.main_grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.main_grid.SetRowSize(0, 22)
        self.main_grid.SetRowSize(1, 22)
        self.main_grid.SetRowSize(2, 22)
        self.main_grid.SetRowSize(3, 22)
        self.main_grid.SetRowSize(4, 22)
        self.main_grid.EnableDragRowSize(True)
        self.main_grid.SetRowLabelSize(80)
        self.main_grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.main_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer7.Add(self.main_grid, 0, wx.ALL, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.speicher_button = wx.Button(self, wx.ID_ANY, u"Speichern", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer8.Add(self.speicher_button, 0, wx.ALL, 5)

        bSizer9 = wx.BoxSizer(wx.HORIZONTAL)

        self.del_button = wx.Button(self, wx.ID_ANY, u"Löschen", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer9.Add(self.del_button, 0, wx.ALL, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.add_button = wx.Button(self, wx.ID_ANY, u"Hinzufügen", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.add_button, 0, wx.ALL, 5)

        bSizer9.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer8.Add(bSizer9, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer8, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)

        self.fillGrid()
        self.Bind(wx.EVT_MENU, self.showMasterPasswort, self.passwordButton)
        self.Bind(wx.EVT_MENU, self.setDeadLine, self.datetime)
        self.del_button.Bind(wx.EVT_BUTTON, self.onDel)
        self.speicher_button.Bind(wx.EVT_BUTTON, self.onSave)
        self.add_button.Bind(wx.EVT_BUTTON, self.showAddPanel)
        self.main_grid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.onOrder)
        self.Bind(wx.EVT_SET_FOCUS, self.onFocus)

    def clearGrid(self):
        """Empties the entire grid. Christian"""
        for row in range(0, 8):
            for cell in range(0, 8):
                self.main_grid.SetCellValue(row, cell, "")

    def fillGrid(self):
        """Fills the grid with the first 8 rows from the database sorted by last clicked label. Christian"""
        self.clearGrid()
        self.tableContents = sqldb.getValues(self.orderBy)
        for row in range(0, 8 if len(self.tableContents) > 8 else len(self.tableContents)):
            for cell in range(0, 8):
                self.main_grid.SetCellValue(row, cell, self.tableContents[row][cell])
                self.main_grid.SetReadOnly(row, cell, False)
            self.setRowColour(row, wx.BLACK)
            if self.highlight:
                if (datetime.datetime.strptime(self.tableContents[row][4],
                                               "%Y-%m-%d") - datetime.datetime.today()) < datetime.timedelta(
                    days=self.deadLine) and row not in self.selection:
                    self.setRowColour(row, wx.RED)
            if datetime.datetime.strptime(self.tableContents[row][4], "%Y-%m-%d") < datetime.datetime.today() and row not in self.selection:
                self.setRowColour(row, wx.LIGHT_GREY)
        if len(self.tableContents) < 8:
            # Sets empty rows to readonly so rows without database equivalent can't be edited
            for row in range(len(self.tableContents), 8):
                for cell in range(0, 8):
                    self.main_grid.SetReadOnly(row, cell, True)

    def onOrder(self, event):
        """Reorders the grid depending on clicked label or adds row to selection. Christian"""
        if event.GetCol() == -1:  # Checks if number label is clicked for selecting a row or colname label is clicked
            # for sorting
            selectedRow = event.GetRow()
            if selectedRow not in self.selection:
                self.selection.append(event.GetRow())
                self.fillGrid()
                self.setRowColour(selectedRow, wx.BLUE)
                return
            else:
                self.selection.remove(selectedRow)
                self.setRowColour(selectedRow, wx.BLACK)
        else:
            self.orderBy = event.GetCol()
            self.resetSelection()  # Resets selection so selection and view doesn't go out of sync
        self.fillGrid()  # Calls fill grid to update values in grid to new ordering

    def setDeadLine(self, event):
        """Opens window used for setting the deadline and toggling highlighting. Christian"""
        deadLinepanel = Fristfeld.DeadlineFrame(self)
        deadLinepanel.Show()

    def showAddPanel(self, event):
        """Shows panel used for adding new rows to database. Christian"""
        self.addPanel = addmenu.AddFrame(None)
        self.addPanel.Show()

    def onDel(self, event):
        """Deletes selected rows. Christian"""
        for row in self.selection:
            rowid = int(self.tableContents[row][8])
            sqldb.remove(rowid)
        self.fillGrid()
        self.resetSelection()

    def resetSelection(self):
        """Empties list containing selected rows and sets them back to default colour. Christian"""
        for row in self.selection:
            self.setRowColour(row, wx.BLACK)
        self.selection = []

    def onSave(self, event):
        """Saves changes made in grid to database. Christian"""
        for row in range(0, len(self.tableContents) if len(self.tableContents) < 8 else 8):
            sqldb.update(self.tableContents[row][8], self.getCurrenValues()[row])

    def getCurrenValues(self):
        """Returns values currently displayed in Grid as list of lists. Christian"""
        values = []
        for row in range(0, 8):
            cells = []
            for cell in range(0, 8):
                cells.append(self.main_grid.GetCellValue(row, cell))
            values.append(cells)
        return values

    def setRowColour(self, row, colour):
        """Changes font colour of entire row in grid. Christian"""
        for i in range(0, 8):
            self.main_grid.SetCellTextColour(row, i, colour)

    def showMasterPasswort(self, event):
        """Shows panel used for changing masterpassword. Christian"""
        masterPasswortpanel = MasterpasswortChange.FrameChangempw(None)
        masterPasswortpanel.Show()
        masterPasswortpanel.Raise()

    def onFocus(self, event):
        self.fillGrid()
    def __del__(self):
        pass
