from flask import Flask, make_response, jsonify
import requests
import datetime

app = Flask(__name__)

if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    """
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL
    """
    file_handler = RotatingFileHandler('server.log', maxBytes=2000, backupCount=10, encoding='utf-8')
    file_handler.setLevel(logging.WARNING)  # set logging level
    app.logger.addHandler(file_handler)     # add logger to app

@app.before_first_request
def before_first_request():
    print("first request ...")

@app.before_request
def before_request():
    print("before request ...")

@app.after_request
def after_request(response):
    print("after request ...")
    return response

@app.route("/hello")
def hello():
    print('hello ...')
    return "hello"

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('404 error : ' + str(datetime.datetime.now()) )
    return "404 not found ...", 404

@app.route("/test", methods=['GET'])
def test():
    return make_response(jsonify(key1='value1', key2='value2', key3=True), 200)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")