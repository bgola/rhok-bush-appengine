# coding: utf-8

from wtforms.ext.appengine.db import model_form

from models import *

SkillForm = model_form(Skill, exclude = ('count'))

ResourceForm = model_form(Resource, exclude = ('count'))

