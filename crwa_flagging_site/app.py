"""
This file handles the construction of the Flask application object.
"""
import os
from typing import ClassVar
from flask import Flask
from .config import ProductionConfig


def create_app(config: ClassVar = None) -> Flask:
    """Create and configure an instance of the Flask application.

    Args:
        config: Can be either a string such as `config.BaseConfig`, or the
                actual object itself.
    """
    app = Flask(__name__, instance_relative_config=True)

    # Get a config for the website. If one was not passed in the function, then
    # the `ProductionConfig` will be used.
    app.config.from_object(config or ProductionConfig)

    # Register the "blueprints." Blueprints are basically like mini web apps
    # that can be joined to the main web app.
    from .blueprints import flagging, cyanobacteria
    app.register_blueprint(flagging.bp)
    app.register_blueprint(cyanobacteria.bp)

    # Register the database commands
    # from .data import db
    # db.init_app(app)

    # And we're all set! We can hand the app over to flask at this point.
    return app


if __name__ == '__main__':
    from .config import TestingConfig
    app = create_app(config=TestingConfig)
    app.run()
