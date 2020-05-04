# flask's CLI will automatically search for a Callable named "create_app"
# see https://github.com/pallets/flask/blob/master/src/flask/cli.py
from .app import create_app

if __name__ == '__main__':
    from .config import TestingConfig
    app = create_app(config=TestingConfig)
    app.run()
