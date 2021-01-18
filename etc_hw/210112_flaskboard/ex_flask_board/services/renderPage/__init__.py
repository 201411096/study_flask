from services import app
from flask import render_template, request, redirect
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

@app.route('/render/boardWrite')
@authDecorator
def render_boardWrite():
	data = {}
	data['test1']='test11'
	data['test2']='test2'
	
	requestParameter = request.args.to_dict()
	print('request.args(render_boardWrite) : ', requestParameter)

	if requestParameter is not None:
		data.update(requestParameter)
	
	return render_template('boardWrite.html', data=data)

# 안씀
@app.route('/render/boardlistView/<board_id>')
@authDecorator
def render_boardlistView(board_id):
	data = {}
	data['board_id'] = board_id
	
	return render_template('boardWrite.html', data=data)