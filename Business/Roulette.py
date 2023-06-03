#!/usr/bin/env python3
from Business.jeu import Jeu
import random

class Roulette(Jeu):
    #attributs
    _nom = "Roulette"

    #constructeur
    def __init__(self):
        super().__init__(self._nom)

    #méthodes
    def run(self, player):
        print("let's play!")
        print(f"Vous avez {player.solde} crédits")
        while True:
                mise = input("Quelle somme voulez-vous miser? (tapez q pour quitter) ")
                match mise:
                    case "q":
                        break
                    case _:
                        try:
                            mise = int(mise)
                            if not player.debit(mise):
                                continue
                        except ValueError:
                            print("\nVous devez saisir un nombre entier\n")
                        while True:
                            nombre_choisi = input("Sur quel nombre voulez-vous miser?\nSaisissez un nombre entre 0 et 49: ")
                            try:
                                nombre_choisi = int(nombre_choisi)
                                if nombre_choisi < 0 or nombre_choisi > 49:
                                    print("\nVous devez saisir un nombre entre 0 et 49\n")
                                    continue
                                else:
                                    break
                            except ValueError:
                                print("\nVous devez saisir un nombre entier entre 0 et 49\n")
                                continue
                        print(f"\nVous avez misé {mise}€ sur le {nombre_choisi}\n")
                        nombre_tire = random.randint(0,49)
                        print(f"Le nombre tiré est le {nombre_tire}\n")
                        if nombre_choisi == nombre_tire:
                            player.credit(mise * 3)
                            print(f"Bravo! Vous avez gagné {mise*3}€")
                            print(f"Votre solde est maintenant de {player.solde}€\n")
                            continue
                        else:
                            print("Dommage, vous avez perdu\n")
                            continue