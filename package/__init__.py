from flask import Flask

from package.db.mongodb import init_db
from package.routes.product import product_bp


def create_app():
    # instantiate the Flask app
    app = Flask(__name__)

    # initialize db
    init_db()

    # register the product blueprints
    app.register_blueprint(product_bp, url_prefix="/product")

    return app
