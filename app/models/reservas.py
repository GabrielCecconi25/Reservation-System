from config import db
from datetime import datetime

class Reservas(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    id_sala = db.Column(db.Integer, db.ForeignKey('salas.id'), nullable=False)
    id_turma = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    data_reserva = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fim = db.Column(db.Time, nullable=False)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)

    def serialize(self):
        return {
            'id': self.id,
            'id_sala': self.id_sala,
            'id_turma': self.id_turma,
            'data_reserva': self.data_reserva.strftime('%Y-%m-%d'),
            'hora_inicio': self.hora_inicio.strftime('%H:%M'),
            'hora_fim': self.hora_fim.strftime('%H:%M'),
            'criado_em': self.criado_em.strftime('%Y-%m-%d %H:%M:%S')
        }

    @staticmethod
    def criar_reserva(dados):
        try:
            dados['data_reserva'] = datetime.strptime(dados['data_reserva'], '%Y-%m-%d').date()
            dados['hora_inicio'] = datetime.strptime(dados['hora_inicio'], '%H:%M').time()
            dados['hora_fim'] = datetime.strptime(dados['hora_fim'], '%H:%M').time()
        except ValueError as e:
            raise ValueError((f"Erro ao converter data ou hora: {e}"), 400)

        conflito = Reservas.verificar_conflito(
            dados['id_sala'],
            dados['data_reserva'],
            dados['hora_inicio'],
            dados['hora_fim']
        )
        if conflito:
            raise ValueError((f"Conflito de reserva, horário já reservado"), 409)
        
        nova_reserva = Reservas(
            id_sala=dados['id_sala'],
            id_turma=dados['id_turma'],
            data_reserva=dados['data_reserva'],
            hora_inicio=dados['hora_inicio'],
            hora_fim=dados['hora_fim']
        )

        db.session.add(nova_reserva)
        db.session.commit()
        return nova_reserva.serialize()

    @staticmethod
    def listar():
        return Reservas.query.all()
    
    @staticmethod
    def buscar_por_id(id):
        reserva = Reservas.query.get(id)
        return reserva.serialize() if reserva else None
    
    @staticmethod
    def verificar_conflito(id_sala, data_reserva, hora_inicio, hora_fim):
        return Reservas.query.filter(
            Reservas.id_sala == id_sala,
            Reservas.data_reserva == data_reserva,
            Reservas.hora_inicio < hora_fim,
            Reservas.hora_fim > hora_inicio
        ).first()