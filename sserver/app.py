#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "-----------my api test!--------\n"

if __name__ == '__main__':
    app.run(debug=True)
