from datetime import datetime

from backend.app.extensions import db


class Curso(db.Model):
    __tablename__ = "courses"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    instructor_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
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

    instructor = db.relationship(
        "Usuario",
        backref="courses"
    )

    def __repr__(self):
        return f"<Curso {self.name}>"
