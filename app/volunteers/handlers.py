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
from models import Profile

class VolunteersMainHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        """Simply returns a Response object with an enigmatic salutation."""
        return self.render_response('index.html', form=self.form)

    def post(self, **kwargs):
        if self.form.validate():
            profile = Profile(
                name = self.form.name.data,
                mobile = self.form.mobile.data,
                location = self.form.location.data,
                email = self.form.email.data,
            )
            profile.put()
            return redirect('/')
        return self.get(**kwargs)

    @cached_property
    def form(self):
        return ProfileForm(self.request.form)

class MapMainHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        return self.render_response('mapa.html')
