from flask import Blueprint, render_template, abort, jsonify
from service import member as service_member

blueprint_member = Blueprint('member', __name__, template_folder='/templates/data', url_prefix='/member')

@blueprint_member.route('/test', methods=['GET'])
def test_get_member():
    return jsonify({"test":"get_member"}) 

# url_prefix가 존재하지 않아 원하는대로 작동하지 않는 듯 => 그냥 작동안하는듯
# @blueprint_member.errorhandler(404)
# def controller_errorHandler_404(e):
#     return render_template('error/page_404.html')

@blueprint_member.route('/', methods=['GET'])
def get_member():
    resultData = {}
    resultData['data'] = service_member.get_member({})
    return resultData