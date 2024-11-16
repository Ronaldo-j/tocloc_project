from flask import Flask
from flask_cors import CORS
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

if __name__ == '__main__':
    app.run(debug=True)