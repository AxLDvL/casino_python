#!/usr/bin/env python3
from Business.jeu import Jeu
from Business.User import User
import random
#creer une classe MachineASous qui extend Jeu
class MachineASous(Jeu):
    #attributs
    _nom = "Machine à sous"

    #constructeur
    def __init__(self):
        super().__init__(self._nom)

    #méthodes
    def run(self, player):
        print("let's play!")
        print(f"Vous avez {player.solde} crédits")
        while True:
            mise = input("choix:\nMiser 1€ (1)\nQuitter (q) ")
            match mise:
                case "1":
                    if not player.debit(1):
                        break
                    #générer 3 nombres aléatoires entre 1 et 6 et les afficher
                    tirage = [random.randint(1,6) for i in range(3)]
                    print("Tirage:")
                    print(tirage)
                    print('')
                    #si les 3 nombres sont identiques, le joueur gagne 500€ sinon il ne gagne rien
                    if tirage[0] == tirage[1] == tirage[2]:
                        player.credit(500)
                        print("Gagné!!!")
                        print(f"Vous avez {player.solde} crédits")
                    else:
                        print("Perdu! Retentez votre chance\n")
                        continue
                case "q":
                    break
                case _:
                    print("Choix invalide")
                    continue


