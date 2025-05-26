from flask import jsonify, request
from config import app, db
from controller.sala import salasApp
from controller.reserva import reservasApp  # novo import do controller de reservas

# Importe os models necessários (mesmo os que não serão criados)
from models.salas import Salas
from models.reservas import Reservas
from models.turmas_dummy import Turmas

# Registro dos Blueprints
app.register_blueprint(salasApp, url_prefix='/')
app.register_blueprint(reservasApp, url_prefix='/salas')  # adiciona o blueprint de reservas

# Criação das tabelas no banco
with app.app_context():
    db.create_all()

#### ROTA RESETAR DADOS ####
@app.route('/salas/resetar', methods=['POST'])
async def resetar_dados():
    from models.salas import Salas
    from models.reservas import Reservas
    
    Reservas.query.delete()
    Salas.query.delete()
    
    db.session.commit()
    return jsonify({"mensagem": "Dados resetados com sucesso!"}), 200


# Inicialização do servidor
if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )
