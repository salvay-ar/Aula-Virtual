from .cursos import course_bp
from .usuarios import user_bp
from .auth import auth_bp


def register_routes(app):
    app.register_blueprint(course_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)