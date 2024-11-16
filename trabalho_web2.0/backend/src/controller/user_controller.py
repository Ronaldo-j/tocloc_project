from flask import request, jsonify
from src.model.user_modal import (
    criar_user, listar_user, atualizar_user, deletar_user, buscar_user
)

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
    return jsonify(user), status_code

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