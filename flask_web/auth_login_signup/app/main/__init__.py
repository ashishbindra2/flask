from flask import Flask
from config import Config
from flask import Blueprint

main_bp = Blueprint('main', __name__)

from app.main import routes


def create_app(config_class=Config):
    # Initialize Flask extensions here
    app = Flask(__name__)
    app.config.from_object(config_class)
    # Register blueprints here
    app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app


