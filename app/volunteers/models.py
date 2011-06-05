# coding: utf-8

from google.appengine.ext import db

class Profile(db.Model):
    user = db.UserProperty()
    name = db.StringProperty()
    email = db.EmailProperty()
    mobile = db.PhoneNumberProperty()
    location = db.GeoPtProperty()

