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

from admin_forms import *
from models import *
from utils import *

from pymaps import PyMap, Map


class SkillsListHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        skills = Skill.all()
        return self.render_response('simple_list_admin.html', 
                                    l = skills, 
                                    recent_actions = recent_actions(), 
                                    top_skills = top_skills(), 
                                    top_resources = top_resources()) 

class SkillsAdminHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        raise NotImplementedError

class ResourceListHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        resources = Resource.all()
        return self.render_response('simple_list_admin.html', 
                                    l = resources, 
                                    recent_actions = recent_actions(), 
                                    top_skills = top_skills(), 
                                    top_resources = top_resources()) 

class ResourceAdminHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        raise NotImplementedError

class NewSkillHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        return self.render_response('simple_form.html', 
                                    form = self.form, 
                                    recent_actions = recent_actions(), 
                                    label = u'Adicionar nova capacitacao', 
                                    top_skills = top_skills(), 
                                    top_resources = top_resources()) 

    def post(self, **kwargs):
        if self.form.validate():
            Skill(name = self.form.name.data).put()
            return redirect('/admin/skills/')
        return self.get(**kwargs)

    @cached_property
    def form(self):
        return SkillForm(self.request.form)

class NewResourceHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        return self.render_response('simple_form.html', 
                                    form = self.form, 
                                    recent_actions = recent_actions(), 
                                    label = u'Adicionar novo recurso', 
                                    top_skills = top_skills(), 
                                    top_resources = top_resources()) 

    def post(self, **kwargs):
        if self.form.validate():
            Resource(name = self.form.name.data).put()
            return redirect('/admin/resources/')
        return self.get(**kwargs)

    @cached_property
    def form(self):
        return ResourceForm(self.request.form)

class AdminMenuHandler(RequestHandler, Jinja2Mixin):
    def get(self):
        return self.render_response('admin_menu.html', 
                                    recent_actions = recent_actions(), 
                                    label = u'Adicionar novo recurso', 
                                    top_skills = top_skills(), 
                                    top_resources = top_resources())
