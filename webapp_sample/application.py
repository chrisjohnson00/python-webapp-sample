from services.backend import Backend
from utilities.env_config import get_config
from flask import (
    Blueprint, render_template
)

bp = Blueprint('app', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('app/index.html')


@bp.route('/users')
def users():
    backend_service = Backend(api_hostname=get_config('API_HOSTNAME'))
    users = backend_service.get_users()
    return render_template('app/users.html', users=users)
