from flask import Flask, send_from_directory, send_file

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return send_file("static/index.html")


@app.route('/static/<path:path>', methods=['GET'])
def static_files(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
