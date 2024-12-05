from flask import jsonify, request
from werkzeug.utils import secure_filename
from src.database.conexao import criar_conexao
from src.model.quadra_modal import (
    criar_quadra, listar_quadras, buscar_quadra, atualizar_quadra, deletar_quadra
)
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def deletar_quadra(id):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM quadra WHERE id = %s", (id,))
        conexao.commit()
        return {"message": "Quadra deletada com sucesso"}, 200
    except Exception as erro:
        return {"error": str(erro)}, 500
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()


def cadastrar_quadra(upload_folder):
    data = request.form  # Dados do formulário
    nomeQuadra = data.get("nomeQuadra")
    preco = data.get("preco")
    localizacao = data.get("localizacao")
    descricao = data.get("descricao")

    if not nomeQuadra or not preco or not localizacao or not descricao:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    # Lida com upload de imagem
    if 'foto' not in request.files:
        return jsonify({"error": "Nenhum arquivo enviado"}), 400

    file = request.files['foto']
    if file.filename == '':
        return jsonify({"error": "Arquivo não selecionado"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)

        message, status_code = criar_quadra(nomeQuadra, preco, localizacao, descricao, filepath)
        return jsonify({"message": message}), status_code
    else:
        return jsonify({"error": "Formato de arquivo não suportado"}), 400




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