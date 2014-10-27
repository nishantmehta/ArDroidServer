from google.appengine.ext import db


class user(db.Model):
        userID = db.StringProperty(required=True, indexed=True)
        registrationID = db.StringProperty(required=True, indexed=True)