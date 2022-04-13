from project.database.db import db

class Product(db.Document):
    name = db.StringField(required=True, unique=True)