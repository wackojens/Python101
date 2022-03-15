from movie_bag.database.db import db

class User(db.Document):
    FirstName = db.StringField(required=True)
    LastName = db.StringField(required=True)
    Age = db.IntField(required=True)