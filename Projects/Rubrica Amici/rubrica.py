# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Febbraio 04/02/2019 11:12
# Created with PyCharm
# Project: Rubrica Amici


"""Fare l'analisi e scrivere uno script python che permetta di registrare nel file di testo "amici.txt" il nome e
cognome degli amici, il numero di telefono, l'email, la categoria dell'amico. Per categoria dell'amico/a si intende:
S se l'amico/a è un compagno di studio D se l'amico/a è un compagno di danza G se l'amico/a è un compagno di giochi C
se l'amico/a è il compagno del cuore. Le categorie sono registrate nel file di testo "categorie_amici.txt". Creare
poi un menu che permetta di: 1) inserire nuovi amici 2) inserire nuove categorie 3) estrarre gli amici di una
determinata categoria 4) estrarre un amico in base al nome 5) correggere i dati di un amico (in caso di cambio di
telefono, email o categoria)

"""

# IMPORT
import datetime
import os
from repo import *

# VARIABILI GLOBALI
presets = dict(S = 'Compagno di Studio', D = 'Compagno di Danza', G = 'Compagno di Giochi', C = 'Compagno di Cuore')
versione = '1.0.5'
nfile_categorie_amici = 'categorie_amici.txt'
nfile_rubrica_amici = 'amici.txt'


# FUNZIONI
def estrai_nome():
    trovato = False
    with open(nfile_rubrica_amici) as f:
        next(f)
        nome_scelto = input("Inserisci Nome: ")
        for line in f:
            nome, cognome, numero_telefono, email, categoria, n = line.split(',')
            if nome_scelto == nome:
                print(nome, cognome, numero_telefono, email, categoria)
                trovato = True
        if not trovato:
            print('Non è stato trovato nessuno\n')
    menu()


def estrai_categoria():
    trovato = False
    tmp_presets = dict_categorie(nfile_categorie_amici)
    with open(nfile_rubrica_amici) as f:
        next(f)
        while True:
            categoria_scelta = input("Inserisci Categoria amici: ")
            if categoria_scelta.upper() in tmp_presets:
                break
            else:
                print('Errore inserisci una Categoria corretta\n')
                print('Categorie Amici disponibili:\n')
                for i, v in tmp_presets.items():
                    print(i + ' = ' + v)
        for line in f:
            nome, cognome, numero_telefono, email, categoria, n = line.split(',')
            if categoria_scelta == categoria:
                print(nome, cognome, numero_telefono, email, categoria)
                trovato = True
        if not trovato:
            print('Non è stato trovato nessuno\n')
    menu()


# FUNZIONI PER VENDITE
def menu_amici():
    if os.path.isfile(nfile_categorie_amici):
        if os.path.isfile(nfile_rubrica_amici):
            print('!!!ATTENZIONE!!!!!\nFile {} trovato\nCome desideri procedere?\n'.format(nfile_rubrica_amici))
            print('****MENU AMICI****')
            x = input('1. Sovrascrivere file\n2. Aggiungere amico\n3.Correggi dati\n4. Annulla / Torna al menu '
                      'principale\n>>> ')
            if x == '1':
                creazione_amici()
                menu()
            elif x == '2':
                creazione_amici(False)
                menu()
            elif x == '3':
                correggi_dati()
            elif x == '4':
                menu()
            else:
                print('Errore')
                menu_amici()
        else:
            print('File {} non trovato!!!!!\nCreazione in corso...\n'.format(nfile_rubrica_amici))
            creazione_amici()
            menu()
    else:
        print('File {} non trovato!!!\n'.format(nfile_categorie_amici))
        print('Devi prima creare il file "{}"'.format(nfile_categorie_amici))
        menu()


def creazione_amici(sovrascrivi = True):
    tmp_presets = dict_categorie(nfile_categorie_amici)
    if sovrascrivi:
        with open(nfile_rubrica_amici, 'w') as f:
            f.writelines('Nome,Cognome,Numero di telefono,E-mail,Categoria Amico,\n')
    with open(nfile_rubrica_amici, 'a+') as f:
        while True:
            nome = input("Inserisci Nome: ")
            cognome = input('Inserisci Cognome: ')
            while True:
                numero_telefono = input('Inserisci numero di telefono: ')
                if len(numero_telefono) >= 10:
                    break
                else:
                    print('Inserisci un numero di telefono corretto!')
            email = input('Inserisci E-Mail: ')
            while True:
                categoria = input("Inserisci Categoria amici: ")
                if categoria.upper() in tmp_presets:
                    break
                else:
                    print('Errore inserisci una Categoria corretta\n')
                    print('Categorie Amici disponibili:\n')
                    for i, v in tmp_presets.items():
                        print(i + ' = ' + v)
            f.writelines('{0},{1},{2},{3},{4},\n'.format(nome, cognome, numero_telefono, email, categoria))
            if input('\nScrivi fine per terminare.....\n>>> ') == 'fine':
                break


