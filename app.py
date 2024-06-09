from flask import Flask, request
from flask_cors import CORS

from dlg.smoke import test

app = Flask(__name__)
CORS(app, origins=["*"])

@app.route('/', methods=['GET'])
def smoke():
    return {"api": "toto-py-test", "running": True}

@app.route('/smoke', methods=['GET'])
def testing(): 
    return test(request)

if __name__ == '__main__':
    app.run()