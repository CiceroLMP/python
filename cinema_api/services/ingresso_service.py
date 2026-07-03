# services/ingresso_service.py
from models import Ingresso, db


def listar_ingressos():
    return Ingresso.query.order_by(Ingresso.id).all()


def buscar_ingresso(ingresso_id):
    return db.session.get(Ingresso, ingresso_id)


def criar_ingresso(dados):
    # TODO (feito): validar e criar um novo Ingresso a partir do JSON recebido
    ingresso = Ingresso(
        assento=str(dados["assento"]).strip(),
        nome_comprador=str(dados["nome_comprador"]).strip(),
        sessao_id=int(dados["sessao_id"]),
    )
    db.session.add(ingresso)
    db.session.commit()
    return ingresso


def atualizar_ingresso(ingresso, dados):
    # TODO (feito): atualizar só os campos que vieram no JSON
    if "assento" in dados:
        ingresso.assento = str(dados["assento"]).strip()
    if "nome_comprador" in dados:
        ingresso.nome_comprador = str(dados["nome_comprador"]).strip()
    if "sessao_id" in dados:
        ingresso.sessao_id = int(dados["sessao_id"])
    db.session.commit()
    return ingresso


def excluir_ingresso(ingresso):
    db.session.delete(ingresso)
    db.session.commit()


def ingresso_para_dict(ingresso):
    return {
        "id": ingresso.id,
        "assento": ingresso.assento,
        "nome_comprador": ingresso.nome_comprador,
        "sessao_id": ingresso.sessao_id,
    }
