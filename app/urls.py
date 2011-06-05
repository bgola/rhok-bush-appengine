# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy.routing import Rule, HandlerPrefix

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
            Rule('/admin/skills/', name='skill_list', 
                 handler='SkillsListHandler'),
            Rule('/admin/skills/new', name='skill_creator', 
                 handler='NewSkillHandler'),
            Rule('/admin/skills/<skill_id>', name='skill_editor', 
                 handler='SkillAdminHandler'),
            Rule('/admin/resources/', name='resource_list', 
                 handler='ResourceListHandler'),
            Rule('/admin/resources/new', name='resource_creator', 
                 handler='NewResourceHandler'),
            Rule('/admin/resources/<resource_id>', name='resource_editor', 
                 handler='ResourceAdminHandler'),
            ]),
]
