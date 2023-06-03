#!/usr/bin/env python3
from Business import formatName, enregistrerScore
from Business.Roulette import Roulette
from Business.User import User
from Business.MachineASous import MachineASous
#début de la partie
print("Bienvenue dans le casino python")
#création du joueur
username = input("Quel est votre nom? ")
username = formatName(username)

#si le joueur est présent dans le fichier score.txt, on récupère son solde
with open("score.txt", "r") as f:
    content = f.readlines()
    for line in content:
        if username in line:
            solde = line.split(";")[1]
            print(f"Bonjour {username}, vous avez {solde}€")
            try:
                solde = int(solde)
            except ValueError:
                print("Erreur lors de la lecture du fichier score.txt")
            player = User(username, solde)
            break
    else:
        #sinon on crée un nouveau joueur avec un wallet de 100€
        player = User(username)
        with open("score.txt", "a") as f:
            f.write(f"\n{player}")
        print(player)

#un menu demande au joueur s'il veut jouer à la roulette ou à la machine à sous
while True:
    choice = input("\nVoulez-vous jouer :\nà la roulette (1)\nà la machine à sous (2)\nQuitter (q) ")
    match choice:
        case "1":
            game = Roulette()
            game.bienvenue()
            game.run(player)
        case "2":
            game = MachineASous()
            game.bienvenue()
            game.run(player)
        case "q":
            #on enregistre le solde du joueur dans le fichier score.txt
            enregistrerScore(player)
            print("Au revoir")
            break
        case _:
            print("\nChoix invalide\n")
