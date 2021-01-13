from services import app
from flask import render_template

@app.route('/test/renderPage')
def test_renderPage():
	return render_template('test_sample.html')

@app.route('/render/login')
def render_login():
	return render_template('login.html')

@app.route('/render/signup')
def render_signup():
	return render_template('signup.html')
