# services/filme_service.py
# Camada de Service: regras de negócio + conversão pra dict.
# O Controller da API chama essas funções em vez de falar direto com o Model.
# Assim o Model continua "limpo" (não precisamos alterar models/filme.py).

from models import Filme, db


def listar_filmes():
    return Filme.listar()


def buscar_filme(filme_id):
    return db.session.get(Filme, filme_id)


def criar_filme(dados):
    # TODO (feito): validar e criar um novo Filme a partir do JSON recebido
    filme = Filme(
        titulo=str(dados["titulo"]).strip(),
        duracao_min=int(dados["duracao_min"]),
        classificacao=str(dados["classificacao"]).strip(),
    )
    db.session.add(filme)
    db.session.commit()
    return filme


def atualizar_filme(filme, dados):
    # TODO (feito): atualizar só os campos que vieram no JSON
    if "titulo" in dados:
        filme.titulo = str(dados["titulo"]).strip()
    if "duracao_min" in dados:
        filme.duracao_min = int(dados["duracao_min"])
    if "classificacao" in dados:
        filme.classificacao = str(dados["classificacao"]).strip()
    db.session.commit()
    return filme


def excluir_filme(filme):
    db.session.delete(filme)
    db.session.commit()


def filme_para_dict(filme):
    return {
        "id": filme.id,
        "titulo": filme.titulo,
        "duracao_min": filme.duracao_min,
        "classificacao": filme.classificacao,
    }
