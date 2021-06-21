from flask import send_file, send_from_directory


# path /
def index():
    return send_file("static/index.html")


# path /static/<path:path>
def static_files(path):
    return send_from_directory('static', path)
