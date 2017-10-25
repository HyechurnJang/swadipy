# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 12.
@author: HyechurnJang
'''

import json
from pygics import RestAPI
from .static import *

class Session(RestAPI):
    
    def __init__(self, ip, user, pwd, **kargs):
        RestAPI.__init__(self, ip, user, pwd, proto=RestAPI.PROTO_HTTPS, **kargs)
    
    def __login__(self, req):
        try: resp = req.post(self.url + '/smc/j_spring_security_check',
                             headers={'Content-Type': 'application/x-www-form-urlencoded',
                                      'Referer': self.url + '/lc-landing-page/',
                                      'Origin': self.url},
                             data='j_username=%s&j_password=%s&submit=' % (self.user, self.pwd),
                             allow_redirects=True,
                             verify=False)
        except Exception as e:
            print str(e)
            raise ExceptSwadipySession(self)
        if resp.status_code == 200:
            if self.debug: print('Stealthwatch Session Connect to %s' % self.url)
            return None
        raise ExceptSwadipySession(self)
    
    def __header__(self):
        return {'Content-Type' : 'application/json'}
    
    def __refresh__(self, req):
        return self.__login__(req)
    
    def get(self, url):
        for _ in range(0, self.retry):
            resp = RestAPI.get(self, '/smc/rest' + url)
            if resp.status_code == 200: return resp.json()
            elif resp.status_code == 401: self.refresh()
            else: raise ExceptSwadipyResponse(self, resp.status_code, url)
        raise ExceptSwadipySession(self)
    
    def post(self, url, data):
        for _ in range(0, self.retry):
            resp = RestAPI.post(self, '/smc/rest' + url, data)
            if resp.status_code == 200: return True
            elif resp.status_code == 401: self.refresh()
            else: raise ExceptSwadipyResponse(self, resp.status_code, url)
        raise ExceptSwadipySession(self)
