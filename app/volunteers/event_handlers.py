# -*- coding: utf-8 -*-
from tipfy.app import Response, redirect
from tipfy.handler import RequestHandler
from tipfyext.jinja2 import Jinja2Mixin
from werkzeug import cached_property
from wtforms.form import WebobInputWrapper

from forms import EventForm
from models import *

from utils import *

class EventMainHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        return self.render_response('event.html', 
                                    form = self.form, 
                                    recent_actions = recent_actions(), 
                                    top_skills = top_skills(), 
                                    top_resources = top_resources())

    def post(self, **kwargs):
        if self.form.validate():
            event = Event(
                name = self.form.name.data,
                what = self.form.what.data,
                location = self.form.location.data,
                when = self.form.when.data,
            )
            event.put()
            profiles = Profile.all().fetch(1000)
            for profile in profiles:
                if in_radius(event.location, profile.location):
                    number = "+" + "".join([ c for c in profile.mobile if c.isdigit() ])
                    x = smssend(number, "Criaram um evento pra voce!")
            Action(event = event,
                   what = 'foi criado!',
                   location = self.form.location.data).put()
            return redirect('/event/')
        return self.get(**kwargs)

    @cached_property
    def form(self):
        return EventForm(self.request.form)

