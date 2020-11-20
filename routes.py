from flask import Flask, request

app = Flask("python-api")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola": "mundo"}

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():
    body = request.get_json()
    print(body)
    return body

app.run(host="0.0.0.0", port= 2000, debug= False)