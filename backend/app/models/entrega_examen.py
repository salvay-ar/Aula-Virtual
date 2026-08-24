from datetime import datetime
from backend.app.extensions import db


class EntregaExamen(db.Model):
    __tablename__ = "submissions"

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

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    submitted_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    score = db.Column(
        db.Numeric(5, 2),
        nullable=True
    )


    exam = db.relationship(
        "Examen",
        backref="submissions"
    )

    student = db.relationship(
        "Usuario",
        backref="exam_submissions"
    )

    __table_args__ = (  #es para un estudiante no pueda entregar mas de un examen
        db.UniqueConstraint(
            "exam_id",
            "student_id",
            name="uq_submission_exam_student"
        ),
    )

    def __repr__(self):
        return f"<EntregaExamen examen={self.exam_id} estudiante={self.student_id}>"
