from flask import Blueprint, render_template, abort

blutprint_errorHandler = Blueprint('blutprint_errorHandler', __name__, template_folder='/templates')

@blutprint_errorHandler.route('/test/route/errorHandler')
def test_errorHandler():
    return render_template('error/test_errorHandlerRouting.html')

@blutprint_errorHandler.route('/test/route/abort')
def test_aborting():
    # abort(404) # 주석해제해서 확인
    return render_template('sample.html')
