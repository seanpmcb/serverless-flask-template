from flask import Flask
app = Flask(__name__)


@app.route("/")
def root():
    return "It's alive. It's alive!!!"
