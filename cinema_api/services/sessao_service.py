# services/sessao_service.py
from datetime import datetime

from models import Sessao, db


def listar_sessoes():
    return Sessao.listar_com_detalhes()


def buscar_sessao(sessao_id):
    return db.session.get(Sessao, sessao_id)


def _parse_data_hora(valor):
    # Aceita tanto "2026-07-03T20:00" (input do form HTML) quanto
    # "2026-07-03 20:00:00" (formato mais "cru" que pode vir de um JSON).
    for formato in ("%Y-%m-%dT%H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d %H:%M"):
        try:
            return datetime.strptime(valor, formato)
        except ValueError:
            continue
    raise ValueError("data_hora em formato inválido. Use AAAA-MM-DDTHH:MM")


def criar_sessao(dados):
    # TODO (feito): validar e criar uma nova Sessao a partir do JSON recebido
    sessao = Sessao(
        filme_id=int(dados["filme_id"]),
        sala_id=int(dados["sala_id"]),
        data_hora=_parse_data_hora(str(dados["data_hora"])),
        preco=float(dados["preco"]),
    )
    db.session.add(sessao)
    db.session.commit()
    return sessao


def atualizar_sessao(sessao, dados):
    # TODO (feito): atualizar só os campos que vieram no JSON
    if "filme_id" in dados:
        sessao.filme_id = int(dados["filme_id"])
    if "sala_id" in dados:
        sessao.sala_id = int(dados["sala_id"])
    if "data_hora" in dados:
        sessao.data_hora = _parse_data_hora(str(dados["data_hora"]))
    if "preco" in dados:
        sessao.preco = float(dados["preco"])
    db.session.commit()
    return sessao


def excluir_sessao(sessao):
    db.session.delete(sessao)
    db.session.commit()


def sessao_para_dict(sessao):
    return {
        "id": sessao.id,
        "filme_id": sessao.filme_id,
        "filme_titulo": sessao.filme.titulo if sessao.filme else None,
        "sala_id": sessao.sala_id,
        "sala_numero": sessao.sala.numero if sessao.sala else None,
        "data_hora": sessao.data_hora.strftime("%Y-%m-%d %H:%M"),
        "preco": sessao.preco,
    }
