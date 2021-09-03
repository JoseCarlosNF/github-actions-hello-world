import os
from flask import Flask

app = Flask(__name__)
FLASK_HOST = os.getenv("FLASK_HOST")
FLASK_PORT = os.getenv("FLASK_PORT")
FLASK_DEBUG = os.getenv("FLASK_DEBUG")


@app.route('/')
def main():
    return f'<h1 style="font-family:arial;">Hostname: {os.uname()[1]}</h1>'


if __name__ == "__main__":
    app.run(host=FLASK_HOST, port=FLASK_PORT)
