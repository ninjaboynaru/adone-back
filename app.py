from flask import Flask, Response
from db import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/set/donation/<float:amount>")
def set_donation(amount):
    db_error = db_set_donation(amount)
    response = Response(status=200)

    if (db_error != None):
         response = Response(status=500)

    return response

@app.route("/set/store/<store>")
def set_store(store):
    db_error = db_set_store(store)
    response = Response(status=200)

    if (db_error != None):
         response = Response(status=500)

    return response

app.run()