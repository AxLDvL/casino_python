#!#!/usr/bin/env python3



#début de la partie
print("Bienvenue dans le casino python")
#création des joueurs
username = input("Quel est votre nom? ")
#si le joueur est présent dans le fichier score.txt, on récupère son wallet
with open("score.txt", "r") as f:
    content = f.readlines()
    for line in content:
        if username in line:
            wallet = line.split(";")[1]
            print(f"Bonjour {username}, vous avez {wallet}€")
            break
    else:
        wallet = 100
        print(f"Bonjour {username}, vous avez {wallet}€")