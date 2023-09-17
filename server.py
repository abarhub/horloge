# pip install Flask
# flask --app server run --host=0.0.0.0
import threading
from time import sleep

from flask import Flask, render_template, url_for, jsonify

from raspberry import RaspberryPi

app = Flask(__name__)


# def init():
#     url_for('static', filename='style.css')
#
# def create_app():
#     app = Flask(__name__)
#
#     with app.app_context():
#         init()
#
#     return app
#
#
# app=create_app()

rasp= RaspberryPi()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('page.html', name=name)

def horloge():
    rasp.horloge()
    # import horloge
    # horloge.stop()
    # sleep(1.0)
    # horloge.demarrage()

def minuteur():
    # import minuteur
    # minuteur.demarrage()
    rasp.minuteur(1,30)

def arret():
    rasp.arret()
    # import arret,horloge
    # horloge.stop()
    # sleep(1.0)
    # arret.demarrage()

@app.route('/api/action/<action>')
def action(action=None):
    if action != None:
        print('action=', action)
        if action=='horloge':
            hologe_thread = threading.Thread(target=horloge, name="horloge")
            hologe_thread.start()
        elif action=='minuteur':
            minuteur_thread = threading.Thread(target=minuteur, name="minuteur")
            minuteur_thread.start()
        elif action=='arret':
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
