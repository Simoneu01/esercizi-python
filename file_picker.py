from appJar import gui

# Genera una lista o lista di liste da un file di testo (non codificato)
def gen_list_from_txt(nome_file, sep=';', header=0, delete_chars='\n', cols=None):
    with open(nome_file) as f:
        if cols is None:
            return [record.replace(delete_chars, '').split(sep) for record in f.readlines()[header:]]
        return [record.replace(delete_chars, '').split(sep)[cols[0]:cols[1]:cols[2]] for record in f.readlines()[header:]]


def press(button):
    if button == 'Apri':
        app.clearTextArea('t1', callFunction = True)
        a = app.openBox(title = None, dirName = None, fileTypes = [('Documenti di Testo', '*.doc'), ('Documenti di Testo', '*.docx'), ('Documenti di Testo', '*.txt'), ('JPG', '*.jpg'), ('GIF','*.gif'),('Tutti i file', '*.*')], asFile = True)
        app.setTextArea("t1", a.readlines(), end=True)
        app.showSubWindow('one')
    else:
        app.stop()


#.openBox(title=None, dirName=None, fileTypes=None, asFile=False, parent=None)
app = gui("File Picker", "800x400")
app.setFont(18)
app.addButtons(['Apri', 'Esci'],press)
app.startSubWindow("one", modal = True)
app.addLabel("l1", "SubWindow One")
app.addTextArea("t1")
app.stopSubWindow()
# start the GUI
app.go()