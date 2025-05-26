from config import db

class Turmas(db.Model):
    __tablename__ = 'turmas'
    id = db.Column(db.Integer, primary_key=True)

    __table_args__ = {'extend_existing': True}