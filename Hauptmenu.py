import wx
import wx.xrc
import wx.grid
import sqldb


class Hauptname_frame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Hauptmenu", pos=wx.DefaultPosition,
                          size=wx.Size(1000, 350), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.orderBy = 0
        self.tableContents = []
        self.selection = []
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial Black"))

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
        self.main_grid.SetFont(
            wx.Font(2, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))

        bSizer7.Add(self.main_grid, 0, wx.ALL, 5)

        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.del_button = wx.Button(self, 1, u"Löschen", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.del_button, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        self.speicher_button = wx.Button(self, 2, u"Speichern", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.speicher_button, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.masterpw_txt = wx.StaticText(self, wx.ID_ANY, u"Neues-Masterpasswort:", wx.DefaultPosition, wx.DefaultSize,
                                          0)
        # self.masterpw_txt.Wrap(-1)

        bSizer14.Add(self.masterpw_txt, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        bSizer11.Add(bSizer14, 1, wx.EXPAND, 5)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_textCtrl3, 0, wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND, 5)

        bSizer11.Add(bSizer13, 1, wx.EXPAND, 5)

        bSizer10.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer8.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer7.Add(bSizer8, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer7)
        self.Layout()

        self.Centre(wx.BOTH)
        self.fillGrid()
        self.del_button.Bind(wx.EVT_BUTTON, self.onDel)
        self.speicher_button.Bind(wx.EVT_BUTTON, self.onSave)
        self.main_grid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.onOrder)

    def clearGrid(self):
        for row in range(0, 8):
            for cell in range(0, 8):
                self.main_grid.SetCellValue(row, cell, "")

    def fillGrid(self):
        self.clearGrid()
        self.tableContents = sqldb.getValues(self.orderBy)
        for row in range(0, 8 if len(self.tableContents) > 8 else len(self.tableContents)):
            for cell in range(0, 8):
                self.main_grid.SetCellValue(row, cell, self.tableContents[row][cell])
                self.main_grid.SetReadOnly(row,cell,False)
        if len(self.tableContents) < 8:
            for row in range(len(self.tableContents), 8):
                for cell in range(0,8):
                    self.main_grid.SetReadOnly(row,cell,True)

    def onOrder(self, event):
        if event.GetCol() == -1:
            print("0")
            selectedRow = event.GetRow()
            if selectedRow not in self.selection:
                print("1")
                self.selection.append(event.GetRow())
                self.setRowColour(selectedRow, wx.BLUE)
            else:
                print("2")
                self.selection.remove(selectedRow)
                self.setRowColour(selectedRow, wx.BLACK)
        else:
            self.orderBy = event.GetCol()
            self.resetSelection()
        self.fillGrid()

    def onDel(self, event):
        for row in self.selection:
            rowid = int(self.tableContents[row][8])
            sqldb.remove(rowid)
        self.fillGrid()
        self.resetSelection()

    def resetSelection(self):
        for row in self.selection:
            self.setRowColour(row, wx.BLACK)
        self.selection = []

    def onSave(self, event):
        print(self.getCurrenValues())
        for row in range(0, len(self.tableContents) if len(self.tableContents) < 8 else 8):
            sqldb.update(self.tableContents[row][8], self.getCurrenValues()[row])

    def getCurrenValues(self):
        values = []
        for row in range(0, 8):
            cells = []
            for cell in range(0, 8):
                cells.append(self.main_grid.GetCellValue(row, cell))
            values.append(cells)
        return values

    def setRowColour(self, row, colour):
        for i in range(0, 8):
            self.main_grid.SetCellTextColour(row, i, colour)

    def __del__(self):
        pass
