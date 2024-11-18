from flask import Flask, jsonify, request
from flask_cors import CORS
from src.database.conexao import criar_conexao
from src.controller.user_controller import(
    cadastrar_user, listar_user_controller,
    buscar_user_controller, atualizar_user_controller, deletar_user_controller
)

app = Flask(__name__)

CORS(app)

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


if __name__ == '__main__':
    app.run(debug=True)