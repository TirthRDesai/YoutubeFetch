
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app=app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/url', methods=['POST'])
def url():
    userUrl = request.form
    print(len(userUrl))
    return render_template("setUrl.html", userUrl=userUrl)
    # return jsonify({'response': userUrl})
