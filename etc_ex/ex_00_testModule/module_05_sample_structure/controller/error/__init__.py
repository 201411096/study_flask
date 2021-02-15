from flask import Blueprint, render_template, abort

blueprint_errorHandler = Blueprint('blueprint_errorHandler', __name__, template_folder='/templates')

@blueprint_errorHandler.route('/test/route/errorHandler')
def test_errorHandler():
    return render_template('error/test_errorHandlerRouting.html')

@blueprint_errorHandler.route('/test/route/abort')
def test_aborting():
    # abort(404) # 주석해제해서 확인
    # abort(5555) # 주석해제해서 확인   # 임의의 코드는 abort 시킬 수 없음
    abort(500)
    return render_template('sample.html')

@blueprint_errorHandler.errorhandler(500)
def blueprint_handler_500(e):
    print('test in blueprint ...')
    return render_template('error/page_500.html')