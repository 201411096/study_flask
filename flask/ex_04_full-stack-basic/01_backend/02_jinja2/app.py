from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/test/<user>')
def test_variable(user):
   return render_template('variable.html', name=user)

@app.route('/test/loop')
def test_loop():
    value_list = ['list1', 'list2', 'list3']
    return render_template('loop.html', values=value_list)

@app.route('/test/if')
def hello_html():
    value = 29
    return render_template('condition.html', data=value)

@app.route("/google")
def get_google():
    response = requests.get("http://www.google.co.kr")
    return response.text 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")