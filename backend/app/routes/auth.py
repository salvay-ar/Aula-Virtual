from flask import Blueprint, jsonify, request, session
from werkzeug.security import check_password_hash

from backend.app.models.usuario import Usuario


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No se recibieron datos"
        }), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "error": "Email y contraseña son obligatorios"
        }), 400

    usuario = Usuario.query.filter_by(email=email).first()

    if not usuario:
        return jsonify({
            "error": "Email o contraseña incorrectos"
        }), 401

    if not check_password_hash(usuario.password_hash, password):
        return jsonify({
            "error": "Email o contraseña incorrectos"
        }), 401

    if not usuario.is_active:
        return jsonify({
            "error": "El usuario está inactivo"
        }), 403

    session["user_id"] = usuario.id
    session["role"] = usuario.role

    return jsonify({
        "mensaje": "Inicio de sesión correcto",
        "usuario": {
            "id": usuario.id,
            "name": usuario.name,
            "email": usuario.email,
            "role": usuario.role
        }
    }), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():

    session.clear()

    return jsonify({
        "mensaje": "Sesión cerrada correctamente"
    }), 200


@auth_bp.route("/me", methods=["GET"])
def usuario_actual():

    user_id = session.get("user_id")

    if not user_id:
        return jsonify({
            "error": "No hay una sesión iniciada"
        }), 401

    usuario = Usuario.query.get(user_id)

    if not usuario:
        session.clear()

        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    return jsonify({
        "id": usuario.id,
        "name": usuario.name,
        "email": usuario.email,
        "role": usuario.role,
        "is_active": usuario.is_active
    }), 200