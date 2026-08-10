from . import db
from .base import ModeloBase


class Tarefa(ModeloBase):
    __tablename__ = "tarefas"

    STATUS_VALIDOS = ["pendente", "em_andamento", "concluida"]

    STATUS_LABELS = {
        "pendente": "Pendente",
        "em_andamento": "Em andamento",
        "concluida": "Concluída",
    }

   
    STATUS_CORES = {
        "pendente": "warning",
        "em_andamento": "primary",
        "concluida": "success",
    }

    titulo = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), nullable=False, default="pendente")

    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    usuario = db.relationship("Usuario", back_populates="tarefas")

    @classmethod
    def listar_por_usuario(cls, usuario_id, status=None):
        consulta = cls.query.filter_by(usuario_id=usuario_id)
        if status in cls.STATUS_VALIDOS:
            consulta = consulta.filter_by(status=status)
        return consulta.order_by(cls.id.desc()).all()

    @classmethod
    def contar_por_status(cls, usuario_id):
        contagem = {status: 0 for status in cls.STATUS_VALIDOS}
        linhas = (
            db.session.query(cls.status, db.func.count(cls.id))
            .filter_by(usuario_id=usuario_id)
            .group_by(cls.status)
            .all()
        )
        for status, total in linhas:
            contagem[status] = total
        return contagem
