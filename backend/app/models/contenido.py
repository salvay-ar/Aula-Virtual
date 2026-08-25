from datetime import datetime

from backend.app.extensions import db


class Contenido(db.Model):
    __tablename__ = "contents"

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

    type = db.Column(
        db.String(20),
        nullable=False
    )

    url = db.Column(
        db.String(500),
        nullable=False
    )

    uploaded_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    course = db.relationship(
        "Curso",
        backref="contents"
    )

    def __repr__(self):
        return f"<Contenido {self.title}>"
