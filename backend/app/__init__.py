from flask import Flask

from app.extensions import db


def crear_aplicacion():
    aplicacion = Flask(__name__)
    aplicacion.config.from_object("config.Config")
    db.init_app(aplicacion)

    return aplicacion
