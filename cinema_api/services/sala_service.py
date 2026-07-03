# services/sala_service.py
from models import Sala, db


def listar_salas():
    return Sala.listar()


def buscar_sala(sala_id):
    return db.session.get(Sala, sala_id)


def criar_sala(dados):
    # TODO (feito): validar e criar uma nova Sala a partir do JSON recebido
    sala = Sala(
        numero=int(dados["numero"]),
        capacidade=int(dados["capacidade"]),
    )
    db.session.add(sala)
    db.session.commit()
    return sala


def atualizar_sala(sala, dados):
    # TODO (feito): atualizar só os campos que vieram no JSON
    if "numero" in dados:
        sala.numero = int(dados["numero"])
    if "capacidade" in dados:
        sala.capacidade = int(dados["capacidade"])
    db.session.commit()
    return sala


def excluir_sala(sala):
    db.session.delete(sala)
    db.session.commit()


def sala_para_dict(sala):
    return {
        "id": sala.id,
        "numero": sala.numero,
        "capacidade": sala.capacidade,
    }
