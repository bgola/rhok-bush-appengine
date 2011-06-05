# coding: utf-8

from google.appengine.ext import db
from django.template import defaultfilters

class Skill(db.Model):
    name = db.StringProperty()
    
    def slug(self):
        return defaultfilters.slugify(self.name)

class Profile(db.Model):
    user = db.UserProperty()
    name = db.StringProperty()
    email = db.EmailProperty()
    mobile = db.PhoneNumberProperty()
    location = db.GeoPtProperty()

class Profile_Skill(db.Model):
    profile = db.ReferenceProperty(Profile)
    skill = db.ReferenceProperty(Skill)

class Action(db.Model):
    when = db.DateTimeProperty(auto_now_add = True)
    what = db.StringProperty()
