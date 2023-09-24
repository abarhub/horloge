# pip install Flask
# flask --app server run --host=0.0.0.0
import threading
from time import sleep

from flask import Flask, render_template, url_for, jsonify, request

from raspberry import RaspberryPi

app = Flask(__name__)

rasp = RaspberryPi()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('page.html', name=name)


def horloge():
    rasp.horloge()
    pass


def minuteur(heure):
    print('heure=', heure)
    heures = 0
    minutes = 1
    secondes = 30
    if heure != None and len(heure) > 0:
        tab = heure.split(':')
        if len(tab) == 3:
            heures = int(tab[0])
            minutes = int(tab[1])
            secondes = int(tab[2])
    print('heure:', heures, 'minutes:', minutes, 'secondes:', secondes)
    rasp.minuteur(minutes, secondes)
    pass


def arret():
    rasp.arret()
    pass

def demarrage():
    print("startup")
    action(action='horloge')

@app.route('/api/action/<action>')
def action(action=None):
    if action != None:
        print('action=', action)
        if action == 'horloge':
            hologe_thread = threading.Thread(target=horloge, name="horloge")
            hologe_thread.start()
        elif action == 'minuteur':
            print('param', request.args['time'])
            heure = request.args['time']
            minuteur_thread = threading.Thread(target=minuteur, name="minuteur", args=(heure,))
            minuteur_thread.start()
        elif action == 'arret':
            arret_thread = threading.Thread(target=arret, name="arret")
            arret_thread.start()
        dictionnaire = {
            'type': 'Prévision de température',
            'valeurs': [24, 24, 25, 26, 27, 28],
            'unite': "degrés Celcius"
        }
        return jsonify(dictionnaire)
    else:
        return ''

# @app.before_first_request
# def my_func():
#     print('demarrage du programme ...')
#     demarrage()
#     print('demarrage du programme OK')

# @app.teardown_appcontext
# def teardown_appcontext(response_or_exc):
#     print('arret du programme ...')
#     arret()
#     print('arret du programme OK')

#demarrage()
