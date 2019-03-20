#  -*- coding: utf-8 -*-

"""
Created on Tue Jan 22 10:04:47 2019

@author: Simone Ungaro

specifiche progetto sw farmacia

i dati relativi al venduto giornaliero (quantità e valore economico) per tipologia prodotto
devono essere salvati su un file
le tipologie di prodotto sono cosmetico ( C ), dietetico (PD), farmaco (F)
è possibile aggiungere una nuova tipologia di prodotto
venduto per tipologia di prodotto e per settimana
tipologia di prodotto con vendite maggiore nella giornata
tipologia di prodotto con vendite maggiore nella settimana
tipologia di prodotto con vendite minore nella giornata
tipologia di prodotto con vendite minore nella settimana
venduto totale
inserire un valore e vedere quante volte il venduto l’ha superato nella settimana

struttura dei file:
codici.txt
codice,descrizione,\n
vendite.txt
codice,giorno,mese,anno,quantità,valore,\n


"""

# IMPORT
import datetime
import os
# import time
# from pandas import DataFrame

# VARIABILI GLOBALI
presets = dict(C = 'Cosmetico', PD = 'Dietetico', F = 'Farmaco')
versione = '1.4.0'
file_vendite = 'vendite.txt'
file_codici = 'codici.txt'
# FUNZIONI


def report(arg):
    if arg == 'vendite_tot':
        qta_tot = 0
        with open(file_vendite) as f:
            next(f)
            for line in f:
                (cod, g, m, a, s, q, v, n) = line.split(',')
                qta_tot = qta_tot + (int(q) * int(v))
        print('Venduto Totale (Somma di tutte le quantità vendute) = {}'.format(qta_tot))
        menu(True)
    elif arg == 'vendite':
        (codice, settimana, giorno, mese, anno, soglia) = creazione_report(arg)
        q_tot = 0
        v_tot = 0
        with open(file_vendite) as f:
            next(f)
            for line in f:
                (cd, g, m, a, s, q, v, n) = line.split(',')
                if codice == cd and str(settimana) == s and str(anno) == a:
                    q_tot = q_tot + int(q)  # Somma quantità venduta
                    v_tot = v_tot + (int(v) * int(q))  # Somma ricavo totale
        print(
            'La vendita del prodotto {} nella settimana {} dell\'anno {} è di quantità {} con ricavo totale {}'.format(
                codice, settimana, anno, q_tot, v_tot))
        menu(True)
    elif arg == 'magg_min':
        a = input(
            'Tipologia di prodotto più venduto e menu venduto in:\n1. Giorno Specifico\n2. Settimana Specifica\n>>> ')
        min = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        max = 0
        vendita = {'max': {}, 'min': {}}
        if a == '1':
            (codice, settimana, giorno, mese, anno, soglia) = creazione_report(arg)
            with open(file_vendite) as f:
                next(f)
                for line in f:
                    (cd, g, m, a, s, q, v, n) = line.split(',')
                    if str(giorno) == g and str(mese) == m and str(anno) == a:
                        if int(q) > max:
                            max = int(q)
                            vendita['max'][cd] = q
                        if int(q) < min:
                            min = int(q)
                            vendita['min'][cd] = q
            max = [list(vendita['max'].keys()), list(vendita['max'].values())]
            min = [list(vendita['min'].keys()), list(vendita['min'].values())]
            max = flat(max)
            min = flat(min)
            print('Il prodotto più venduto nell giorno {}/{}/{} è {} con quantità {}'.format(giorno, mese, anno, max[0],
                                                                                             max[1]))
            print(
                'Il prodotto meno nell giorno {}/{}/{} è {} con quantità {}'.format(giorno, mese, anno, min[0], min[1]))
        elif a == '2':
            (codice, settimana, giorno, mese, anno, soglia) = creazione_report(arg)
            with open(file_vendite) as f:
                next(f)
                for line in f:
                    (cd, g, m, a, s, q, v, n) = line.split(',')
                    if str(settimana) == s and str(anno) == a:
                        if int(q) > max:
                            max = int(q)
                            vendita['max'][cd] = q
                        if int(q) < min:
                            min = int(q)
                            vendita['min'][cd] = q
            max = [list(vendita['max'].keys()), list(vendita['max'].values())]
            min = [list(vendita['min'].keys()), list(vendita['min'].values())]
            max = flat(max)
            min = flat(min)
            print(
                'Il prodotto più venduto della settimana {} dell\'anno {} è {} con quantità {}'.format(settimana, anno,
                                                                                                       max[0], max[1]))
            print(
                'Il prodotto meno venduto della settimana {} dell\'anno {} è {} con quantità {}'.format(settimana, anno,
                                                                                                        min[0], min[1]))
        else:
            report('magg_min')
        menu(True)
    elif arg == 'soglia':
        (codice, settimana, giorno, mese, anno, soglia) = creazione_report(arg)
        cont = 0
        with open(file_vendite) as f:
            next(f)
            for line in f:
                (cd, g, m, a, s, q, v, n) = line.split(',')
                if str(settimana) == s and str(anno) == a and str(soglia) < q:
                    cont = cont + 1
        print(
            'La quantità inserita è stata superata {} volte/a nella settimana {} dell\'anno {}'.format(cont, settimana,
                                                                                                       anno))
        menu(True)
    else:
        print('Errore')
        menu()


