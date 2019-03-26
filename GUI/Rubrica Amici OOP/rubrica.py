# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Marzo 20/03/2019 20:30
# Created with PyCharm
# Project: Rubrica Amici OOP

from appJar import gui
import time
cercati=[]
# OOP
class Rubrica(object):
    def __init__(self, lista):
        self.rubrica = []
        for i in lista:
            self.rubrica.append(Persona(i))

    def aggiungi(self, lista):
        self.rubrica.append(Persona(lista))

    def elimina(self, id_rubrica):
        self.rubrica.pop(id_rubrica)


class Persona(object):
    def __init__(self, lista):
        self.nome = lista[0]
        self.cognome = lista[1]
        self.telefono = lista[2]
        self.email = lista[3]
        self.categoria = lista[4]

    def modifica(self, lista):
        self.nome = lista[0]
        self.cognome = lista[1]
        self.telefono = lista[2]
        self.email = lista[3]
        self.categoria = lista[4]

    def get(self):
        get_lista = []
        get_lista.append(self.nome)
        get_lista.append(self.cognome)
        get_lista.append(self.telefono)
        get_lista.append(self.email)
        get_lista.append(self.categoria)
        return get_lista

# GUI
def modifica():
    print('modifica')

# function to confirm logout
def logoutFunction():
    return app.yesNoBox("Confirm Exit", "Are you sure you want to exit?")


def aggiungi():
    app.addTableRow('g1', app.getTableEntries('g1'))
    print(app.getTableEntries('g1'))
    with open('amici.txt', 'a+') as f:
        for i in app.getTableEntries('g1'):
            f.writelines(i+',')


def gen_list_from_txt(nome_file, sep=';', header=0, delete_chars='\n'):
    with open(nome_file) as f:
        data = [record.split(sep) for record in f.readlines()[header:]]
        for record in range(len(data)):
            try:
                data[record].remove(delete_chars)
            except:
                pass
        return data


# Rende una lista di liste una unica lista
def flat(lista):
    return [j for i in lista for j in i]


def press(button):
    if button == 'Aggiungi':
        app.showSubWindow('crea_contatto')
    elif button == 'Salva':
        creaContatto()
        app.show()
        prova = []
        for i in range(len(rubrica.rubrica)):
            prova.append(rubrica.rubrica[i].get())

        app.openScrollPane('rubrica')
        for i in range(len(prova)):
            try:
                app.addLabel('a' + str(i), prova[i][0], i, 0)
            except:
                app.setLabel('a' + str(i), prova[i][0])
            try:
                app.addLabel('b' + str(i), prova[i][1], i, 1)
            except:
                app.setLabel('b' + str(i), prova[i][1])
            try:
                app.addLabel('c' + str(i), prova[i][2], i, 2)
            except:
                app.setLabel('c' + str(i), prova[i][2])
            try:
                app.addLabel('d' + str(i), prova[i][3], i, 3)
            except:
                app.setLabel('d' + str(i), prova[i][3])
            try:
                app.addLabel('e' + str(i), prova[i][4], i, 4)
            except:
                app.setLabel('e' + str(i), prova[i][4])
        app.stopScrollPane()
    elif button == 'Pulisci':
        app.clearAllEntries()
    elif button == 'Cerca':
        print(app.getEntry('Search'))

def creaContatto():
    global rubrica
    new_lista = []
    new_lista.append(app.getEntry('Nome'))
    new_lista.append(app.getEntry('Cognome'))
    new_lista.append(app.getEntry('Telefono'))
    new_lista.append(app.getEntry('E-Mail'))
    new_lista.append(app.getEntry('Categoria'))
    print(new_lista)
    if new_lista[0] == '' or new_lista[2] == '':
        app.retryBox('Errore', 'Inserisci i campi obbligatori (*)', parent='crea_contatto')
    else:
        rubrica.aggiungi(new_lista)
        app.clearAllEntries()
        app.hideSubWindow('crea_contatto')


def showTime():
    app.setStatusbar(time.strftime("%X"))

def keyPress(key):
    global cercati
    if key == '<Enter>':
        for x in rubrica.rubrica:
            if app.getEntry('Search') in x.get():
                cercati.append(x)
    return cercati
# Crea oggetto Rubrica
rubrica = Rubrica(gen_list_from_txt('amici.txt', ',', 1))

# GUI
with gui("PyRubrica", "800x600") as app:
    app.setFont(18)
    # add a statusbar to show the time
    app.addStatusbar(side="RIGHT")
    app.registerEvent(showTime)
    app.stopFunction = logoutFunction
    app.addMenuList("?", ["Aiuto", "Informazioni su PyRubrica"], [app.appJarHelp, app.appJarAbout])
    app.label('l1', "Benvenuto sulla PyRubrica")
    words = []
    for i in rubrica.rubrica:
        words.append(i.get()[0] + ' ' + i.get()[1])
    app.addAutoEntry('Search', words)
    app.addButton('Cerca', press)
    print(app.bindKey('<Enter>', keyPress))
    app.addButton('Aggiungi', press)
    app.setLabelBg("l1", "red")
    prova = gen_list_from_txt('amici.txt', ',', 1)
    app.startScrollPane('rubrica')
    for i in range(len(prova)):
        app.addLabel('a' + str(i), prova[i][0], i, 0)
        app.addLabel('b' + str(i), prova[i][1], i, 1)
        app.addLabel('c' + str(i), prova[i][2], i, 2)
        app.addLabel('d' + str(i), prova[i][3], i, 3)
        app.addLabel('e' + str(i), prova[i][4], i, 4)
    app.stopScrollPane()

    app.startSubWindow('crea_contatto', 'Crea Contatto', modal=True)
    app.setSize('450x300')
    app.setBg('yellow')
    app.addLabel('nome', 'Nome *', 0, 0)
    app.addEntry('Nome', 0, 1)
    app.addLabel('cognome','Cognome', 1, 0)
    app.addEntry('Cognome', 1, 1)
    app.addLabel('telefono', 'Telefono *', 2, 0)
    app.addEntry('Telefono', 2, 1)
    app.addLabel('e-Mail', 'E-mail', 3, 0)
    app.addEntry('E-Mail', 3, 1)
    app.addLabel('categoria','Categoria', 4, 0)
    app.addEntry('Categoria', 4, 1)
    app.addButtons(['Pulisci', 'Salva'], press, 5,1)
    app.stopSubWindow()

