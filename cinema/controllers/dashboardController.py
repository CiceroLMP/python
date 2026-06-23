from flask import Blueprint, render_template
from models import Filme, Sala, Sessao
 
dashboard_bp = Blueprint("dashboard", __name__)
 
@dashboard_bp.route("/")
def index():
    total_filmes = Filme.query.count()
    total_salas = Sala.query.count()
    total_sessoes = Sessao.query.count()
    return render_template(
        "index.html",
        total_filmes=total_filmes,
        total_salas=total_salas,
        total_sessoes=total_sessoes,
    )