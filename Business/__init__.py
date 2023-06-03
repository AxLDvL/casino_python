#!/usr/bin/env python3

def formatName(name):
    name = name[0].upper() + name[1:].lower()
    return name
def enregistrerScore(player):
    with open("score.txt", "r") as f:
        lines = f.readlines()

    # Trouver la ligne correspondante et la modifier
    for i, line in enumerate(lines):
        if line.strip().startswith(player.username) :
            lines[i] = f"{player}\n"

    # Réécrire le fichier avec les nouvelles données
    with open("score.txt", "w") as f:
        f.writelines(lines)

