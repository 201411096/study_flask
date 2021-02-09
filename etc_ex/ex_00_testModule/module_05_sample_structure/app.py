from flask import Flask, abort
from flask_cors import CORS
# from database import *      # 주석처리해도 정상적으로 돌아감  => 미리 import할 필요 없이 service단에서 import하면 되는 듯
from controller import *

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '111'

app.register_blueprint(blutprint_errorHandler)
app.register_blueprint(blueprint_member)

CORS(app)

@app.route('/')
def test_routing():
    return 'indexpage'

@app.errorhandler(404)
def _handler_404(e):
    return render_template('error/page_404.html')

if __name__ == '__main__':
    app.run(debug=True)