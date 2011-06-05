# coding: utf-8

from google.appengine.ext import db
#from django.template import defaultfilters

class Skill(db.Model):
    """
    Uma habilidade
    """
    name = db.StringProperty()
    count = db.IntegerProperty(default = 0)
    
    def slug(self):
        return self.name.lower()

class Profile(db.Model):
    """
    Ume passoa cadastrada no sistema
    """
    user = db.UserProperty()
    name = db.StringProperty()
    email = db.EmailProperty()
    mobile = db.PhoneNumberProperty()
    location = db.GeoPtProperty()

class Profile_Skill(db.Model):
    """
    Habilidade dada por alguém quando a pessoa aprende a fazer algo
    """
    profile = db.ReferenceProperty(Profile)
    skill = db.ReferenceProperty(Skill)


class Resource(db.Model):
    """
    Uma coisa que uma pessoa tem ou pode mobilizar em caso de necessidade
    """
    name = db.StringProperty()
    count = db.IntegerProperty(default = 0)
    
    def slug(self):
        return self.name.lower()


class Profile_Resource(db.Model):
    skill = db.ReferenceProperty(Skill)
    resource = db.ReferenceProperty(Resource)
   

class SMS(db.Model):
    """
    Mensagem de SMS - manter 
    """
    pass

class Event(db.Model):
    name = db.StringProperty()
    when = db.DateTimeProperty(auto_now_add = False)
    what = db.StringProperty(multiline=True)
    location = db.GeoPtProperty()

class Action(db.Model):
    """
    """
    when = db.DateTimeProperty(auto_now_add = True)
    who = db.ReferenceProperty(Profile)
    event = db.ReferenceProperty(Event)
    what = db.StringProperty()
    location = db.GeoPtProperty()

    def is_event(self):
        return self.who is None

    @property
    def name(self):
        if self.who:
            return self.who.name
        return self.event.name

