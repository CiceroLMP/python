from flask import Blueprint, jsonify, request, session

from controllers.auth_utils import login_required
from models import Tarefa
from services import tarefa_service

api_v1_bp = Blueprint("api_v1", __name__, url_prefix="/api/v1")


@api_v1_bp.route("/tarefas", methods=["GET"])
@login_required
def listar_tarefas():
    status = request.args.get("status")
    tarefas = tarefa_service.listar_tarefas(session["usuario_id"], status)
    return jsonify([tarefa_service.tarefa_para_dict(t) for t in tarefas])


@api_v1_bp.route("/tarefas/<int:tarefa_id>", methods=["GET"])
@login_required
def detalhe_tarefa(tarefa_id):
    tarefa = tarefa_service.buscar_tarefa(tarefa_id, session["usuario_id"])
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    return jsonify(tarefa_service.tarefa_para_dict(tarefa))


@api_v1_bp.route("/tarefas", methods=["POST"])
@login_required
def criar_tarefa():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body (Content-Type: application/json)"}), 400

    try:
        tarefa = tarefa_service.criar_tarefa(dados, session["usuario_id"])
    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400

    return jsonify(tarefa_service.tarefa_para_dict(tarefa)), 201


@api_v1_bp.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
@login_required
def atualizar_tarefa(tarefa_id):
    tarefa = tarefa_service.buscar_tarefa(tarefa_id, session["usuario_id"])
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Envie JSON no body"}), 400

    try:
        tarefa = tarefa_service.atualizar_tarefa(tarefa, dados)
    except ValueError as erro:
        return jsonify({"erro": str(erro)}), 400

    return jsonify(tarefa_service.tarefa_para_dict(tarefa))


@api_v1_bp.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
@login_required
def excluir_tarefa(tarefa_id):
    tarefa = tarefa_service.buscar_tarefa(tarefa_id, session["usuario_id"])
    if not tarefa:
        return jsonify({"erro": "Tarefa não encontrada"}), 404

    tarefa_service.excluir_tarefa(tarefa)
    return "", 204



@api_v1_bp.route("/progresso", methods=["GET"])
@login_required
def progresso():
    contagem = tarefa_service.contar_por_status(session["usuario_id"])
    return jsonify({
        "labels": [Tarefa.STATUS_LABELS[s] for s in Tarefa.STATUS_VALIDOS],
        "valores": [contagem[s] for s in Tarefa.STATUS_VALIDOS],
        "cores": ["#ffc107", "#0d6efd", "#198754"],  # amarelo, azul, verde
    })




@api_v1_bp.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "API está funcionando"}), 200
