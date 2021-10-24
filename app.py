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


@app.route("/make_donation/")
def make_donation():
    db_error, hit_max = db_make_donation()

    if (db_error != None):
        response = Response(status=500)
    else:
        if (hit_max == 'Yes'):
            response = Response('You have reached your donation limit', status=200)
        else:
            response = Response(status=200)

    return response

@app.route("/set/store/<store>")
def set_store(store):
    db_error = db_set_store(store)
    response = Response(status=200)

    if (db_error != None):
        response = Response(status=500)

    return response


@app.route("/set/cap/<amount>")
def set_cap(amount):
    db_error = db_set_cap(amount)
    response = Response(status=200)

    if (db_error != None):
        response = Response(status=500)

    return response


@app.route("/set/charity/<charity>")
def set_charity(charity):
    db_error = db_set_charity(charity)
    response = Response(status=200)

    if (db_error != None):
        response = Response(status=500)

    return response


@app.route("/get/donated")
def get_donated():
    db_error, donated = db_get_donated()

    if (db_error != None):
        response = Response(status=500)
    else:
        response = Response('$' + str(donated), status=200)

    return response

@app.route("/quick_donate/")
def quick_donate():
    db_error = db_quick_donate()
    response = Response(status=200)

    if (db_error != None):
        response = Response(status=500)

    return response

app.run()
