from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_user, logout_user, login_required, current_user
from model.User import User
import datetime

bp_login = Blueprint('bp_login', __name__)

"""
Blueprint.name (ex bp_login)

url_for( <Blueprint.name>.<function_name> )
"""
@bp_login.route('/login')
def login():
    user_email = request.args.get('user_email')
    blog_id = request.args.get('blog_id')
    user = User.create(user_email, blog_id)

    login_user(user, remember=True, duration=datetime.timedelta(days=365))
    
    return redirect(url_for('bp_login.render_sample'))
    # return redirect('/render/sample')

@bp_login.route('/logout')
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect('/render/sample')

@bp_login.route('/test/login-required')
@login_required
def test_login_required():
    return 'test login-required'

@bp_login.route('/render/sample')
def render_sample():
    webpage_name = 'index.html'
    if current_user.is_authenticated:
        return render_template(webpage_name, user_email=current_user.user_email)
    else:
        return render_template(webpage_name)