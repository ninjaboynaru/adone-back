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
    db_error, hit_max, donation_made = db_make_donation()

    if (db_error != None):
        response = Response(status=500)
    else:
        if (hit_max == 'Yes'):
            response = Response('You made a donation of $' + str(donation_made) +
                                '\n You have reached your donation limit', status=200)
        else:
            response = Response('You made a donation of $' + str(donation_made), status=200)

    return response

@app.route("/set/store/<store>")
def set_store(store):
    db_error, store_db = db_set_store(store)

    if (db_error != None):
        response = Response(status=500)
    else:
        response = Response('Your store has been set to ' + str(store_db), status=200)

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
    db_error, charity_db = db_set_charity(charity)

    if (db_error != None):
        response = Response(status=500)
    else:
        response = Response('Your charity has been set to ' + str(charity_db), status=200)

    return response

@app.route("/quick_donate/")
def quick_donate():
    db_error = db_quick_donate()

    if (db_error != None):
        response = Response(status=500)
    else:
        response = Response(status=200)
    return response

@app.route("/get/donated")
def get_donated():
    db_error, donated = db_get_donated()

    if (db_error != None):
        response = Response(status=500)
    else:
        response = Response('You have donated $' + str(donated), status=200)

    return response

@app.route("/get/store")
def get_store():
    db_error, store = db_get_store()

    if (db_error != None):
        response = Response(status=500)
    else:
        response = Response('You have chosen ' + str(store) + ' as your store', status=200)

    return response

@app.route("/get/charity")
def get_charity():
    db_error, charity = db_get_charity()

    if (db_error != None):
        response = Response(status=500)
    else:
        response = Response('You have chosen ' + str(charity) + ' as your charity', status=200)

    return response

@app.route("/get/donation")
def get_donation():
    db_error, donation = db_get_donation()

    if (db_error != None):
        response = Response(status=500)
    else:
        response = Response('You have chosen to donate $' + str(donation) + ' each visit', status=200)

    return response

@app.route("/get/cap")
def get_cap():
    db_error, cap = db_get_cap()

    if (db_error != None):
        response = Response(status=500)
    else:
        response = Response('Your current donation limit is $' + str(cap), status=200)

    return response

app.run()
