from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from controllers.auth_utils import login_required
from models import Tarefa
from services import motivacional_service, tarefa_service

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def index():
    if "usuario_id" in session:
        return redirect(url_for("dashboard.dashboard"))
    return redirect(url_for("auth.login"))


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():
    status_filtro = request.args.get("status")
    tarefas = tarefa_service.listar_tarefas(session["usuario_id"], status_filtro)
    frase = motivacional_service.obter_frase_motivacional()

    return render_template(
        "dashboard.html",
        tarefas=tarefas,
        status_filtro=status_filtro or "todas",
        status_labels=Tarefa.STATUS_LABELS,
        status_cores=Tarefa.STATUS_CORES,
        frase=frase,
    )


@dashboard_bp.route("/nova_tarefa", methods=["GET", "POST"])
@login_required
def nova_tarefa():
    if request.method == "POST":
        try:
            tarefa_service.criar_tarefa(request.form, session["usuario_id"])
        except ValueError as erro:
            flash(str(erro), "danger")
            return render_template(
                "nova_tarefa.html",
                status_validos=Tarefa.STATUS_VALIDOS,
                status_labels=Tarefa.STATUS_LABELS,
            )

        flash("Tarefa criada com sucesso!", "success")
        return redirect(url_for("dashboard.dashboard"))

    return render_template(
        "nova_tarefa.html",
        status_validos=Tarefa.STATUS_VALIDOS,
        status_labels=Tarefa.STATUS_LABELS,
    )


@dashboard_bp.route("/editar/<int:tarefa_id>", methods=["GET", "POST"])
@login_required
def editar(tarefa_id):
    tarefa = tarefa_service.buscar_tarefa(tarefa_id, session["usuario_id"])
    if tarefa is None:
        flash("Tarefa não encontrada.", "danger")
        return redirect(url_for("dashboard.dashboard"))

    if request.method == "POST":
        try:
            tarefa_service.atualizar_tarefa(tarefa, request.form)
        except ValueError as erro:
            flash(str(erro), "danger")
            return render_template(
                "editar_tarefa.html",
                tarefa=tarefa,
                status_validos=Tarefa.STATUS_VALIDOS,
                status_labels=Tarefa.STATUS_LABELS,
            )

        flash("Tarefa atualizada com sucesso!", "success")
        return redirect(url_for("dashboard.dashboard"))

    return render_template(
        "editar_tarefa.html",
        tarefa=tarefa,
        status_validos=Tarefa.STATUS_VALIDOS,
        status_labels=Tarefa.STATUS_LABELS,
    )


@dashboard_bp.route("/excluir/<int:tarefa_id>", methods=["POST"])
@login_required
def excluir(tarefa_id):
    tarefa = tarefa_service.buscar_tarefa(tarefa_id, session["usuario_id"])
    if tarefa is None:
        flash("Tarefa não encontrada.", "danger")
    else:
        tarefa_service.excluir_tarefa(tarefa)
        flash("Tarefa excluída com sucesso!", "success")

    return redirect(url_for("dashboard.dashboard"))


@dashboard_bp.route("/progresso")
@login_required
def progresso():
    return render_template("progresso.html")