# FUNZIONI PER CORREGGE
def correggi_dati():
    d = {}
    tmp_presets = dict_categorie(nfile_categorie_amici)
    with open(nfile_rubrica_amici) as f:
        next(f)
        cont = 1
        for line in f:
            nome, cognome, telefono, email, categoria, n = line.split(',')
            d[cont] = [nome, cognome, telefono, email, categoria]
            cont = cont+1
        for x, y in d.items():
            print(str(x), '=', y)
        x = int(input('Quale amico vuoi modificare? Inserisci numero\n>>>'))
        new_nome = input("Inserisci Nome: ")
        new_cognome = input('Inserisci Cognome: ')
        while True:
            new_numero_telefono = input('Inserisci numero di telefono: ')
            if len(new_numero_telefono) >= 10:
                break
            else:
                print('Inserisci un numero di telefono corretto!')
        new_email = input('Inserisci E-Mail: ')
        while True:
            new_categoria = input("Inserisci Categoria amici: ")
            if new_categoria.upper() in tmp_presets:
                break
            else:
                print('Errore inserisci una Categoria corretta\n')
                print('Categorie Amici disponibili:\n')
                for i, v in tmp_presets.items():
                    print(i + ' = ' + v)
        d[x] = [new_nome, new_cognome, new_numero_telefono, new_email, new_categoria]
        lista_new = []
        for i in d.keys():
            lista_new.append(','.join(d[i])+',\n')
    with open(nfile_rubrica_amici) as f:
        f.writelines('Nome,Cognome,Numero di telefono,E-mail,Categoria Amico,\n')
        f.writelines(lista_new)
    menu()


# FUNZIONI PER CATEGORIE
def menu_categorie():
    if os.path.isfile(nfile_categorie_amici):
        print('!!!ATTENZIONE!!!!!\nFile {} trovato\nCome desideri procedere?\n'.format(nfile_categorie_amici))
        print('Categorie Amici trovati nel file:\n')
        for i, v in dict_categorie(nfile_categorie_amici).items():
            print(i + ' = ' + v)
        print('\n****MENU CATEGORIE AMICI****')
        x = input('1. Sovrascrivere file\n2. Aggiungere categorie amici\n3. Modifica Categoria esistente\n4. Annulla '
                  '/ Torna al menu principale\n>>> ')
        if x == '1':
            creazione_categorie()
            menu()
        elif x == '2':
            creazione_categorie(False)
            menu()
        elif x == '3':
            edit_categorie()
        elif x == '4':
            menu()
        else:
            print('Errore')
            menu_categorie()
    else:
        print('File {} non trovato\nCreazione File...\n'.format(nfile_categorie_amici))
        creazione_categorie()
        menu()


def creazione_categorie(sovrascrivi = True):
    tmp_presets = presets if sovrascrivi else {}
    with open(nfile_categorie_amici, 'w' if sovrascrivi else 'a+') as f:
        if sovrascrivi:
            print('Categorie Amici base:\n')
            for i, v in presets.items():
                print(i + ' = ' + v)
            f.writelines('Categorie Amici,Descrizione,\n')
        a = input('Vuoi aggiungere categorie amici? [SI/NO]\n>>>') if sovrascrivi else 'SI'
        if a.upper() == 'SI' or a.upper() == 'YES':
            while True:
                categoria = input("Inserisci Categoria Amici: ")
                descrizione = input("Inserisci la descrizione della categoria {}: ".format(categoria.upper()))
                tmp_presets[categoria.upper()] = descrizione
                if input('\nScrivi fine per terminare.....\n>>> ').lower() == 'fine':
                    break
        for x, y in tmp_presets.items():
            f.writelines(x + ',' + y + ',\n')


def edit_categorie():
    tmp_preset = list(dict_categorie(nfile_categorie_amici,).items())
    print('Categorie Amici trovati nel file:\n')
    for i, v in tmp_preset:
        print(i + ' = ' + v)
    x = input('Quale categoria vuoi modificare? (Inserisci la categoria o la descrizione)\n>>> ')
    for i in range(len(tmp_preset)):
        if x in tmp_preset[i]:
            print('Nome categoria attuale: {}'.format(tmp_preset[i][0]))
            print('Descrizione attuale della categoria {} è: {}'.format(tmp_preset[i][0], tmp_preset[i][1]))
            new = input('Inserisci nuovo nome alla categoria: ')
            new_cat = input('Inserisci nuova descrizione per la categoria {}'.format(new))
            tmp_preset[i] = (new, new_cat)
            with open(nfile_categorie_amici, 'w') as f:
                f.writelines('Categorie Amici,Descrizione,\n')
                for x, y in tmp_preset:
                    f.writelines(x + ',' + y + ',\n')
    menu()


# MENU
def menu():
    print('\n******MENU PRINCIPALE******')
    a = input(
        "1.Inserimento Nuove Categorie Amici\n2.Inserimento Nuovi Amici\n"
        "3.Estrai gli amici di una determinata categoria\n4.Estrarre un amico in base al nome\n"
        "5.Correggi i dati di un amico\n"
        "6.Elimina tutti i file\n7.Esci\n>>> ")
    if a == '1':
        menu_categorie()
    elif a == '2':
        menu_amici()
    elif a == '3':
        estrai_categoria()
    elif a == '4':
        estrai_nome()
    elif a == '5':
        correggi_dati()
    elif a == '6':
        a = input('Sei sicuro? La scelta che stai per eseguire è irreversibile!!! [SI/NO]\n>>> ')
        if a.upper() == 'SI' or a.upper() == 'YES':
            elimina_file(nfile_categorie_amici)
            elimina_file(nfile_rubrica_amici)
            menu()
        else:
            menu()
    elif a == '7':
        print('Grazie per aver usato il programma')
    else:
        print("ERRORE")
        menu()


# MAIN
print('Rubrica Amici\t\tv. {}\nCopyright © Simone Ungaro - Davide Grossi'.format(versione))
menu()
