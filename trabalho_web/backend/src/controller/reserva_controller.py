from flask import jsonify, request
from src.model.reserva_modal import (
    criar_reserva, listar_reservas, buscar_reserva, atualizar_reserva, deletar_reserva
)

def cadastrar_reserva_controller():
    data = request.get_json()
    user_id = data.get("user_id")
    quadra_id = data.get("quadra_id")
    horario = data.get("horario")

    message, status_code = criar_reserva(user_id, quadra_id, horario)
    return jsonify(message), status_code

def listar_reservas_controller():
    reservas, status_code = listar_reservas()
    return jsonify(reservas), status_code

def buscar_reserva_controller(id):
    reserva, status_code = buscar_reserva(id)
    return jsonify(reserva), status_code

def atualizar_reserva_controller(id):
    data = request.get_json()
    user_id = data.get("user_id")
    quadra_id = data.get("quadra_id")
    horario = data.get("horario")

    message, status_code = atualizar_reserva(id, user_id, quadra_id, horario)
    return jsonify(message), status_code

def deletar_reserva_controller(id):
    message, status_code = deletar_reserva(id)
    return jsonify(message), status_code
