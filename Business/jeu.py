#!/usr/bin/env python3

class Jeu:
    #attributs
    _nom = None

    #constructeur
    def __init__(self, nom):
        self._nom = nom

    #méthodes
    def bienvenue(self):
        print(f"Bienvenue dans le jeu de la {self._nom}")