#!/usr/bin/env python3

# Importation des librairies TM1637 et time
from tm1637 import TM1637
from time import sleep, localtime

fin=False

# Fonction appelee a l'infini pour afficher l'heure
def afficher_horloge(aff):
    # Recuperation de l'heure locale et affichage sur le module
    t = localtime()
    aff.numbers(t.tm_hour, t.tm_min)


def demarrage():
    print("Demarrage de l'horloge ...")

    # Initialisation de l'afficheur et definition de la luminosite (0-7)
    afficheur = TM1637(clk=5, dio=4)
    afficheur.brightness(1)

    fin = False
    # Boucle infinie appelant la fonction afficher_horloge()
    while not fin:
        afficher_horloge(afficheur)
        # Pour soulager le Raspberry : pause de 0.5 sec
        sleep(0.5)


def stop():
    fin=True
