# Importation des librairies TM1637 et time
from tm1637 import TM1637
from time import sleep, localtime

VIDE = ''
HORLOGE = 'HORLOGE'
MINUTEUR = 'MINUTEUR'


class RaspberryPi:

    def __init__(self):
        self.afficheur = None
        self.finHorloge = False
        self.finMinuteur = False
        self.action = VIDE

    # Fonction appelee a l'infini pour afficher l'heure
    def _afficher_horloge(self, aff):
        # Recuperation de l'heure locale et affichage sur le module
        t = localtime()
        aff.numbers(t.tm_hour, t.tm_min)

    def _initAfficheur(self):
        if self.afficheur == None:
            # Initialisation de l'afficheur
            self.afficheur = TM1637(clk=5, dio=4)

    def horloge(self):
        self.stopTout()
        self.action = HORLOGE
        print("Demarrage de l'horloge ...")

        # Initialisation de l'afficheur et definition de la luminosite (0-7)
        self._initAfficheur()
        self.afficheur.brightness(0)

        self.finHorloge = False
        # Boucle infinie appelant la fonction afficher_horloge()
        while not self.finHorloge:
            self._afficher_horloge(self.afficheur)
            # Pour soulager le Raspberry : pause de 0.5 sec
            sleep(0.5)

        self.action = VIDE

    def stopHorloge(self):
        self.finHorloge = True
        sleep(1.0)

    def minuteur(self, minutes, secondes):
        self.stopTout()
        self.action = MINUTEUR
        print("- Demarage du minuteur : " + str(minutes) + ":" + str(secondes) + " -")

        # Initialisation de l'afficheur
        self._initAfficheur()

        # Definition de la luminosite (0-7)
        self.afficheur.brightness(2)

        # Affichage du temps du minuteur sur le module avant demarage
        # .numbers(x, y) : Affiche x sur les deux premiers 7 segments et y sur les deux suivants
        # -10 < x(resp. y) < 100
        self.afficheur.numbers(minutes, secondes)

        self.finMinuteur = False

        # Boucle du minuteur
        i = minutes
        j = secondes
        while i >= 0 and not self.finMinuteur:
            while j >= 0 and not self.finMinuteur:
                self.afficheur.numbers(i, j)
                sleep(1)
                j -= 1
            i -= 1
            j = 59
        print("- Temps ecoule ! -")

        # Animation de fin : on fait clignoter 00:00
        for n in range(0, 20):
            if self.finMinuteur:
                break
            self.afficheur.brightness(0)
            sleep(0.25)
            self.afficheur.brightness(7)
            sleep(0.25)

        self.action = VIDE

    def stopMinuteur(self):
        self.finMinuteur = True
        sleep(1.0)

    def stopTout(self):
        if self.action == HORLOGE:
            self.stopHorloge()
        elif self.action == MINUTEUR:
            self.stopMinuteur()

    def arret(self):
        self.stopTout()
        self._initAfficheur()

        # all LEDS off
        self.afficheur.write([0, 0, 0, 0])
