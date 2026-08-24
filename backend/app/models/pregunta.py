from backend.app.extensions import db


class Pregunta(db.Model):
    __tablename__ = "questions"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    exam_id = db.Column(
        db.Integer,
        db.ForeignKey("exams.id"),
        nullable=False
    )

    statement = db.Column(
        db.Text,
        nullable=False
    )

    type = db.Column(
        db.String(30),
        nullable=False
    )

    points = db.Column(
        db.Numeric(5, 2),
        nullable=False,
        default=1
    )

    exam = db.relationship(
        "Examen",
        backref="questions"
    )

    def __repr__(self):
        return f"<Pregunta {self.id}>"
