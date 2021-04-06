from flask import Flask
from controller import controller_01

app = Flask(__name__)
app.register_blueprint(controller_01.blueprint_01 , url_prefix='/test')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')