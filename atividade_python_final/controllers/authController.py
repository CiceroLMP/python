from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from services import usuario_service

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        try:
            usuario_service.criar_usuario(request.form)
        except ValueError as erro:
            flash(str(erro), "danger")
            return render_template("registro.html")

        flash("Conta criada com sucesso! Faça login.", "success")
        return redirect(url_for("auth.login"))

    return render_template("registro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "")
        senha = request.form.get("senha", "")

        usuario = usuario_service.autenticar(email, senha)
        if usuario is None:
            flash("E-mail ou senha inválidos.", "danger")
            return render_template("login.html")

        session.clear()
        session["usuario_id"] = usuario.id
        session["usuario_nome"] = usuario.nome
        flash(f"Bem-vindo(a), {usuario.nome}!", "success")
        return redirect(url_for("dashboard.index"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("Você saiu da sua conta.", "info")
    return redirect(url_for("auth.login"))
