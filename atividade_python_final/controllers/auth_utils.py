from functools import wraps

from flask import flash, redirect, session, url_for


def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Você precisa entrar para acessar essa página.", "warning")
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)
    return wrapped


def usuario_logado():
    if "usuario_id" in session:
        return {"id": session["usuario_id"], "nome": session.get("usuario_nome")}
    return None
