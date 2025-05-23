from flask import jsonify, request
from config import app, db

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
