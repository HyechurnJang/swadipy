# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 12.
@author: HyechurnJang
'''

class ExceptSwadipyAbstract(Exception):
    def __init__(self, session, msg):
        Exception.__init__(self, msg)
        if session.debug: print msg

class ExceptSwadipySession(ExceptSwadipyAbstract):
    def __init__(self, session):
        ExceptSwadipyAbstract.__init__(self, session, '[Error]Swadipy:Session:%s' % session.url)

class ExceptSwadipyResponse(ExceptSwadipyAbstract):
    def __init__(self, session, code, text):
        ExceptSwadipyAbstract.__init__(self, session, '[Error]Swadipy:Response:%s:%s' % (code, text))