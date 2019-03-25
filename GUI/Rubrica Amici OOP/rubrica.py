# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Marzo 20/03/2019 20:30
# Created with PyCharm
# Project: Rubrica Amici OOP

from appJar import gui
import time

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


li = gen_list_from_txt('amici.txt', ',', 1)
rubrica = Rubrica(li)


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


def creaContatto():
    global rubrica
    new_lista = []
    new_lista.append(app.getEntry('Nome'))
    new_lista.append(app.getEntry('Cognome'))
    new_lista.append(app.getEntry('Telefono'))
    new_lista.append(app.getEntry('E-Mail'))
    new_lista.append(app.getEntry('Categoria'))
    print(new_lista)
    if new_lista == ['','','','','']:
        pass
    else:
        rubrica.aggiungi(new_lista)


def showTime():
    app.setStatusbar(time.strftime("%X"))


with gui("PyRubrica", "800x600") as app:
    # add a statusbar to show the time
    app.addStatusbar(side="RIGHT")
    app.registerEvent(showTime)
    app.stopFunction = logoutFunction
    app.addMenuList("?", ["Aiuto", "Informazioni su PyRubrica"], [app.appJarHelp, app.appJarAbout])
    app.label('l1', "Benvenuto sulla PyRubrica")
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
    app.startSubWindow('crea_contatto', modal=True)
    app.setBg('yellow')
    app.setFont(22)
    app.addLabel('title', 'Crea nuovo Contatto')
    app.setLabelBg('title', 'green')
    app.addLabelEntry('Nome')
    app.addLabelEntry('Cognome')
    app.addLabelEntry('Telefono')
    app.addLabelEntry('E-Mail')
    app.addLabelEntry('Categoria')
    app.addButton('Salva', press)
    app.stopSubWindow()

