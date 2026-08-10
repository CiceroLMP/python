from models import Tarefa, db


def listar_tarefas(usuario_id, status=None):
    return Tarefa.listar_por_usuario(usuario_id, status)


def buscar_tarefa(tarefa_id, usuario_id):
    return Tarefa.query.filter_by(id=tarefa_id, usuario_id=usuario_id).first()


def criar_tarefa(dados, usuario_id):

    titulo = str(dados.get("titulo", "")).strip()
    if not titulo:
        raise ValueError("O título da tarefa é obrigatório.")

    status = dados.get("status", "pendente")
    if status not in Tarefa.STATUS_VALIDOS:
        status = "pendente"

    tarefa = Tarefa(
        titulo=titulo,
        descricao=str(dados.get("descricao", "")).strip(),
        status=status,
        usuario_id=usuario_id,
    )
    db.session.add(tarefa)
    db.session.commit()
    return tarefa


def atualizar_tarefa(tarefa, dados):

    if "titulo" in dados:
        titulo = str(dados["titulo"]).strip()
        if not titulo:
            raise ValueError("O título da tarefa é obrigatório.")
        tarefa.titulo = titulo
    if "descricao" in dados:
        tarefa.descricao = str(dados["descricao"]).strip()
    if "status" in dados and dados["status"] in Tarefa.STATUS_VALIDOS:
        tarefa.status = dados["status"]

    db.session.commit()
    return tarefa


def excluir_tarefa(tarefa):
    db.session.delete(tarefa)
    db.session.commit()


def contar_por_status(usuario_id):
    return Tarefa.contar_por_status(usuario_id)


def tarefa_para_dict(tarefa):
    return {
        "id": tarefa.id,
        "titulo": tarefa.titulo,
        "descricao": tarefa.descricao,
        "status": tarefa.status,
        "status_label": Tarefa.STATUS_LABELS.get(tarefa.status, tarefa.status),
        "cor": Tarefa.STATUS_CORES.get(tarefa.status, "secondary"),
        "usuario_id": tarefa.usuario_id,
    }
