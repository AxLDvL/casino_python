#!/usr/bin/env python3
from Business.jeu import Jeu
#creer une classe MachineASous qui extend Jeu
class MachineASous(Jeu):
    #attributs
    _nom = "Machine à sous"

    #constructeur
    def __init__(self):
        super().__init__(self._nom)


    #méthodes
    def run(self):
        print("let's play")
