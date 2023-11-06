
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import database
import json

app = Flask(__name__)
CORS(app=app, origins=["*"])


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/url', methods=['GET', 'POST'])
def url():
    if request.method == "GET":
        userUrl = request.args
    else:
        userUrl = request.json

    userUrl = userUrl["userUrl"]
    print(userUrl)
    database.main(userUrl)

    return jsonify({'response': 'success'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
