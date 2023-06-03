#!/usr/bin/env python3

class User:
    # Attributs
    _name = None
    _solde = None

    # Constructeur
    def __init__(self, name, solde=100):
        self.username = name
        self.solde = solde

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
    def solde(self):
        return self._solde
    @solde.setter
    def solde(self, credit):
        if credit > 0:
            self._solde = credit
        else:
            print("Le montant doit être positif")

    # Méthodes
    def __str__(self):
        return f"{self._name};{self._solde}"

    def credit(self, amount):
        self._solde += amount
        print(f"Le compte de {self._name} a été crédité de {amount}€")
    def debit(self, amount):
        amount = abs(amount)
        if self._solde >= amount:
            self._solde -= amount
            print(f"Le compte de {self._name} a été débité de {amount}€\nSolde restant: {self._solde}€\n")
            return 1
        else:
            print(f"Le compte de {self._name} n'est pas suffisamment approvisionné")
            return 0