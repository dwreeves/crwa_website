from flask import Blueprint

bp = Blueprint('flagging', __name__)


@bp.route('/')
def main() -> str:
    return 'Hello, world! This will be a website some day!'
