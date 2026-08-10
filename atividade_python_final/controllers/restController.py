from flask import Blueprint, render_template

from controllers.auth_utils import login_required
from models import Tarefa

rest_bp = Blueprint("rest", __name__, url_prefix="/rest")


@rest_bp.route("/")
@login_required
def index():
    return render_template(
        "rest.html",
        status_validos=Tarefa.STATUS_VALIDOS,
        status_labels=Tarefa.STATUS_LABELS,
    )