def creazione_report(arg):
    tmp_presets = dict_codici()
    codice = settimana = giorno = mese = anno = soglia = 0
    if arg == 'vendite':
        # codice
        while True:
            codice = input("Inserisci codice identificativo: ")
            codice = codice.upper()
            if codice in tmp_presets:
                break
            else:
                print('Errore inserisci un codice identificativo corretto\n')
                print('Codici Prodotti disponibili: \n{}'.format(list(tmp_presets.keys())))
    if arg == 'vendite' or arg == 'magg_min' or arg == 'soglia':
        # settimana
        while True:
            settimana = int(input('Inserisci il numero della settimana da visualizzare: '))
            if 0 <= settimana <= 53:
                break
            else:
                print('Errore inserisci una settimana corretto\n')
    if arg == 'magg_min':
        # giorno
        while True:
            giorno = int(input("Inserisci giorno: "))
            if 1 <= giorno <= 31:
                break
            else:
                print('Errore inserisci un giorno corretto\n')
    if arg == 'magg_min':
        # mese
        while True:
            mese = int(input("Inserisci mese: "))
            if 1 <= mese <= 12:
                break
            else:
                print('Errore inserisci un mese corretto\n')
    if arg == 'vendite' or arg == 'magg_min' or arg == 'soglia':
        # anno
        while True:
            anno = int(input("Inserisci anno: "))
            if 1980 <= anno <= 2100:
                break
            else:
                print('Errore inserisci un anno corretto\n')
    if arg == 'soglia':
        # soglia
        while True:
            soglia = int(input("Inserisci soglia da verificare: "))
            if soglia >= 0:
                break
            else:
                print('Errore\nInserisci un valore corretto!!!')
    return codice, settimana, giorno, mese, anno, soglia


# Rende una lista di liste una unica lista
def flat(lista):
    return [j for i in lista for j in i]


# FUNZIONI PER VENDITE
def vendite():
    if os.path.isfile(file_codici):
        if os.path.isfile(file_vendite):
            print('!!!ATTENZIONE!!!!!\nFile {} trovato\nCome desideri procedere?\n'.format(file_vendite))
            print('****MENU VENDITE****')
            x = int(input('1. Sovrascrivere file\n2. Aggiungere vendita\n3. Annulla / Torna al menu '
                          'principale\n>>> '))
            if x == 1:
                creazione_vendite()
                menu()
            elif x == 2:
                creazione_vendite(False)
                menu()
            elif x == 3:
                menu()
            else:
                print('Errore')
                vendite()
        else:
            print('File "{}" non trovato!!!!!\nCreazione in corso...\n'.format(file_vendite))
            creazione_vendite()
            menu()
    else:
        print('File "{}" non trovato!!!\n'.format(file_codici))
        print('Devi prima creare il file "{}" ESEGUI il punto 1 del menu'.format(file_codici))
        menu()


