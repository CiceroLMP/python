from werkzeug.security import check_password_hash, generate_password_hash

from models import Usuario, db


def buscar_usuario(usuario_id):
    return db.session.get(Usuario, usuario_id)


def criar_usuario(dados):

    nome = str(dados.get("nome", "")).strip()
    email = str(dados.get("email", "")).strip().lower()
    senha = str(dados.get("senha", ""))

    if not nome or not email or not senha:
        raise ValueError("Preencha nome, e-mail e senha.")

    if len(senha) < 6:
        raise ValueError("A senha deve ter pelo menos 6 caracteres.")

    if Usuario.buscar_por_email(email):
        raise ValueError("Já existe uma conta com esse e-mail.")

    usuario = Usuario(
        nome=nome,
        email=email,
        senha_hash=generate_password_hash(senha),
    )
    db.session.add(usuario)
    db.session.commit()
    return usuario


def autenticar(email, senha):
    email = str(email).strip().lower()
    usuario = Usuario.buscar_por_email(email)

    if usuario is None or not check_password_hash(usuario.senha_hash, senha):
        return None
    return usuario
