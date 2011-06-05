# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule

rules = [
    Rule('/', name='volunteer', handler='volunteers.handlers.VolunteersMainHandler'),
]
