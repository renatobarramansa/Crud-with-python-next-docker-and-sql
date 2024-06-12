# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


import os
from dotenv import load_dotenv

load_dotenv()

DB_SERVER = os.getenv('DB_SERVER')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

SQLALCHEMY_DATABASE_URI = f'mssql+pymssql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}'
SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
db = SQLAlchemy(app)




from backend.model.usuario import Usuario
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuario.get_all()
    print(usuarios)
    return jsonify([{'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email} for usuario in usuarios])
    

# @app.route('/usuarios', methods=['POST'])
# def add_usuario():
#     data = request.json
#     novo_usuario = Usuario.create(nome=data['nome'], email=data['email'])
#     return jsonify({'id': novo_usuario.id, 'nome': novo_usuario.nome, 'email': novo_usuario.email}), 201

# @app.route('/usuarios/<int:id>', methods=['PUT'])
# def update_usuario(id):
#     data = request.json
#     usuario = Usuario.update(id, nome=data['nome'], email=data['email'])
#     if usuario:
#         return jsonify({'id': usuario.id, 'nome': usuario.nome, 'email': usuario.email})
#     return jsonify({'message': 'Usuário não encontrado'}), 404

# @app.route('/usuarios/<int:id>', methods=['DELETE'])
# def delete_usuario(id):
#     success = Usuario.delete(id)
#     if success:
#         return jsonify({'message': 'Usuário deletado com sucesso'}), 200
#     return jsonify({'message': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
