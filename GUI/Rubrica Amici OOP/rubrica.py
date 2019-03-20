# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Marzo 20/03/2019 20:30
# Created with PyCharm
# Project: Rubrica Amici OOP

from appJar import gui


# OOP
class Persona(object):
    def __init__(self, categorie):
        self.nome = input("Inserisci Nome: ")
        self.cognome = input('Inserisci Cognome: ')
        while True:
            self.telefono = input('Inserisci numero di telefono: ')
            if len(self.telefono) >= 10:
                break
            else:
                print('Inserisci un numero di telefono corretto!')
        self.email = input('Inserisci E-Mail: ')
        while True:
            self.categoria = input("Inserisci Categoria amici: ")
            if self.categoria.upper() in categorie:
                break
            else:
                print('Errore inserisci una Categoria corretta\n')
                print('Categorie Amici disponibili:\n')
                for i, v in categorie.items():
                    print(i + ' = ' + v)

    def modifica(self, categorie):
        self.nome = input("Inserisci Nome: ")
        self.cognome = input('Inserisci Cognome: ')
        while True:
            self.telefono = input('Inserisci numero di telefono: ')
            if len(self.telefono) >= 10:
                break
            else:
                print('Inserisci un numero di telefono corretto!')
        self.email = input('Inserisci E-Mail: ')
        while True:
            self.categoria = input("Inserisci Categoria amici: ")
            if self.categoria.upper() in categorie:
                break
            else:
                print('Errore inserisci una Categoria corretta\n')
                print('Categorie Amici disponibili:\n')
                for i, v in categorie.items():
                    print(i + ' = ' + v)


# GUI
def press():
    print("User:", app.entry("Username"), "Pass:", app.entry("Password"))


def modifica():
    print('modifica')


def aggiungi():
    print('aggiungi')


with gui("Rubrica", "800x600") as app:
    app.label("Benvenuto sulla PyRubrica", bg='blue', fg='orange')
    #app.entry("Nome", label=True, focus=True)
    #app.entry("Password", label=True, secret=True)
    #app.buttons(["Submit", "Cancel"], [press, app.stop])
    app.frame()
    #app.addTable("g1",
    #             [["Nome", "Cognome", "Telefono", "E-mail", "Categoria"],
    #             ["Fred", "Male", "3203204953", "simoneungaro@hotmail.it", "S"],
    ##             ["Tina", "Female", "3203204953", "simoneungaro@hotmail.it", "S"],
    #                 ["Clive", "Male", "3203204953", "simoneungaro@hotmail.it", "S"],
#             ["Betty", "Female", "3203204953", "simoneungaro@hotmail.it", "S"]],
    #             action=modifica, addRow = aggiungi, addButton = 'Modifica',  actionHeading = 'Modifica', border = "raised")
    app.startScrollPane("Table")
    for x in range(10):
        for y in range(10):
            name = str(x) + "-" + str(y)
            app.addLabel(name, name, row = x, column = y)
            app.setLabelBg(name, app.RANDOM_COLOUR())
    app.stopScrollPane()
