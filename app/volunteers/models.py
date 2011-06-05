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

class Action(db.Model):
    """
    """
    when = db.DateTimeProperty(auto_now_add = True)
    who = db.ReferenceProperty(Profile)
    what = db.StringProperty()
    location = db.GeoPtProperty()

    @property
    def name(self):
        return self.who.name

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

