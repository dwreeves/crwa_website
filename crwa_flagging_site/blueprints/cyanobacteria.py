from flask import Blueprint

bp = Blueprint('cyanobacteria', __name__, url_prefix='/cyanobacteria')


@bp.route('/')
def main() -> str:
    return 'Foo + bar'
