from sqlobject import *

sqlhub.processConnection = connectionForURI('sqlite:Vertragswarner.db')

colnames = [
"kategorie", "bezeichnung", "start_datum", "enddatum", "kuendigungsdatum", "webseite", "nutzername", "passwort"
]
# Kategorie, Bezeichnung, Start-, End- und spätestem Kündigungsdatum, Webseite, Nutzername und Passwort.
class Vertragswarner(SQLObject):
    kategorie = StringCol()
    bezeichnung = StringCol()
    start_datum = DateCol()
    enddatum = DateCol()
    kuendigungsdatum = DateCol()
    webseite = StringCol()
    nutzername = StringCol()
    passwort = StringCol()
    iv = StringCol()

#Vertragswarner(kategorie="a", bezeichnung="b", start_datum="2002-10-10", enddatum="2002-10-10", kuendigungsdatum="2002-10-10",
#               webseite="a", nutzername="b", passwort="c", iv="d")

Vertragswarner.createTable(ifNotExists=True)


def getValues(orderBy):
    values = Vertragswarner.select(orderBy=colnames[orderBy])
    rows = []
    values = list(values)[:8]
    for row in range(0, 8 if len(values) > 8 else len(values)):
        cells = []
        cells.append(values[row].kategorie)
        cells.append(values[row].bezeichnung)
        cells.append(values[row].start_datum.strftime("%Y-%m-%d"))
        cells.append(values[row].enddatum.strftime("%Y-%m-%d"))
        cells.append(values[row].kuendigungsdatum.strftime("%Y-%m-%d"))
        cells.append(values[row].webseite)
        cells.append(values[row].nutzername)
        cells.append(values[row].passwort)
        cells.append(values[row].id)
        rows.append(cells)
    return rows
