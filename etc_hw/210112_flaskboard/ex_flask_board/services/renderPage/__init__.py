from services import app
from flask import render_template

@app.route('/test/renderPage')
def test_renderPage():
  return render_template('test_sample.html')