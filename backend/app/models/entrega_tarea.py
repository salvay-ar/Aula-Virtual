from datetime import datetime

from backend.app.extensions import db


class EntregaTarea(db.Model):
    __tablename__ = "task_submissions"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    task_id = db.Column(
        db.Integer,
        db.ForeignKey("tasks.id"),
        nullable=False
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    submission_url = db.Column(
        db.String(500),
        nullable=True
    )

    submission_text = db.Column(
        db.Text,
        nullable=True
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

    feedback = db.Column(
        db.Text,
        nullable=True
    )

    task = db.relationship(
        "Tarea",
        backref="submissions"
    )

    student = db.relationship(
        "Usuario",
        backref="task_submissions"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "task_id",
            "student_id",
            name="uq_task_submission_student"
        ),
    )

    def __repr__(self):
        return f"<EntregaTarea tarea={self.task_id} estudiante={self.student_id}>"
