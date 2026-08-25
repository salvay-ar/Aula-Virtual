from backend.app.extensions import db


class Opcion(db.Model):
    __tablename__ = "options"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    question_id = db.Column(
        db.Integer,
        db.ForeignKey("questions.id"),
        nullable=False
    )

    text = db.Column(
        db.String(500),
        nullable=False
    )

    is_correct = db.Column(
        db.Boolean,
        nullable=False,
        default=False
    )

    question = db.relationship(
        "Pregunta",
        backref="options"
    )

    def __repr__(self):
        return f"<Opcion {self.text}>"
