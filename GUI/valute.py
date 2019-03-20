# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Febbraio 26/02/2019 11:27
# Created with PyCharm
# Project: GUI

from appJar import gui

DOLLARO = "\u0024"
STERLINA = "\u00A3"
BITCOIN = "\u20BF"
EURO = "\u20AC"

def press(button):
    value_dollar = 1.14
    valie_pound = 0.86
    value_bitcoin = 0.00030
    if button == "Esci":
        app.stop()
    elif button == "Pulisci":
        app.clearAllEntries()
        app.clearLabel("DOLLARO")
        app.clearLabel("STERLINA")
        app.clearLabel("BITCOIN")
    elif button == DOLLARO:
        app.setLabel("DOLLARO", app.getEntry("INSERISCI") * float(value_dollar))
    elif button == STERLINA:
        app.setLabel("STERLINA", app.getEntry("INSERISCI") * float(valie_pound))
    elif button == BITCOIN:
        app.setLabel("BITCOIN", app.getEntry("INSERISCI") * float(value_bitcoin))
    else:
        pass


with gui('VALUTE', '600x300') as app:
    app.addLabel("VALUTE")

    app.startFrame("TOP")
    app.addNumericEntry('INSERISCI', 0, 0)
    app.addEmptyLabel("DOLLARO", 1, 0)
    app.setLabelBg("DOLLARO", "white")
    app.addEmptyLabel("STERLINA", 2, 0)
    app.setLabelBg("STERLINA", "white")
    app.addEmptyLabel("BITCOIN", 3, 0)
    app.setLabelBg("BITCOIN", "white")
    app.addButton(DOLLARO, press, 1, 1)
    app.addButton(STERLINA, press, 2, 1)
    app.addButton(BITCOIN, press, 3, 1)
    app.addLabel("EURO", EURO, 0, 1)
    app.stopFrame()

    app.startFrame("BOTTTOM")
    app.addButton("Pulisci", press)
    app.setSticky("se")
    app.addButton("Esci", press)
    app.stopFrame()
