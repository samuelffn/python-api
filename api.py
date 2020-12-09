import os
import requests
from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/rota-nome/<nome>") # GET
def rota(nome):
    return "Meu nome é " + nome

@app.route("/rota-nome-sobrenome/<nome>, <sobrenome>") # Testar se está correto
def rota(nome):
    return "Meu nome é " + nome + sobrenome

app.run(host="0.0.0.0", port= 2000, debug= False)
## Informações sobre os parâmetros utilizados:
# host="0.0.0.0" permite que outra máquina ou dispositivo acesse a aplicação, sem ser localhost
# port= 2000 é a porta onde a aplicação vai rodar. Por padrão roda na porta 5000
# debug= False para não seja feito debug


##  Instruções para execução deste arquivo:
# 1- No terminal acessa o diretório do projeto  
# 2- Utiliza o comando **python3 api.py**  
# 3- Abra o navegador para testar a rota padrão: http://localhost:2000/  
# 4- Teste a outra rota utilizando parâmetro: http://localhost:2000/rota-nome/Samuel


