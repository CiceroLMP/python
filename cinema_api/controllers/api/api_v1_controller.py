from flask import Blueprint, jsonify, request

from services import filme_service, ingresso_service, sala_service, sessao_service

api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")


# FILMES


@api_v1_bp.route("/filmes", methods=["GET"])
def listar_filmes():
    
    filmes = filme_service.listar_filmes()
    return jsonify([filme_service.filme_para_dict(f) for f in filmes])


@api_v1_bp.route("/filmes/<int:filme_id>", methods=["GET"])
def detalhe_filme(filme_id):
    
    filme = filme_service.buscar_filme(filme_id)
    if not filme:
        return jsonify({"erro": "Filme não encontrado"}), 404
    return jsonify(filme_service.filme_para_dict(filme))


@api_v1_bp.route("/filmes", methods=["POST"])
def criar_filme():
    
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body (Content-Type: application/json)"}), 400

    try:
        filme = filme_service.criar_filme(dados)
    except (KeyError, ValueError, TypeError):
        return jsonify({"erro": "Campos obrigatórios: titulo, duracao_min, classificacao"}), 400

    return jsonify(filme_service.filme_para_dict(filme)), 201


@api_v1_bp.route("/filmes/<int:filme_id>", methods=["PUT"])
def atualizar_filme(filme_id):
    
    filme = filme_service.buscar_filme(filme_id)
    if not filme:
        return jsonify({"erro": "Filme não encontrado"}), 404

    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400

    try:
        filme = filme_service.atualizar_filme(filme, dados)
    except (ValueError, TypeError):
        return jsonify({"erro": "Dados inválidos"}), 400

    return jsonify(filme_service.filme_para_dict(filme))


@api_v1_bp.route("/filmes/<int:filme_id>", methods=["DELETE"])
def excluir_filme(filme_id):
    
    filme = filme_service.buscar_filme(filme_id)
    if not filme:
        return jsonify({"erro": "Filme não encontrado"}), 404

    filme_service.excluir_filme(filme)
    return "", 204


# SALAS


@api_v1_bp.route("/salas", methods=["GET"])
def listar_salas():
    salas = sala_service.listar_salas()
    return jsonify([sala_service.sala_para_dict(s) for s in salas])


@api_v1_bp.route("/salas/<int:sala_id>", methods=["GET"])
def detalhe_sala(sala_id):
    sala = sala_service.buscar_sala(sala_id)
    if not sala:
        return jsonify({"erro": "Sala não encontrada"}), 404
    return jsonify(sala_service.sala_para_dict(sala))


@api_v1_bp.route("/salas", methods=["POST"])
def criar_sala():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body (Content-Type: application/json)"}), 400

    try:
        sala = sala_service.criar_sala(dados)
    except (KeyError, ValueError, TypeError):
        return jsonify({"erro": "Campos obrigatórios: numero, capacidade"}), 400

    return jsonify(sala_service.sala_para_dict(sala)), 201


@api_v1_bp.route("/salas/<int:sala_id>", methods=["PUT"])
def atualizar_sala(sala_id):
    sala = sala_service.buscar_sala(sala_id)
    if not sala:
        return jsonify({"erro": "Sala não encontrada"}), 404

    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400

    try:
        sala = sala_service.atualizar_sala(sala, dados)
    except (ValueError, TypeError):
        return jsonify({"erro": "Dados inválidos"}), 400

    return jsonify(sala_service.sala_para_dict(sala))


@api_v1_bp.route("/salas/<int:sala_id>", methods=["DELETE"])
def excluir_sala(sala_id):
    sala = sala_service.buscar_sala(sala_id)
    if not sala:
        return jsonify({"erro": "Sala não encontrada"}), 404

    sala_service.excluir_sala(sala)
    return "", 204



# SESSÕES


@api_v1_bp.route("/sessoes", methods=["GET"])
def listar_sessoes():
    sessoes = sessao_service.listar_sessoes()
    return jsonify([sessao_service.sessao_para_dict(s) for s in sessoes])


