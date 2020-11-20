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

