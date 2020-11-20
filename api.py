import os
import requests
from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/rota-nome/<nome>")
def rota(nome):
    return "Meu nome é " + nome

app.run(host="0.0.0.0", port= 2000, debug= False)
# host="0.0.0.0" permite que outra máquina ou dispositivo acesse a aplicação, sem ser localhost
# port= 2000 é a porta onde a aplicação vai rodar. Por padrão roda na porta 5000
# debug= False para não seja feito debug

