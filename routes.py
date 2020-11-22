from flask import Flask, request
from usuario_controller import insertUsuario

app = Flask("python-api")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola": "mundo"}

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():
    
    body = request.get_json()

    if("nome" not in body):
        return geraResponse(400, "O campo nome é obrigatório")

    if("email" not in body):
        return geraResponse(400, "O campo email é obrigatório")

    if("senha" not in body):
        return geraResponse(400, "O campo senha é obrigatório")

    usuario = insertUsuario(body["nome"], body["email"], body["senha"])

    return geraResponse(200, "Usuario criado", "user",  usuario)

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    tipoMensagem = "mensagem" if status == 200 else "erro"
    response = {}
    response["status"] = status
    response[tipoMensagem] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo

    return response

app.run(host="0.0.0.0", debug= False)
