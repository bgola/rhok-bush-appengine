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

def recent_actions():
    return [ {'when': a.when, 
              'name':a.name, 
              'what': a.what,
              'is_event': a.is_event()} 
             for a in Action.all().order('-when').fetch(10) ]

def in_radius(pt1, pt2, d=0.5):
    return pt2.lat < pt1.lat+d and pt2.lat > pt1.lat-d and pt2.lon < pt1.lon+d and pt2.lon > pt1.lon-d

import urllib2, urllib

def smssend(phone, message):
    response = urllib2.urlopen("http://186.202.49.60:8080/api/sms?cmd=send&token=1307270193710&to=%s&message=%s" % (phone, urllib.quote(message))).read()
    return '"response":"OK"' in response

