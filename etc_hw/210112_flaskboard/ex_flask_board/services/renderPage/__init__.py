from services import app
from flask import render_template
from flask import session as flaskSession
from util import authDecorator


@app.route('/test/renderPage')
def test_renderPage():
	return render_template('test_sample.html')

@app.route('/test/test_loginSuccess')
@authDecorator
def test_loginSuccess():
	print('check userData : ', flaskSession.get('userData'))
	return render_template('test_loginSuccess.html')

@app.route('/render/login')
def render_login():
	return render_template('login.html')

@app.route('/render/signup')
def render_signup():
	return render_template('signup.html')

@app.route('/render/index')
def render_index():
	return render_template('index.html')
