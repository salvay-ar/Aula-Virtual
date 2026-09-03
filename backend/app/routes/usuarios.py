from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash

from backend.app.extensions import db
from backend.app.models.usuario import Usuario


user_bp = Blueprint("users", __name__)


@user_bp.route("/users", methods=["GET"])
def obtener_usuarios():

    usuarios = Usuario.query.all()

    return jsonify([
        {
            "id": usuario.id,
            "name": usuario.name,
            "email": usuario.email,
            "role": usuario.role,
            "is_active": usuario.is_active,
            "created_at": usuario.created_at.isoformat()
        }
        for usuario in usuarios
    ]), 200


@user_bp.route("/users/<int:id>", methods=["GET"])
def obtener_usuario(id):

    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    return jsonify({
        "id": usuario.id,
        "name": usuario.name,
        "email": usuario.email,
        "role": usuario.role,
        "is_active": usuario.is_active,
        "created_at": usuario.created_at.isoformat()
    }), 200


@user_bp.route("/users", methods=["POST"])
def crear_usuario():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No se recibieron datos"
        }), 400

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")
    is_active = data.get("is_active", True)

    if not name:
        return jsonify({
            "error": "El nombre es obligatorio"
        }), 400

    if not email:
        return jsonify({
            "error": "El email es obligatorio"
        }), 400

    if not password:
        return jsonify({
            "error": "La contraseña es obligatoria"
        }), 400

    if not role:
        return jsonify({
            "error": "El rol es obligatorio"
        }), 400

    roles_validos = ["admin", "instructor", "student"]

    if role not in roles_validos:
        return jsonify({
            "error": "Rol inválido. Debe ser admin, instructor o student"
        }), 400

    usuario_existente = Usuario.query.filter_by(email=email).first()

    if usuario_existente:
        return jsonify({
            "error": "El email ya está registrado"
        }), 409

    password_hash = generate_password_hash(password)

    nuevo_usuario = Usuario(
        name=name,
        email=email,
        password_hash=password_hash,
        role=role,
        is_active=is_active
    )

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({
        "mensaje": "Usuario creado correctamente",
        "usuario": {
            "id": nuevo_usuario.id,
            "name": nuevo_usuario.name,
            "email": nuevo_usuario.email,
            "role": nuevo_usuario.role,
            "is_active": nuevo_usuario.is_active,
            "created_at": nuevo_usuario.created_at.isoformat()
        }
    }), 201


@user_bp.route("/users/<int:id>", methods=["PUT"])
def modificar_usuario(id):

    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No se recibieron datos"
        }), 400

    if "name" in data:

        if not data["name"]:
            return jsonify({
                "error": "El nombre no puede estar vacío"
            }), 400

        usuario.name = data["name"]

    if "email" in data:

        if not data["email"]:
            return jsonify({
                "error": "El email no puede estar vacío"
            }), 400

        usuario_existente = Usuario.query.filter(
            Usuario.email == data["email"],
            Usuario.id != id
        ).first()

        if usuario_existente:
            return jsonify({
                "error": "El email ya está registrado"
            }), 409

        usuario.email = data["email"]

    if "password" in data:

        if not data["password"]:
            return jsonify({
                "error": "La contraseña no puede estar vacía"
            }), 400

        usuario.password_hash = generate_password_hash(data["password"])

    if "role" in data:

        roles_validos = ["admin", "instructor", "student"]

        if data["role"] not in roles_validos:
            return jsonify({
                "error": "Rol inválido. Debe ser admin, instructor o student"
            }), 400

        usuario.role = data["role"]

    if "is_active" in data:
        usuario.is_active = data["is_active"]

    db.session.commit()

    return jsonify({
        "mensaje": "Usuario modificado correctamente",
        "usuario": {
            "id": usuario.id,
            "name": usuario.name,
            "email": usuario.email,
            "role": usuario.role,
            "is_active": usuario.is_active,
            "created_at": usuario.created_at.isoformat()
        }
    }), 200


@user_bp.route("/users/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):

    usuario = Usuario.query.get(id)

    if not usuario:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    db.session.delete(usuario)
    db.session.commit()

    return jsonify({
        "mensaje": "Usuario eliminado correctamente"
    }), 200