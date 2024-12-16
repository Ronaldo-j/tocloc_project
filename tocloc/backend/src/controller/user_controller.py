from flask import request, jsonify
from src.model.user_modal import (
    criar_user, listar_user, atualizar_user, deletar_user, buscar_user
)
from bcrypt import checkpw

def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    try:
        # Buscar o usuário pelo email
        user, status_code = buscar_user(email)

        if status_code != 200:
            return jsonify({"error": "Usuário não encontrado"}), 404
        
        # Verificar a senha
        if checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return jsonify({
                    "message": "Login realizado com sucesso",
                    "user": {
                    "id": user['id'],
                    "nomeUsuario": user['nomeUsuario'],
                    "email": user['email']
                }
            }), 200
        else:
            return jsonify({"error": "Senha incorreta"}), 401

    except Exception as erro:
        return jsonify({"error": str(erro)}), 500
def cadastrar_user():
    data = request.get_json()
    nomeUsuario = data.get("nomeUsuario")
    email = data.get("email")
    password = data.get("password")

    message, status_code = criar_user(nomeUsuario, email, password)
    return jsonify(message), status_code

def listar_user_controller():
    user_list, status_code = listar_user()
    return jsonify(user_list), status_code

def buscar_user_controller(id):
    user, status_code = buscar_user(id)
    if status_code == 200:
        return jsonify(user), 200
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404


def atualizar_user_controller(id):
    data = request.get_json()
    nomeUsuario = data.get('nomeUsuario')
    email = data.get('email')
    password = data.get('password')

    message, status_code = atualizar_user(id, nomeUsuario, email, password)
    return jsonify(message), status_code

def deletar_user_controller(id):
    message, status_code = deletar_user(id)
    return jsonify(message), status_code