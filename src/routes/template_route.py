from flask import Blueprint, jsonify
from controllers.template_controller import *

prefix = '/template'
template_bp = Blueprint('template_blueprint', __name__, url_prefix=prefix)

@template_bp.route('/', methods=['GET'])
def hello_from_server():
    return hello_word()


