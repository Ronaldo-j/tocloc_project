from flask import jsonify, request
from src.model.quadra_modal import (
    criar_quadra, listar_quadras, buscar_quadra, atualizar_quadra, deletar_quadra
)

def cadastrar_quadra():
    data = request.get_json()
    
    # Verificar se todos os campos necessários estão presentes
    nomeQuadra = data.get("nomeQuadra")
    preco = data.get("preco")
    localizacao = data.get("localizacao")
    descricao = data.get("descricao")
    
    if not nomeQuadra or not preco or not localizacao or not descricao:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    message, status_code = criar_quadra(nomeQuadra, preco, localizacao, descricao)
    return jsonify({"message": message}), status_code



def listar_quadra_controller():
    quadra_list, status_code = listar_quadras()
    return jsonify(quadra_list), status_code

def buscar_quadra_controller(id):
    quadra, status_code = buscar_quadra(id)
    return jsonify(quadra), status_code

def atualizar_quadra_controller(id):
    data = request.get_json()
    nomeQuadra = data.get("nomeQuadra")
    preco = data.get("preco")
    localizacao = data.get("localizacao")
    descricao = data.get("descricao")

    message, status_code = atualizar_quadra(id, nomeQuadra, preco, localizacao, descricao)
    return jsonify(message), status_code

def deletar_quadra_controller(id):
    message, status_code = deletar_quadra(id)
    return jsonify(message), status_code