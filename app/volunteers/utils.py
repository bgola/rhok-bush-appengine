# -*- coding: utf-8 -*-

from models import *

def recent_actions():
    return [ {'when': a.when, 
              'name':a.name, 
              'what': a.what } 
             for a in Action.all().order('-when').fetch(10) ]

def top_skills():
        return [ {'name': o.name,
              'count': o.count}
             for o in Skill.all().order('-count').order('name').fetch(5) ]

def top_resources():
 
        return [ {'name': o.name,
              'count': o.count}
             for o in Resource.all().order('-count').order('name').fetch(5) ]
 
