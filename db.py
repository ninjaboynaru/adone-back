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
	username = CharField()
	password = CharField()
	phone_num = CharField()
	store = CharField()
	charity = CharField()
	donation = FloatField()
	donated = FloatField()
	max_donation = FloatField()
	class Meta:
		database = db

db.create_tables([User])

def db_create_account(name, un, pw, phone):
	new_acct = User.create(name = name,
						   username = un,
						   password = pw,
						   phone_num = phone,
						   store = '',
						   charity = '',
						   donation = 0,
						   donated = 0,
						   max_donation = 0)
	print(new_acct.name)
	print(new_acct.username)
	print(new_acct.password)
	print(new_acct.phone_num)

def get_user():
	return User.select().get()

def db_get_user():
	user = get_user()
	return model_to_dict(user)

def db_get_donated():
	user = get_user()
	return None, user.donated

def db_make_donation():
	user = get_user()
	user.donated += user.donation
	user.save()

def db_set_store(store):
	user = get_user()
	user.store = store
	user.save()

def db_set_donation(amount):
	user = get_user()
	user.donation = amount
	user.save()

def db_set_cap(amount):
    user = get_user()
    user.max_donation = amount
    user.save()

def db_set_charity(charity):
    user = get_user()
    user.charity = charity
    user.save()