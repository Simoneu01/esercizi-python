from appJar import gui
import webbrowser

a = ''
salvato = False

def menupress(button):
    global a,salvato
    if button == 'Esci':
        app.stop()
        salvato = False
    elif button == 'Informazioni su PyNotepad':
        app.startSubWindow("info", "Informazioni su PyNotepad")
        app.addLabel("l1", "Informazioni su PyNotepad")
        app.addLabel("l3", "Esercizio di Informatica\nClasse 4B INF ITT Ettore Molinari")
        app.addLabel('l2', "Code by Simone Ungaro && Davide Grossi")
        app.stopSubWindow()
        app.showSubWindow('info')
    elif button == 'Guida':
        webbrowser.open('https://github.com/Simoneu01/esercizi-python')
    elif button == 'Apri..':
        app.clearTextArea('t1')
        a = app.openBox(fileTypes = [('Documenti di Testo', '*.txt'), ('Tutti i file', '*.*')])
        b = open(a, 'r')
        c = a.split("/")
        app.setTitle(str(c[-1]) + ' - PyNotepad')
        app.setTextArea("t1", b.readlines(), end = True)
        b.close()
        salvato = True
    elif button == 'Nuovo':
        if not salvato:
            print('NOT SALVATO')
            if app.getTextArea('t1'):
                if app.questionBox("NON SALVATO", "Salvare le modifiche?"):
                    menupress('Salva')
                    app.clearTextArea('t1')
                    app.setTitle('Senza nome - PyNotepad')
                else:
                    app.clearTextArea('t1')
                    app.setTitle('Senza nome - PyNotepad')
        elif salvato:
            print('SALVATO')
            app.clearTextArea('t1')
            app.setTitle('Senza nome - Notepad Python')
        else:
            print('ERRORE')
            app.questionBox("ERRORE", "ERRORE")


    elif button == 'Salva':
        try:
            b = open(a, 'w')
            b.writelines(app.getTextArea('t1'))
            b.close()
            salvato = True
        except:
            a = app.saveBox(fileTypes = [('Documenti di Testo', '*.txt'), ('Tutti i file', '*.*')])
            b = open(a, 'w')
            b.writelines(app.getTextArea('t1'))
            b.close()
            c = a.split("/")
            app.setTitle(str(c[-1]) + ' - PyNotepad')
            salvato = True
    elif button == "Salva con nome...":
        a = app.saveBox(fileTypes=[('Documenti di Testo', '*.txt'), ('Tutti i file', '*.*')])
        b = open(a, 'w')
        b.writelines(app.getTextArea('t1'))
        b.close()
        c = a.split("/")
        app.setTitle(str(c[-1]) + ' - PyNotepad')
        salvato = True
    else:
        pass


def keypress(key):
    if key == "<Control_L>" + "<S>" or "<Control_L>" + "<s>":
        menupress('Salva')
    elif key == "<Control_L>" + "<N>" or "<Control_L>" + "<n>":
        menupress('Nuovo')
    elif key == "<Control_L>" + "<O>" or "<Control_L>" + "<o>":
        menupress('Apri..')
    else:
        pass

app = gui("Senza nome - PyNotepad", "800x400")
app.addScrolledTextArea("t1")
app.setTextAreaWidth("t1", 50)
app.setTextAreaHeight("t1", 10)
fileMenus = ["Nuovo", "Apri..", "Salva", "Salva con nome...", "-", "Esci"]
fileMenus2 = ['Guida', 'Informazioni su PyNotepad']
app.addMenuList("File", fileMenus, menupress)
app.addMenuList("Aiuto", ["Aiuto", "Informazioni su AppJar"], [app.appJarHelp, app.appJarAbout])
app.addMenuList("?", fileMenus2, menupress)
app.bindKeys(["<Control_L>" + "<S>", "<Control_L>" + "<s>"], keypress)
app.bindKeys(["<Control_L>" + "<N>", "<Control_L>" + "<n>"], keypress)
app.bindKeys(["<Control_L>" + "<O>", "<Control_L>" + "<o>"], keypress)

# start the GUI
app.go()
