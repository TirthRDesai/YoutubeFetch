
from flask import Flask, render_template, request, jsonify
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app, permanent=True)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/url', methods=['POST'])
def url():
    userUrl = request.form['url']
    return render_template("setUrl.html", userUrl=userUrl)
    # return jsonify({'response': 'success'})


if __name__ == '__main__':
    app.run(debug=True, host="10.84.33.200",
            ssl_context=('C:\\Program Files\\OpenSSL-Win64\\bin\\cert.pem', 'C:\\Program Files\\OpenSSL-Win64\\bin\\privkey.pem'))
