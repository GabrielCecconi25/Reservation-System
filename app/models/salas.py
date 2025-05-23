from config import db

class Salas(db.Model):
    __tablename__ = 'salas'

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10), nullable=False)
    descricao = db.Column(db.String(100), nullable=True)

    reservas = db.relationship('Reservas', backref='sala', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'numero': self.numero,
            'descricao': self.descricao
        }

    @staticmethod
    def criar(dados):
        if not dados.get('numero'):
            raise ValueError(("Campo 'numero' é obrigatório."), 400)

        nova_sala = Salas(
            numero=dados['numero'],
            descricao=dados.get('descricao')
        )
        db.session.add(nova_sala)
        db.session.commit()
        return nova_sala.serialize()

    @staticmethod
    def listar():
        return Salas.query.all()

    @staticmethod
    def buscar_por_id(id):
        sala = Salas.query.get(id)
        return sala.serialize() if sala else None
