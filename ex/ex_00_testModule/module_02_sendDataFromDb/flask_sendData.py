from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/dataFromServer')
def sendSampleData():
    with open('sampleCase.txt') as MyFile:
        fileData = MyFile.read()
        print(fileData)
        fileData = json.loads(fileData)
        return Response(
            response = json.dumps(fileData),
            status = 200,
            mimetype="application/json"
        )

if __name__ == '__main__':
    app.run(host="192.168.0.51", port="5000")