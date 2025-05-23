from flask import jsonify, request
from config import app, db
from controller.sala import salasApp
from controller.reserva import reservasApp  # novo import do controller de reservas

# Registro dos Blueprints
app.register_blueprint(salasApp, url_prefix='/')
app.register_blueprint(reservasApp, url_prefix='/salas')  # adiciona o blueprint de reservas

# Criação das tabelas no banco
with app.app_context():
    db.create_all()

# Inicialização do servidor
if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
