#Importando a framework
from flask import Flask
import json

f = open("mapas.json")
data = json.load(f)

#flask run

#Instanciando o Flask
app = Flask(__name__)

@app.route("/")
def mapas_api():
    return data