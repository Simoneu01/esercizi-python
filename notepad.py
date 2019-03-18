from appJar import gui
import webbrowser


a = ''

def menuPress(button):
    global a
    if button == 'Esci':
        app.stop()
    elif button == 'Informazioni su Notepad Python':
        app.startSubWindow("info", "Informazioni su Notepad Python")
        app.addLabel("l1", "Informazioni su Notepad Python")
        app.addLabel('l2', "Code with ❤ by Simone Ungaro")
        app.stopSubWindow()
        app.showSubWindow('info')
    elif button == 'Guida':
        webbrowser.open('https://github.com/Simoneu01/esercizi-python')
    elif button == 'Apri..':
        app.clearTextArea('t1')
        a = app.openBox(fileTypes = [('Documenti di Testo', '*.doc'), ('Documenti di Testo', '*.docx'),
                                     ('Documenti di Testo', '*.txt'), ('Tutti i file', '*.*')], asFile = False)
        b = open(a, 'r')
        app.setTitle(a + ' - Notepad Python')
        app.setTextArea("t1", b.readlines(), end = True)
    elif button == 'Nuovo':
        app.clearTextArea('t1')
        app.setTitle('Nuovo - Notepad Python')
    elif button == 'Salva':
        b = open(a, 'w')
        b.writelines(app.getTextArea('t1'))
    else:
        pass


app = gui("Notepad Python", "800x400")
app.addScrolledTextArea("t1")
app.setTextAreaWidth("t1", 50)
app.setTextAreaHeight("t1", 10)
fileMenus = ["Nuovo", "Apri..", "Salva", "Salva con nome...", "-", "Esci"]
fileMenus2 = ['Guida', 'Informazioni su Notepad Python']
app.addMenuList("File", fileMenus, menuPress)
app.addMenuList("?", fileMenus2, menuPress)

# start the GUI
app.go()
