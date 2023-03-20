from wams import app
from wams import socketio

#check si run.py exec le dossier et l'importe pas
if __name__ == '__main__':
    socketio.run(app, debug = True)
    
