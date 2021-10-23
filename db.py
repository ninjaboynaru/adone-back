from playhouse.cockroachdb import CockroachDatabase
from playhouse.shortcuts import model_to_dict
from peewee import Model, CharField, FloatField

db_name = 'adone-back-4309.defaultdb'
db_host = 'free-tier.gcp-us-central1.cockroachlabs.cloud'
db_user = 'thiago'
db_password = 'devpass12345'
db_port = 26257
db =  CockroachDatabase(db_name, user=db_user, password=db_password, host=db_host, port=db_port)

class User(Model):
	name = CharField()
	store = CharField()
	charity = CharField()
	donation = FloatField()
	donated = FloatField()
	max_donation = FloatField()
	class Meta:
		database = db

db.create_tables([User])

def db_get_user():
	user = User.select().get()
	return model_to_dict(user)

def db_make_donation():
	pass

def db_set_store(store):
	pass

def db_set_donation(amount):
	pass

def db_set_cap(amount):
	pass
