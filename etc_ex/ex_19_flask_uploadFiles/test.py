from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/testFiles', methods=['GET', 'POST'])
def test():
    files = request.files.getlist('file') # html의 name attribute값과 맞춰줘야함
    for file in files:
        print(file.filename)
    return 'test...'

if __name__ == '__main__':
     app.run(host="127.0.0.1", port="8080")