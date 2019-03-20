from appJar import gui
import webbrowser

a = ''
salvato = False

def menupress(button):
    global a,salvato
    if button == 'Esci':
        app.stop()
        salvato = False
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
        c = a.split("/")
        app.setTitle(str(c[-1]) + ' - Notepad Python')
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
                    app.setTitle('Senza nome - Notepad Python')
                else:
                    app.clearTextArea('t1')
                    app.setTitle('Senza nome - Notepad Python')
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
            app.setTitle(str(c[-1]) + ' - Notepad Python')
            salvato = True
    elif button == "Salva con nome...":
        a = app.saveBox(fileTypes=[('Documenti di Testo', '*.txt'), ('Tutti i file', '*.*')])
        b = open(a, 'w')
        b.writelines(app.getTextArea('t1'))
        b.close()
        c = a.split("/")
        app.setTitle(str(c[-1]) + ' - Notepad Python')
        salvato = True
    else:
        pass


def keypress3(key):
    menupress('Apri..')

def keypress2(key):
    menupress('Nuovo')

def keypress1(key):
    menupress('Salva')


app = gui("Senza nome - Notepad Python", "800x400")
app.addScrolledTextArea("t1")
app.setTextAreaWidth("t1", 50)
app.setTextAreaHeight("t1", 10)
fileMenus = ["Nuovo", "Apri..", "Salva", "Salva con nome...", "-", "Esci"]
fileMenus2 = ['Guida', 'Informazioni su Notepad Python']
app.addMenuList("File", fileMenus, menupress)
app.addMenuList("?", fileMenus2, menupress)
app.bindKeys(["<Control_L>" + "<S>", "<Control_L>" + "<s>"], keypress1)
app.bindKeys(["<Control_L>" + "<N>", "<Control_L>" + "<n>"], keypress2)
app.bindKeys(["<Control_L>" + "<O>", "<Control_L>" + "<o>"], keypress3)

# start the GUI
app.go()