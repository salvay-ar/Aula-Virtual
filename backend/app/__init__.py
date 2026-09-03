from flask import Flask

from app.extensions import db
from app.routes import register_routes


def crear_aplicacion():
    aplicacion = Flask(__name__)
    aplicacion.config.from_object("config.Config")
    db.init_app(aplicacion)
    register_routes(aplicacion)
    return aplicacion

from flask import Flask


