from flask import Flask, jsonify
from risco.risco import Risco
import os

app = Flask(__name__)
riscoapi = Risco()
riscoapi.authenticate(os.environ["username"],
                      os.environ["password"],
                      os.environ["pin"],
                      os.environ["site_id"])

@app.route("/")
def root():
    return "Hello World!"

@app.route("/get_dects")
def get_dects():
    global riscoapi
    return jsonify(riscoapi.get_dects())

@app.route("/overview")
def overview():
    global riscoapi
    return jsonify(riscoapi.overview())

@app.route("/get_cp_state")
def get_cp_state():
    global riscoapi
    return jsonify(riscoapi.get_cp_state())

app.run()
