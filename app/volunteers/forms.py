# coding: utf-8

from wtforms.ext.appengine.db import model_form
from wtforms.fields import SelectMultipleField

from models import Profile, Skill, Resource, Event

EventForm = model_form(Event)

PForm = model_form(Profile)

class ProfileForm(PForm):
    skills = SelectMultipleField(u'Habilidades', choices=[ (skill.name, skill.name) for skill in Skill.all().fetch(1000) ])
    resources = SelectMultipleField(u'Recursos', choices=[ (resource.name, resource.name) for resource in Resource.all().fetch(1000) ])

