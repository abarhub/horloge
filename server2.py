import threading
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from raspberry import RaspberryPi

rasp = RaspberryPi()


def debut():
    print('Début')


def fin():
    print('Fin')


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    debut()
    yield
    # Clean up the ML models and release the resources
    fin()


app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")


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
    #rasp.arret()
    pass

def demarrage():
    print("startup")
    #action(action='horloge')


@app.get("/home")
def index():
    return {"message": "Hello World"}


@app.get("/api/action/{action}")
async def read_item(action: str, time: str = ''):
    #return {"message": "Hello " + action + ":" + time}
    if action != '':
        print('action=', action)
        if action == 'horloge':
            hologe_thread = threading.Thread(target=horloge, name="horloge")
            hologe_thread.start()
        elif action == 'minuteur':
            print('param', time)
            heure = time
            minuteur_thread = threading.Thread(target=minuteur, name="minuteur", args=(heure,))
            minuteur_thread.start()
        elif action == 'arret':
            arret_thread = threading.Thread(target=arret, name="arret")
            arret_thread.start()
        # dictionnaire = {
        #     'type': 'Prévision de température',
        #     'valeurs': [24, 24, 25, 26, 27, 28],
        #     'unite': "degrés Celcius"
        # }
        # return jsonify(dictionnaire)
        return {"message": "Hello " + action + ":" + time}
    else:
        return ''

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=30000)
