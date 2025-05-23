from flask import request, jsonify, Blueprint
from models.salas import Salas

salasApp = Blueprint('salas', __name__)

@salasApp.route('/salas', methods=['POST'])
def criar_sala():
    dados = request.get_json()
    try:
        nova_sala = Salas.criar(dados)
        return jsonify({"message": "Sala criada com sucesso", "sala": nova_sala}), 201
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

@salasApp.route('/salas', methods=['GET'])
def listar_salas():
    salas = Salas.listar()
    return jsonify([s.serialize() for s in salas]), 200

@salasApp.route('/salas/<int:id>', methods=['GET'])
def buscar_sala(id):
    sala = Salas.buscar_por_id(id)
    if sala:
        return jsonify(sala), 200
    return jsonify({'erro': 'Sala não encontrada'}), 404
