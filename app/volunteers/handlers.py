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
            skills = self.form.skills.data
            for skill in skills:
                s = Skill.all().filter('name',skill).get()
                s.count += 1
                s.put()
                sp = Profile_Skill(profile=profile, skill=s)
                sp.put()
            resources = self.form.resources.data
            for resource in resources:
                r = Resource.all().filter('name',resource).get()
                r.count += 1
                r.put()
                rp = Profile_Resource(profile=profile, resource=r)
                rp.put()
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
