# coding: utf-8

from google.appengine.ext import db

class Profile(db.Model):
    user = db.UserProperty()
    name = db.StringProperty()
    mobile = db.PhoneNumberProperty()
    location = db.GeoPtProperty()
    radius = db.IntegerProperty()

