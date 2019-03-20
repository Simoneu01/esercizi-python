# -*- coding: utf-8 -*-

# Created by Simone Ungaro at Febbraio 13/02/2019 11:57
# Created with PyCharm
# Project: programmazione_ad_oggetti


class Passeggero(object):
    def __init__(self, genere, tipo):
        self.genere = genere
        self.tipo = tipo
        self.trasportato = False
        self.riva = 0
        self.mangiato = False

    def in_barca(self):
        pass

    def mangia(self, passeggero):
        pass


# MAIN

lupo = Passeggero('Carnivoro', 'Animale')

print(lupo.tipo, lupo.genere, lupo.mangiato, lupo.riva, lupo.trasportato)