def creazione_vendite(sovrascrivi = True):
    tmp_presets = dict_codici()
    if sovrascrivi:
        with open(file_vendite, 'w') as f:
            f.writelines('Codice Identificativo,Giorno,Mese,Anno,Settimana,Quantità,Valore,\n')
    with open(file_vendite, 'a+') as f:
        while True:
            while True:
                codice = input("Inserisci codice identificativo: ")
                codice = codice.upper()
                if codice in tmp_presets:
                    break
                else:
                    print('Errore inserisci un codice identificativo corretto\n')
                    print('Codici Prodotti disponibili: \n{}'.format(list(tmp_presets.keys())))
            while True:
                giorno = int(input("Inserisci giorno: "))
                if 1 <= giorno <= 31:
                    break
                else:
                    print('Errore inserisci un giorno corretto\n')
            while True:
                mese = int(input("Inserisci mese: "))
                if 1 <= mese <= 12:
                    break
                else:
                    print('Errore inserisci un mese corretto\n')
            while True:
                anno = int(input("Inserisci anno: "))
                if 1980 <= anno <= 2100:
                    break
                else:
                    print('Errore inserisci un anno corretto\n')
            while True:
                settimana = int(datetime.date(anno, mese, giorno).strftime("%V"))
                print('Il numero della settimana in base ai dati inseriti è: {}'.format(settimana))
                a = input('Vuoi confermare il numero della settimana? [SI / NO]\n>>> ').upper()
                if a.upper() == 'SI' or a.upper() == 'YES':
                    if 0 <= settimana <= 53:
                        break
                    else:
                        print('Errore inserisci una settimana corretto\n')
                    break
                elif a.upper() == 'NO':
                    settimana = int(input('Inserisci il numero della settimana: '))
                    if 0 <= settimana <= 53:
                        break
                    else:
                        print('Errore inserisci una settimana corretto\n')
                    break
                else:
                    print('\nErrore!!')
            while True:
                quantita = int(input("Inserisci quantità: "))
                if quantita >= 1:
                    break
                else:
                    print('Errore inserisci una quantità corretta\n')
            while True:
                valore = int(input("Inserisci valore del prodotto (singolo): "))
                if valore >= 1:
                    break
                else:
                    print('Errore inserisci un valore corretto\n')
            f.writelines(
                '{0},{1},{2},{3},{4},{5},{6},\n'.format(codice, str(giorno), str(mese), str(anno), str(settimana),
                                                        str(quantita), str(valore)))
            if input('\nScrivi fine per terminare.....\n>>> ') == 'fine':
                break


# FUNZIONI PER CODICI
def codici():
    if os.path.isfile(file_codici):
        print('!!!ATTENZIONE!!!!!\nFile {} trovato\nCome desideri procedere?\n'.format(file_codici))
        print('Codici Identificativi trovati nel file:\n{}'.format(list(dict_codici().keys())))
        print('\n****MENU CODICI****')
        x = int(input('1. Sovrascrivere file\n2. Aggiungere codice prodotto\n3. Annulla / Torna al menu '
                      'principale\n>>> '))
        if x == 1:
            # time.sleep(1)
            menu_codici()
        elif x == 2:
            # time.sleep(1)
            creazione_codici(False)
            # time.sleep(1)
            menu()
        elif x == 3:
            # time.sleep(1)
            menu()
        else:
            print('Errore')
            # time.sleep(1)
            codici()
    else:
        print('File "{}" non trovato\nCrazione File...\n'.format(file_codici))
        menu_codici()


