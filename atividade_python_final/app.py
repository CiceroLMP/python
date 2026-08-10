import os

from flask import Flask

from controllers import api_v1_bp, auth_bp, dashboard_bp, rest_bp
from models import db


def criar_app():
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static",
    )

    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "troque-esta-chave-em-producao")
    app.config["DEBUG"] = False 

    pasta = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        pasta, "tarefas.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(rest_bp)
    app.register_blueprint(api_v1_bp)

    @app.context_processor
    def inject_usuario():
        from controllers.auth_utils import usuario_logado
        return {"usuario_logado": usuario_logado()}

    with app.app_context():
        db.create_all()

    return app


app = criar_app()

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
