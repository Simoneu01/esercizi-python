def menu1():
    c = 0
    while c != 4:
        while c <= 0 or c > 4:
            c = int(input(
                '1) per inserire un nuovo prodotto\n2) per inserire le vendite\n3) per visualizare le altre scelte\n4) per uscire\n'))
        if c == 1:
            ins()
            c = 0
        elif c == 2:
            ins_ven()
            c = 0
        elif c == 3:
            menu2()
            c = 0
        elif c == 4:
            c = 0
            break


def menu2():
    c = 0
    while c != 5:
        while c <= 0 or c => 5:
            c = int(input(
                '1)se vuoi sapere le vendite totali\n2)se vuoi sapere il venduto per tipologia di prodotto e per '
                'settimana\n3)se vuoi sapere il nome dell prodotto che ha venduto maggiormente e quello che ha '
                'venduto di meno\n4)se vuoi sapere all’inserimento di un numero quante volte nell’arco della '
                'settimanali venduto ha superato quelle vendite\n5)per uscire premi\n'))
        if c == 1:
            v_tot()
            c = 0
        elif c == 2:
            v_set()
            c = 0
        elif c == 3:
            mag_min()
            c = 0
        elif c == 4:
            t_c()
            c = 0
        elif c == 5:
            break
            c = 0


def ins():
    a = open('codici.txt', 'a')
    c = input('inserisci codice prodotto')
    d = input('inserisci descrizione prodotto')
    a.write(c + ',' + d + ',' + '\n')


def ins_ven():
    d = 0
    e = 0
    f = 0
    g = 0
    h = -1
    i = -1

    b = open('vendite.txt', 'a')
    c = input('inserisci codice prodotto')

    while d <= 0 or d > 31:
        d = int(input('inserisci giorno maggiore di 0 e minore di 32'))
    d = str(d)
    while e <= 0 or e > 12:
        e = int(input('inserisci mese maggiore di 0 e minore di 13'))
    e = str(e)
    while f <= 1980 or f > 2100:
        f = int(input('inserisci anno maggiore di 1980 e minore di 2100 '))
    f = str(f)
    while g <= 0 or g > 53:
        g = int(input('inserisci settimana maggiore di 0 e minore di 54'))
    g = str(g)
    while h <= 0:
        h = int(input('inserisci quantita maggiore di 0'))
    h = str(h)
    while i <= 0 or i > 12:
        i = int(input('inserisci quantita minore di 13 e maggiore di 0'))
    i = str(i)
    b.writelines(c + ',' + d + ',' + e + ',' + f + ',' + g + ',' + h + ',' + i + ',' + '\n')


def v_tot():
    tot = 0
    b = open('vendite.txt')
    a = b.readlines()
    for i in range(len(a)):
        temp = a[i]
        temp = temp.split(',')
        tot = tot + (int(temp[5]) * int(temp[6]))
    print(tot)


def v_set():
    f = 0
    e = 0
    b = open('vendite.txt')
    a = b.readlines()
    while f <= 1980 or f > 2100:
        e = int(input("inserisci l'anno in cui vuoi sapere la vendita maggiore di 1980 e minore di 2100 "))
    while g <= 0 or g > 53:
        c = int(input('inserisci la settimana in cui vuoi sapere la vendita maggiore di 0 e minore di 54'))
    d = input('inserisci il codice prodotto di cui vuoi sapere la vendita')
    for i in range(len(a)):
        temp = a[i]
        temp = temp.split(',')
        if temp[3] == str(e) and temp[4] == str(c) and temp[0] == d:
            print('quello che vuoi')
            f = int(temp[5]) * int(temp[6])
        else:
            e = 1
    if e == 1:
        print('non è stato trovato')
    print(f)


def mag_min():
    b = open('vendite.txt')
    a = b.readlines()
    c = int(input('inserisci  la giornata in cui vuoi sapere il massimo e il minimo venduto per prodotto'))
    d = int(input('inserisci  la mese in cui vuoi sapere il massimo e il minimo venduto per prodotto'))
    e = int(input('inserisci  la anno in cui vuoi sapere il massimo e il minimo venduto per prodotto'))
    for i in range(len(a)):
        temp = a[i]
        temp = temp.split(',')
        if temp[1] == str(c) and temp[2] == str(d) and temp[3] == str(e):
            if i == 0:
                max = temp[5]
                min = temp[5]
            if temp[5] >= max:
                max = temp[5]
            if temp[5] <= min:
                min = temp[5]

    print('il minimo venduto è', max)
    print('il massimo venduto è', min)


def t_c():
    cont = 0
    b = open('vendite.txt')
    a = b.readlines()
    c = int(input('inserisci il valore di cui vuoi sapere quante volte sia stato superato il valore inserito'))
    d = int(input('inserisci la settimana di cui vuoi sapere quante volte sia stato superato il valore inserito'))
    e = int(input('inserisci la settimana di cui vuoi sapere quante volte sia stato superato il valore inserito'))
    for i in range(len(a)):
        temp = a[i]
        temp = temp.split(',')

        if int(temp[5]) > c and d == temp[4] and temp[3] == str(e):
            cont = cont + 1
    if cont == 0:
        print('il valore non è stato superato')
    else:
        print('il valore è stato superato', cont, 'volte')


# main
menu1()