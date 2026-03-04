from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app


# creamos la app aplicacion
application = create_app() # <- esto es lo que WSGI va a importar


