from appJar import gui


def press_toolbar(button):
    pass


def menuPress(button):
    if button == 'Esci':
        app.stop()
    elif button == 'Informazioni su File Picker':
        app.startSubWindow("one", modal = True)
        app.addLabel("l1", "SubWindow One")
        app.stopSubWindow()
        app.showSubWindow('one')
    elif button == 'Guida':
        print('Guida')
    elif button == 'Apri..':
        app.clearTextArea('t1')
        a = app.openBox(fileTypes = [('Documenti di Testo', '*.doc'), ('Documenti di Testo', '*.docx'),
                                     ('Documenti di Testo', '*.txt'), ('JPG', '*.jpg'), ('GIF', '*.gif'),
                                     ('Tutti i file', '*.*')], asFile = False)
        b = open(a, 'r')
        app.setTitle(a)
        app.setTextArea("t1", b.readlines(), end = True)
    else:
        pass

def press(button):
    if button == 'Apri':
        app.clearTextArea('t1')
        a = app.openBox(fileTypes = [('Documenti di Testo', '*.doc'), ('Documenti di Testo', '*.docx'), ('Documenti di Testo', '*.txt'), ('JPG', '*.jpg'), ('GIF','*.gif'),('Tutti i file', '*.*')], asFile = False)
        b = open(a, 'r')
        app.setTitle(a)
        app.setTextArea("t1", b.readlines(), end=True)
        app.hideSubWindow("File Picker")
        app.show()
    else:
        app.stop()


app = gui("File Picker", "800x400")
app.addScrolledTextArea("t1")
app.setTextAreaWidth("t1", 50)
app.setTextAreaHeight("t1", 10)
fileMenus = ["Nuovo", "Apri..", "Salva", "Salva con nome...", "-", "Esci"]
fileMenus2 = ['Guida', 'Informazioni su File Picker']
app.addMenuList("File", fileMenus, menuPress)
app.addMenuList("?", fileMenus2, menuPress)

app.startSubWindow("File Picker", modal = True)
app.setSize("800x400")
app.setFont(18)
app.addLabel('File Picker','File Picker',0,0)
app.setLabelBg('File Picker', 'red')
app.addButtons(['Apri', 'Esci'], press, 1,0)
app.stopSubWindow()

# start the GUI
app.go(startWindow="File Picker")
