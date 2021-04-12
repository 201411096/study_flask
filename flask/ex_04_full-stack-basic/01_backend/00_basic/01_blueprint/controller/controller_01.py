from flask import Blueprint

blueprint_01 = Blueprint('blueprint_01', __name__)

@blueprint_01.route('/test1')
def test():
    return 'test blueprint ...'