def menu_codici():
    print('Codici identificativi base: {}'.format(list(presets.keys())))
    a = input('Vuoi aggiungere codici identificativi? [SI/NO]\n>>>')
    if 'SI' == a.upper() or 'YES' == a.upper():
        # time.sleep(1)
        creazione_codici()
        # time.sleep(1)
        menu()
    elif 'NO' == a.upper():
        with open(file_codici, 'w') as f:
            f.writelines('Codici Identificativi,Descrizione,\n')
            for x, y in presets.items():
                f.writelines(x + ',' + y + ',\n')
        # time.sleep(1)
        menu()
    else:
        print('\n!!!!!ERROR!!!!\n')
        # time.sleep(1)
        codici()


def creazione_codici(sovrascrivi = True):
    if sovrascrivi:
        tmp_presets = presets
        with open(file_codici, 'w') as f:
            f.writelines('Codici Identificativi,Descrizione,\n')
            while True:
                codice = input("Inserisci codice identificativo: ")
                descrizione = input("Inserisci la descrizione del codice {}: ".format(codice.upper()))
                tmp_presets[codice.upper()] = descrizione
                if input('\nScrivi fine per terminare.....\n>>> ') == 'fine':
                    break
            for x, y in tmp_presets.items():
                f.writelines(x + ',' + y + ',\n')
    elif not sovrascrivi:
        tmp_presets = {}
        with open(file_codici, 'a+') as f:
            while True:
                codice = input("Inserisci codice identificativo: ")
                descrizione = input("Inserisci la descrizione del codice {}: ".format(codice.upper()))
                tmp_presets[codice.upper()] = descrizione
                if input('\nScrivi fine per terminare.....\n>>> ') == 'fine':
                    break
            for x, y in tmp_presets.items():
                f.writelines(x + ',' + y + ',\n')


def dict_codici():
    d = {}
    with open(file_codici) as f:
        next(f)
        for line in f:
            (key, val, n) = line.split(',')
            d[key] = val
    return d


def read_vendite():
    cd = g = m = a = s = q = v = n = 0
    with open(file_vendite) as f:
        next(f)
        for line in f:
            (cd, g, m, a, s, q, v, n) = line.split(',')
    return cd, g, m, a, s, q, v, n


def menu(rep = False):
    if not rep:
        print('\n******MENU PRINCIPALE******')
        a = input("1.Inserimento Tipologie di prodotto\n2.Inserimento Dati Venduto\n3.Report\n4.Elimina tutti i "
                  "file\n5.Esci\n>>> ")
        if a == '1':
            # time.sleep(1)
            codici()
        elif a == '2':
            # time.sleep(1)
            vendite()
        elif a == '3':
            # time.sleep(1)
            menu(True)
        elif a == '4':
            a = input('Sei sicuro? La scelta che stai per eseguire è irreversibile!!! [SI/NO]\n>>> ')
            if a.upper() == 'SI' or a.upper() == 'YES':
                try:
                    os.remove(file_codici)
                    os.remove(file_vendite)
                    print("File '{}' e '{}' cancellati".format(file_codici,file_vendite))
                    # time.sleep(1)
                    menu()
                except:
                    print('\nI file non esistono\n')
                    # time.sleep(1)
                    menu()
            else:
                # time.sleep(1)
                menu()
        elif a == '5':
            print('Grazie per aver usato il programma')
        else:
            print("ERRORE")
            # time.sleep(1)
            menu()
    elif rep:
        print('\n******MENU REPORT******')
        a = input("1.Vendite Totali\n2.Vendite per Prodotto e per settimana\n3.Vendite Maggiori e Minori\n4.Valore "
                  "Soglia\n5.Torna al menu principale\n>>> ")
        if a == '1':
            # time.sleep(1)
            report('vendite_tot')
        elif a == '2':
            # time.sleep(1)
            report('vendite')
        elif a == '3':
            # time.sleep(1)
            report('magg_min')
        elif a == '4':
            # time.sleep(1)
            report('soglia')
        elif a == '5':
            # time.sleep(1)
            menu()
        else:
            print("ERRORE\n\n")
            # time.sleep(1)
            menu(True)


# MAIN
print('New SW Farmacia\t\tv. {}\nCopyright © Simone Ungaro'.format(versione))
try:
    menu()
except:
    print('Qualcosa non ha funzionato!! ERRORE')
    menu()
