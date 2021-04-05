from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/uploadFile', methods=['POST'])
def uploadFile():
    files = request.files
    print(files)    # [(nametag, <filestorage: 'filename' (mimetype) >), ...]
    fileList = []
    for file in files:
        print(file) # request.files의 name태그에 해당하는 값
        fileList+=files.getlist(file)
    print('==========fileList==========\n', fileList, '===============')
    return 'uploadFile...'

if __name__ == '__main__':
     app.run(host="127.0.0.1", port="8080", debug=True)