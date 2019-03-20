# import the library
from appJar import gui

# UNICODE
ARROW_LEFT = "\u2190"
ARROW_RIGHT = "\u2192"

# array with img
img = ['cane', 'gatto', 'giraffa', 'leone', 'pecora']
i = 0


# handle button events
def press_animali(button):
    global i
    if button == ARROW_LEFT:
        if i == 0:
            i = 4
        else:
            i = i - 1
    else:
        if i == 4:
            i = 0
        else:
            i = i + 1
    app.reloadImage("image", "../img/{}.gif".format(img[i]))
    app.setLabel('description', '{}'.format(img[i]))


# create a GUI variable called app
app = gui("slider di immagini", "800x400")
app.setFont(18)

# link the buttons to the function called press
app.addButton(ARROW_LEFT, press_animali, 0, 0)
app.addButton(ARROW_RIGHT, press_animali, 0, 2)

# add image
app.addImage("image", "../img/{}.gif".format(img[i]), 0, 1)

# add label with description
app.addLabel("description", "{}".format(img[i]), 1, 1)

# start the GUI
app.go()
