from flask import Blueprint, jsonify, request

from backend.app.extensions import db
from backend.app.models.curso import Curso
from backend.app.models.usuario import Usuario


course_bp = Blueprint("courses", __name__)


@course_bp.route("/courses", methods=["GET"])
def obtener_cursos():

    cursos = Curso.query.all()

    return jsonify([
        {
            "id": curso.id,
            "name": curso.name,
            "description": curso.description,
            "instructor_id": curso.instructor_id,
            "status": curso.status,
            "created_at": curso.created_at.isoformat()
        }
        for curso in cursos
    ]), 200


@course_bp.route("/courses/<int:id>", methods=["GET"])
def obtener_curso(id):

    curso = Curso.query.get(id)

    if not curso:
        return jsonify({
            "error": "Curso no encontrado"
        }), 404

    return jsonify({
        "id": curso.id,
        "name": curso.name,
        "description": curso.description,
        "instructor_id": curso.instructor_id,
        "status": curso.status,
        "created_at": curso.created_at.isoformat()
    }), 200


@course_bp.route("/courses", methods=["POST"])
def crear_curso():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No se recibieron datos"
        }), 400

    name = data.get("name")
    description = data.get("description")
    instructor_id = data.get("instructor_id")
    status = data.get("status", "draft")

    if not name:
        return jsonify({
            "error": "El nombre del curso es obligatorio"
        }), 400

    if not instructor_id:
        return jsonify({
            "error": "El instructor_id es obligatorio"
        }), 400

    instructor = Usuario.query.get(instructor_id)

    if not instructor:
        return jsonify({
            "error": "El instructor no existe"
        }), 404

    if instructor.role != "instructor":
        return jsonify({
            "error": "El usuario seleccionado no tiene el rol de instructor"
        }), 400

    estados_validos = ["draft", "published", "archived"]

    if status not in estados_validos:
        return jsonify({
            "error": "Status inválido. Debe ser draft, published o archived"
        }), 400

    nuevo_curso = Curso(
        name=name,
        description=description,
        instructor_id=instructor_id,
        status=status
    )

    db.session.add(nuevo_curso)
    db.session.commit()

    return jsonify({
        "mensaje": "Curso creado correctamente",
        "curso": {
            "id": nuevo_curso.id,
            "name": nuevo_curso.name,
            "description": nuevo_curso.description,
            "instructor_id": nuevo_curso.instructor_id,
            "status": nuevo_curso.status,
            "created_at": nuevo_curso.created_at.isoformat()
        }
    }), 201


@course_bp.route("/courses/<int:id>", methods=["PUT"])
def modificar_curso(id):

    curso = Curso.query.get(id)

    if not curso:
        return jsonify({
            "error": "Curso no encontrado"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No se recibieron datos"
        }), 400

    if "name" in data:

        if not data["name"]:
            return jsonify({
                "error": "El nombre del curso no puede estar vacío"
            }), 400

        curso.name = data["name"]

    if "description" in data:
        curso.description = data["description"]

    if "instructor_id" in data:

        instructor = Usuario.query.get(data["instructor_id"])

        if not instructor:
            return jsonify({
                "error": "El instructor no existe"
            }), 404

        if instructor.role != "instructor":
            return jsonify({
                "error": "El usuario seleccionado no tiene el rol de instructor"
            }), 400

        curso.instructor_id = data["instructor_id"]

    if "status" in data:

        estados_validos = ["draft", "published", "archived"]

        if data["status"] not in estados_validos:
            return jsonify({
                "error": "Status inválido. Debe ser draft, published o archived"
            }), 400

        curso.status = data["status"]

    db.session.commit()

    return jsonify({
        "mensaje": "Curso modificado correctamente",
        "curso": {
            "id": curso.id,
            "name": curso.name,
            "description": curso.description,
            "instructor_id": curso.instructor_id,
            "status": curso.status,
            "created_at": curso.created_at.isoformat()
        }
    }), 200


@course_bp.route("/courses/<int:id>", methods=["DELETE"])
def eliminar_curso(id):

    curso = Curso.query.get(id)

    if not curso:
        return jsonify({
            "error": "Curso no encontrado"
        }), 404

    db.session.delete(curso)
    db.session.commit()

    return jsonify({
        "mensaje": "Curso eliminado correctamente"
    }), 200