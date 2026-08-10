from . import db
from .base import ModeloBase


class Usuario(ModeloBase):
    __tablename__ = "usuarios"

    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    senha_hash = db.Column(db.String(255), nullable=False)

    tarefas = db.relationship("Tarefa", back_populates="usuario")

    @classmethod
    def buscar_por_email(cls, email):
        return cls.query.filter_by(email=email).first()
