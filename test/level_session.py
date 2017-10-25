# -*- coding: utf-8 -*-
'''
Created on 2017. 10. 12.
@author: HyechurnJang
'''

import json
from swadipy import Session

s = Session('198.18.133.136', 'admin', 'C1sco12345')

hgroups = s.get('/system/domains/143/hostGroups')

# print json.dumps(hgroups, indent=2)

print hgroups['root'][0]['name']
print hgroups['root'][0]['children'][0]['name']
print hgroups['root'][0]['children'][1]['name']
print hgroups['root'][0]['children'][2]['name']
print hgroups['root'][0]['children'][3]['name']
print hgroups['root'][0]['children'][4]['name']
print hgroups['root'][0]['children'][5]['name']
