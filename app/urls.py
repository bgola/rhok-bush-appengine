# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule

rules = [
    HandlerPrefix('volunteers.handlers.', [
            Rule('/', name='volunteer', handler='VolunteersMainHandler'),
            Rule('/mapa/', name='mapa', handler='MapMainHandler'),
            Rule('/sobre/', name='sobre', handler='AboutHandler')
            ]),

    HandlerPrefix('volunteers.profile_handlers', [
            Rule('/me', name='mapa', handler='ProfileHandler'),
            ]),
 
    HandlerPrefix('volunteers.admin_handlers.', [
            Rule('/admin/skills>', name='skill_list', 
                 handler='SkillsListHandler'),
            Rule('/admin/skill/<skill_id>', name='skill_editor', 
                 handler='SkillAdminHandler'),
            ]),
]
