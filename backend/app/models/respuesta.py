from backend.app.extensions import db


class Respuesta(db.Model):
    __tablename__ = "answers"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    submission_id = db.Column(
        db.Integer,
        db.ForeignKey("submissions.id"),
        nullable=False
    )

    question_id = db.Column(
        db.Integer,
        db.ForeignKey("questions.id"),
        nullable=False
    )

    answer_text = db.Column(
        db.Text,
        nullable=True
    )

    selected_option_id = db.Column(
        db.Integer,
        db.ForeignKey("options.id"),
        nullable=True
    )


    submission = db.relationship(
        "EntregaExamen",
        backref="answers"
    )

    question = db.relationship(
        "Pregunta",
        backref="answers"
    )

    selected_option = db.relationship(
        "Opcion",
        backref="answers"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "submission_id",
            "question_id",
            name="uq_answer_submission_question"
        ),
    )

    def __repr__(self):
        return f"<Respuesta pregunta={self.question_id}>"
