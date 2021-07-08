from flask import render_template, send_from_directory


# path /
def index():
    return render_template("index.html")


# path /static/<path:path>
def static_files(path):
    return send_from_directory('static', path)
