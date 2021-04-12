from flask import Flask, render_template, session, request, make_response, jsonify
from flask_login import LoginManager
from flask_cors import CORS
from controller import controller_login
from model.User import User
import os

app = Flask(__name__)
CORS(app)
# app.secret_key = 'secret_key...'
app.secret_key = os.urandom(20)

app.register_blueprint(controller_login.bp_login)

# flask login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong" # "basic"(default) or "strong" or None


"""
flask_login module 사용시 ...

1.  user_loader 혹은 request_loader callback을 제공해야함
2.  1에서 나온 User class는 직접 구현해야하며, 
    필수적으로 구현이 필요한 것들이 존재하고, 
    UserMixin을 상속받아 구현을 편하게 할 수 있음
"""
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.before_request
def before_request():
    if 'client_id' not in session:
        # HTTP_X_REAL_IP : 실제 함수
        session['client_id'] = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

# 로그인을 하지 않은 채로, @login_requried decorator가 붙어있는 요청을 할 때
@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test_test():
    return "test"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")