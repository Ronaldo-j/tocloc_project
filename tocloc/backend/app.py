import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from src.database.conexao import criar_conexao
from src.controller.user_controller import (
    cadastrar_user, listar_user_controller, 
    buscar_user_controller, atualizar_user_controller, deletar_user_controller
)
from src.controller.quadra_controller import (
    cadastrar_quadra, listar_quadra_controller,
    buscar_quadra_controller, atualizar_quadra_controller, deletar_quadra_controller
)
from src.controller.reserva_controller import (
    cadastrar_reserva_controller, listar_reservas_controller,
    buscar_reserva_controller, atualizar_reserva_controller, deletar_reserva_controller
)

app = Flask(__name__)
CORS(app)

@app.route('/reserva', methods=['POST'])
def cadastrar_reserva_route():
    return cadastrar_reserva_controller()

@app.route('/reserva', methods=['GET'])
def listar_reservas_route():
    return listar_reservas_controller()

@app.route('/reserva/<int:id>', methods=['GET'])
def buscar_reserva_route(id):
    return buscar_reserva_controller(id)

@app.route('/reserva/<int:id>', methods=['PUT'])
def atualizar_reserva_route(id):
    return atualizar_reserva_controller(id)

@app.route('/reserva/<int:id>', methods=['DELETE'])
def deletar_reserva_route(id):
    return deletar_reserva_controller(id)


# Configuração do upload de arquivos
UPLOAD_FOLDER = 'uploads'  # Diretório onde as imagens serão armazenadas
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Garante que a pasta existe
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limite de 16 MB

@app.route('/quadra', methods=['POST'])
def cadastrar_quadra_route():
    return cadastrar_quadra(app.config['UPLOAD_FOLDER'])


@app.route('/quadra', methods = ['GET'])
def listar_quadra_route():
    return listar_quadra_controller()

@app.route('/quadra/<int:id>', methods = ['GET'])
def buscar_quadra_route(id):
    return buscar_quadra_controller(id)

@app.route('/quadra/<int:id>', methods=['PUT'])
def atualizar_quadra_route(id):
    return atualizar_quadra_controller(id)

@app.route('/quadra/<int:id>', methods=['DELETE'])
def deletar_quadra_route(id):
    return deletar_quadra_controller(id)

@app.route('/user', methods = ['POST'])
def cadastrar_user_route():
    return cadastrar_user()

@app.route('/user', methods = ['GET'])
def listar_user_route():
    return listar_user_controller()

@app.route('/user/<int:id>', methods = ['GET'])
def buscar_user_route(id):
    return buscar_user_controller(id)

@app.route('/user/<int:id>', methods = ['PUT'])
def atualizar_user_route(id):
    return atualizar_user_controller(id)

@app.route('/user/<int:id>', methods=['DELETE'])
def deletar_user_route(id):
    return deletar_user_controller(id)

@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    conexao = criar_conexao()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM user WHERE email = %s AND password = %s",
            (email, password)
        )
        user = cursor.fetchone()
        if user:
            return jsonify({"message": "Login realizado com sucesso", "user": user}), 200
        else:
            return jsonify({"error": "Credenciais inválidas"}), 401
    except Exception as erro:
        return jsonify({"error": str(erro)}), 500
    finally:
        cursor.close()
        conexao.close()


if __name__ == "__main__":
    app.run(debug=True)
