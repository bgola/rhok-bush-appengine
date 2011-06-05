# coding: utf-8

from wtforms.ext.appengine.db import model_form

from models import Profile

ProfileForm = model_form(Profile)
