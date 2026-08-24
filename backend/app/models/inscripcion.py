from datetime import datetime

from backend.app.extensions import db


class Inscripcion(db.Model):
    __tablename__ = "enrollments"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    course_id = db.Column(
        db.Integer,
        db.ForeignKey("courses.id"),
        nullable=False
    )

    enrolled_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    student = db.relationship(
        "Usuario",
        backref="enrollments"
    )

    course = db.relationship(
        "Curso",
        backref="enrollments"
    )

    __table_args__ = (
        db.UniqueConstraint(
            "student_id",
            "course_id",
            name="uq_enrollment_student_course"
        ),
    )

    def __repr__(self):
        return f"<Inscripcion estudiante={self.student_id} curso={self.course_id}>"
