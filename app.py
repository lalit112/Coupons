"""
This module is the entry point for application
"""

import os.path
from flask import Flask
from authentication.auth_login import authenticate
from database.models import db
from src.generate_coupon import generate_coupon
from src.fetch_coupon import fetch_coupon


def create_app():
    """
    Factory function for creating flask app
    :return: app instance
    """
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    app.register_blueprint(generate_coupon, url_prefix='/generate')
    app.register_blueprint(fetch_coupon, url_prefix='/fetch')
    app.register_blueprint(authenticate, url_prefix='/auth')
    return app


def setup_database(app):
    """
    Function for setting up data base
    :param app: flask app instance
    :return: None
    """
    with app.app_context():
        db.create_all()
        db.session.commit()


# if __name__ == '__main__':
#     app = create_app()
#     print (os.path)
#     if not os.path.isfile('instance/discount.db'):
#         setup_database(app)
#     app.run()
