from .db import db

class Bookmarks(db.Document):
    name = db.StringField(required=True, unique=True)
    url = db.StringField(required=True)
    tags = db.ListField(db.StringField(), required=False)
