from datetime import datetime

from backend.app.extensions import db


class Tarea(db.Model):
    __tablename__ = "tasks"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    content_id = db.Column(
        db.Integer,
        db.ForeignKey("contents.id"),
        nullable=True
    )

    activity_type = db.Column(
        db.String(20),
        nullable=False
    )

    activity_url = db.Column(
        db.String(500),
        nullable=True
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="draft"
    )

    uploaded_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    deadline = db.Column(
        db.DateTime,
        nullable=True
    )

    course = db.relationship(
        "Curso",
        backref="tasks"
    )

    content = db.relationship(
        "Contenido",
        backref="tasks"
    )

    def __repr__(self):
        return f"<Tarea {self.title}>"
