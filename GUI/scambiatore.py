# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Febbraio 12/02/2019 10:16
# Created with PyCharm
# Project: GUI

from appJar import gui

ARROW = "\u21F5"


def press(button):
    if button == "Esci":
        app.stop()
    elif button == "Pulisci":
        app.clearAllEntries()
    else:
        for i in range(6):
            temp = app.getEntry('first'+str(i))
            app.setEntry('first'+str(i), app.getEntry('second'+str(i)))
            app.setEntry('second'+str(i), temp)


with gui('SCAMBIATORE', '600x300') as app:
    app.addLabel("Scambiatore")
    app.startPanedFrameVertical("frame1")
    for i in range(6):
        app.addEntry("first"+str(i), 0, i)
        app.addLabel("arrow"+str(i), ARROW, 1, i)
        app.addEntry("second"+str(i), 2, i)
    app.startPanedFrame("frame2")
    app.addButtons(["Scambia", "Pulisci"], press)
    app.setSticky("se")
    app.addButton("Esci", press)
    app.stopAllPanedFrames()
