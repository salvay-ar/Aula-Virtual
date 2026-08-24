from datetime import datetime

from backend.app.extensions import db


class Examen(db.Model):
    __tablename__ = "exams"

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

    available_from = db.Column(
        db.DateTime,
        nullable=True
    )

    available_until = db.Column(
        db.DateTime,
        nullable=True
    )

    status = db.Column(
        db.String(20),
        nullable=False,
        default="draft"
    )

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    course = db.relationship(
        "Curso",
        backref="exams"
    )

    def __repr__(self):
        return f"<Examen {self.title}>"
