#!/usr/bin/env python3
from Business import formatName
from Business.User import User
from Business.MachineASous import MachineASous
#début de la partie
print("Bienvenue dans le casino python")
#création du joueur
username = input("Quel est votre nom? ")
username = formatName(username)

#si le joueur est présent dans le fichier score.txt, on récupère son wallet
with open("score.txt", "r") as f:
    content = f.readlines()
    for line in content:
        if username in line:
            wallet = line.split(";")[1]
            print(f"Bonjour {username}, vous avez {wallet}€")
            player = User(username, wallet)
            print(player)
            break
    else:
        #sinon on crée un nouveau joueur avec un wallet de 100€
        player = User(username)
        print(player)

#un menu demande au joueur s'il veut jouer à la roulette ou à la machine à sous
while True:
    choice = input("Voulez-vous jouer :\nà la roulette (1)\nà la machine à sous (2)\nQuitter (q) ")
    match choice:
        case "1":
            print("Roulette")
            break
        case "2":
            game = MachineASous()
            game.bienvenue()
            break
        case "q":
            print("Au revoir")
            break
        case _:
            print("\nChoix invalide\n")
