#!/usr/bin/env python3

class User:
    # Attributs
    _name = None
    _wallet = None

    # Constructeur
    def __init__(self, name, wallet=100):
        self._name = name
        self._wallet = wallet

    # Getters & setters
    @property
    def username(self):
        return self._name
    @username.setter
    def username(self, name):
        if len(name) > 0:
            #formatage du nom avec la première lettre en majuscule et le reste en minuscule
            name = name[0].upper() + name[1:].lower()
            self._name = name
        else:
            print("Le nom doit être renseigné")
    @property
    def wallet(self):
        return self._wallet
    @wallet.setter
    def wallet(self, wallet):
        if wallet > 0:
            self._wallet = wallet
        else:
            print("Le montant doit être positif")

    # Méthodes
    def __str__(self):
        return f"{self._name};{self._wallet}"

    def credit(self, amount):
        self._wallet += amount
        print(f"Le compte de {self._name} a été crédité de {amount}€")
    def bet(self, amount):
        if self._wallet >= amount:
            self._wallet -= amount
            print(f"Le compte de {self._name} a été débité de {amount}€")
            return 1
        else:
            print(f"Le compte de {self._name} n'est pas suffisamment approvisionné")
            return 0