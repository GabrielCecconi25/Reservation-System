from flask import request, jsonify, Blueprint
from flasgger import swag_from

from datetime import datetime

from models.reservas import Reservas
from config import db


reservasApp = Blueprint('reservas', __name__)

@reservasApp.route('/reservas', methods=['POST'])
@swag_from('docs/reservas/post.yml')
def criar_reserva():
    dados = request.json
    try:
        nova_reserva = Reservas.criar_reserva(dados)
        return jsonify({"message": "Sala reservada com sucesso"}), 201
    except ValueError as e:
        return jsonify({"erro": str(e.args[0])}), e.args[1]

@reservasApp.route('/reservas', methods=['GET'])
@swag_from('docs/reservas/get_all.yml')
def listar_reservas():
    reservas = Reservas.listar()
    return jsonify([r.serialize() for r in reservas]), 200

@reservasApp.route('/reservas/<int:id>', methods=['GET'])
@swag_from('docs/reservas/get_by_id.yml')
def buscar_reserva(id):
    reserva = Reservas.buscar_por_id(id)
    if reserva:
        return jsonify(reserva), 200
    return jsonify({'erro': 'Reserva não encontrada'}), 404
