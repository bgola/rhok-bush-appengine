# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule

rules = [
    Rule('/', name='volunteer', handler='volunteers.handlers.VolunteersMainHandler'),
    Rule('/mapa/', name='mapa', handler='volunteers.handlers.MapMainHandler'),
    Rule('/sobre/', name='sobre', handler='volunteers.handlers.AboutHandler'),
]
