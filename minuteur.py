#!/usr/bin/env python3

# inspiré de https://raspberry-lab.fr/Composants/Afficheur-7-Segments-x4-TM1637/
# et de https://github.com/depklyon/raspberrypi-tm1637
#
# C'est en Python 3
# pour installer el module : pip3 install raspberrypi-tm1637

# Importation des librairies TM1637 et time
from tm1637 import TM1637
from time import sleep

def demarrage():
    # Stockage de la duree dans des variables
    print("- Duree du minuteur -")
    minutes = int(input("Minutes : "))
    secondes = int(input("Secondes : "))
    print("- Demarage du minuteur : " + str(minutes) + ":" + str(secondes) + " -")

    # Initialisation de l'afficheur
    #afficheur = TM1637(clk=23, dio=24)
    afficheur = TM1637(clk=5, dio=4)

    # Definition de la luminosite (0-7)
    afficheur.brightness(2)

    # Affichage du temps du minuteur sur le module avant demarage
    # .numbers(x, y) : Affiche x sur les deux premiers 7 segments et y sur les deux suivants
    # -10 < x(resp. y) < 100
    afficheur.numbers(minutes, secondes)

    # Boucle du minuteur
    i = minutes
    j = secondes
    while i >= 0:
        while j >= 0:
            afficheur.numbers(i, j)
            sleep(1)
            j -= 1
        i -= 1
        j = 59
    print("- Temps ecoule ! -")

    # Animation de fin : on fait clignoter 00:00
    for n in range(0, 20):
        afficheur.brightness(0)
        sleep(0.25)
        afficheur.brightness(7)
        sleep(0.25)

