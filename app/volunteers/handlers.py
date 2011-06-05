# -*- coding: utf-8 -*-
"""
    hello_world.handlers
    ~~~~~~~~~~~~~~~~~~~~

    Hello, World!: the simplest tipfy app.

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE for more details.
"""

from tipfy.app import Response, redirect
from tipfy.handler import RequestHandler
from tipfyext.jinja2 import Jinja2Mixin
from werkzeug import cached_property
from wtforms.form import WebobInputWrapper

from forms import ProfileForm
from models import *

from pymaps import PyMap, Map
from utils import *

def recent_actions():
    return [ {'when': a.when, 
              'name':a.name, 
              'what': a.what } 
             for a in Action.all().order('-when').fetch(10) ]

class VolunteersMainHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        """Simply returns a Response object with an enigmatic salutation."""

        return self.render_response('index.html', 
                                    form = self.form, 
                                    recent_actions = recent_actions(), 
                                    top_skills = top_skills(), 
                                    top_resources = top_resources())

    def post(self, **kwargs):
        if self.form.validate():
            profile = Profile(
                name = self.form.name.data,
                mobile = self.form.mobile.data,
                location = self.form.location.data,
                email = self.form.email.data,
            )
            profile.put()
            Action(who = profile,
                   what = 'tornou-se membro do rhok bush!',
                   location = self.form.location.data).put()
            return redirect('/')
        return self.get(**kwargs)

    @cached_property
    def form(self):
        return ProfileForm(self.request.form)

class MapMainHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        points = [ (profile.location.lat, profile.location.lon, profile.name, '') for profile in Profile.all().fetch(1000) ]
        pm = PyMap(maplist=[Map("mapao", points)])
        return self.render_response('mapa.html', pymap=pm)


class AboutHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        return self.render_response('about.html', 
                                    recent_actions = recent_actions(), 
                                    top_skills = top_skills(), 
                                    top_resources = top_resources())
