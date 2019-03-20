# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Febbraio 11/02/2019 11:16
# Created with PyCharm
# Project: GUI
# import the library
from appJar import gui


# handle button events
def press(button):
    if button == "Esci":
        app.stop()
    elif button == "Pulisci":
        app.clearAllEntries()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)


# create a GUI variable called app
app = gui("Login", "800x400")
app.setBg("orange")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Login")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabelEntry("Username")
app.addLabelEntry("Password")

# link the buttons to the function called press
app.addButtons(["Login", "Pulisci", "Esci"], press)

app.setFocus("Username")

# start the GUI
app.go()
