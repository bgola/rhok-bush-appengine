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

class SkillsListHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        raise NotImplementedError

class SkillsAdminHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        raise NotImplementedError

class ResourceListHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        resources = Resource.all()
        return self.render_response('resource_admin.html', l = resources) 

class ResourceAdminHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        raise NotImplementedError
