from appJar import gui
import webbrowser

a = ''


def menupress(button):
    global a
    if button == 'Esci':
        app.stop()
    elif button == 'Informazioni su Notepad Python':
        app.startSubWindow("info", "Informazioni su Notepad Python")
        app.addLabel("l1", "Informazioni su Notepad Python")
        app.addLabel("l3", "Esercizio di Informatica\nClasse 4B INF ITT Ettore Molinari")
        app.addLabel('l2', "Code by Simone Ungaro")
        app.stopSubWindow()
        app.showSubWindow('info')
    elif button == 'Guida':
        webbrowser.open('https://github.com/Simoneu01/esercizi-python')
    elif button == 'Apri..':
        app.clearTextArea('t1')
        a = app.openBox(fileTypes = [('Documenti di Testo', '*.txt'), ('Tutti i file', '*.*')])
        b = open(a, 'r')
        a = a.split("/")
        app.setTitle(str(a[-1]) + ' - Notepad Python')
        app.setTextArea("t1", b.readlines(), end = True)
    elif button == 'Nuovo':
        app.clearTextArea('t1')
        app.setTitle('Senza nome - Notepad Python')
    elif button == 'Salva':
        b = open(a, 'w')
        b.writelines(app.getTextArea('t1'))
    elif button == "Salva con nome...":
        a = app.saveBox(fileTypes=[('Documenti di Testo', '*.txt'), ('Tutti i file', '*.*')])
        b = open(a, 'w')
        b.writelines(app.getTextArea('t1'))
        a = a.split("/")
        app.setTitle(str(a[-1]) + ' - Notepad Python')
    else:
        pass


app = gui("Senza nome - Notepad Python", "800x400")
app.addScrolledTextArea("t1")
app.setTextAreaWidth("t1", 50)
app.setTextAreaHeight("t1", 10)
fileMenus = ["Nuovo", "Apri..", "Salva", "Salva con nome...", "-", "Esci"]
fileMenus2 = ['Guida', 'Informazioni su Notepad Python']
app.addMenuList("File", fileMenus, menupress)
app.addMenuList("?", fileMenus2, menupress)

# start the GUI
app.go()