@api_v1_bp.route("/sessoes/<int:sessao_id>", methods=["GET"])
def detalhe_sessao(sessao_id):
    sessao = sessao_service.buscar_sessao(sessao_id)
    if not sessao:
        return jsonify({"erro": "Sessão não encontrada"}), 404
    return jsonify(sessao_service.sessao_para_dict(sessao))


@api_v1_bp.route("/sessoes", methods=["POST"])
def criar_sessao():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body (Content-Type: application/json)"}), 400

    try:
        sessao = sessao_service.criar_sessao(dados)
    except (KeyError, ValueError, TypeError) as erro:
        return jsonify({"erro": f"Dados inválidos: {erro}"}), 400

    return jsonify(sessao_service.sessao_para_dict(sessao)), 201


@api_v1_bp.route("/sessoes/<int:sessao_id>", methods=["PUT"])
def atualizar_sessao(sessao_id):
    sessao = sessao_service.buscar_sessao(sessao_id)
    if not sessao:
        return jsonify({"erro": "Sessão não encontrada"}), 404

    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400

    try:
        sessao = sessao_service.atualizar_sessao(sessao, dados)
    except (ValueError, TypeError) as erro:
        return jsonify({"erro": f"Dados inválidos: {erro}"}), 400

    return jsonify(sessao_service.sessao_para_dict(sessao))


@api_v1_bp.route("/sessoes/<int:sessao_id>", methods=["DELETE"])
def excluir_sessao(sessao_id):
    sessao = sessao_service.buscar_sessao(sessao_id)
    if not sessao:
        return jsonify({"erro": "Sessão não encontrada"}), 404

    sessao_service.excluir_sessao(sessao)
    return "", 204


# ---------------------------------------------------------------------------
# INGRESSOS
# ---------------------------------------------------------------------------

@api_v1_bp.route("/ingressos", methods=["GET"])
def listar_ingressos():
    ingressos = ingresso_service.listar_ingressos()
    return jsonify([ingresso_service.ingresso_para_dict(i) for i in ingressos])


@api_v1_bp.route("/ingressos/<int:ingresso_id>", methods=["GET"])
def detalhe_ingresso(ingresso_id):
    ingresso = ingresso_service.buscar_ingresso(ingresso_id)
    if not ingresso:
        return jsonify({"erro": "Ingresso não encontrado"}), 404
    return jsonify(ingresso_service.ingresso_para_dict(ingresso))


@api_v1_bp.route("/ingressos", methods=["POST"])
def criar_ingresso():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body (Content-Type: application/json)"}), 400

    try:
        ingresso = ingresso_service.criar_ingresso(dados)
    except (KeyError, ValueError, TypeError):
        return jsonify({"erro": "Campos obrigatórios: assento, nome_comprador, sessao_id"}), 400

    return jsonify(ingresso_service.ingresso_para_dict(ingresso)), 201


@api_v1_bp.route("/ingressos/<int:ingresso_id>", methods=["PUT"])
def atualizar_ingresso(ingresso_id):
    ingresso = ingresso_service.buscar_ingresso(ingresso_id)
    if not ingresso:
        return jsonify({"erro": "Ingresso não encontrado"}), 404

    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400

    try:
        ingresso = ingresso_service.atualizar_ingresso(ingresso, dados)
    except (ValueError, TypeError):
        return jsonify({"erro": "Dados inválidos"}), 400

    return jsonify(ingresso_service.ingresso_para_dict(ingresso))


@api_v1_bp.route("/ingressos/<int:ingresso_id>", methods=["DELETE"])
def excluir_ingresso(ingresso_id):
    ingresso = ingresso_service.buscar_ingresso(ingresso_id)
    if not ingresso:
        return jsonify({"erro": "Ingresso não encontrado"}), 404

    ingresso_service.excluir_ingresso(ingresso)
    return "", 204


# ---------------------------------------------------------------------------
# STATUS (health-check simples da API)
# ---------------------------------------------------------------------------

@api_v1_bp.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "API está funcionando"}), 200
