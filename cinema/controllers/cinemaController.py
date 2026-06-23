from datetime import datetime
from flask import Blueprint, redirect, render_template, request, url_for
from models import Filme, Sala, Sessao, db

# Se eu entender e sobrar tempo, depois faço o ingresso

cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema")

@cinema_bp.route("/")
def index():
    sessoes = Sessao.listar_com_detalhes()
    return render_template("cinema/lista_sessoes.html", sessoes=sessoes)

@cinema_bp.route("/sessao/cadastrar", methods=["GET", "POST"])
def cadastrar_sessao():
    filmes = Filme.listar()
    salas = Sala.listar()

    if request.method == "POST":
        filme_id = request.form.get("filme_id")
        sala_id = request.form.get("sala_id")
        data_hora = request.form.get("data_hora")  # precisa converter p/ datetime
        preco = request.form.get("preco")

        nova_sessao = Sessao(
            filme_id=filme_id,
            sala_id=sala_id,
            data_hora=datetime.strptime(data_hora, "%Y-%m-%dT%H:%M"),
            preco=float(preco),
        )
        db.session.add(nova_sessao)
        db.session.commit()
        return redirect(url_for("cinema.index"))

    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
    )
       