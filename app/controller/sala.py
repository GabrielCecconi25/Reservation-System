from flask import request, jsonify, Blueprint
from flasgger import swag_from

from models.salas import Salas

salasApp = Blueprint('salas', __name__)

@salasApp.route('/salas', methods=['POST'])
@swag_from('../docs/salas/post.yml')
def criar_sala():
    dados = request.get_json()
    try:
        nova_sala = Salas.criar(dados)
        return jsonify({"message": "Sala criada com sucesso", "sala": nova_sala}), 201
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

@salasApp.route('/salas', methods=['GET'])
@swag_from('../docs/salas/get_all.yml')
def listar_salas():
    salas = Salas.listar()
    return jsonify([s.serialize() for s in salas]), 200

@salasApp.route('/salas/<int:id>', methods=['GET'])
@swag_from('../docs/salas/get_by_id.yml')
def buscar_sala(id):
    sala = Salas.buscar_por_id(id)
    if sala:
        return jsonify(sala), 200
    return jsonify({'erro': 'Sala não encontrada'}), 404
