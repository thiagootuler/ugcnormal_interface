#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

root_url = 'http://127.0.0.1:5000'
#action_url = root_url + '/token'
#action_url = root_url + '/spell'
#action_url = root_url + '/acronym'
#action_url = root_url + '/textese'
action_url = root_url + '/proper_noun'

headers = {'content-type': 'application/json'}
data = u'{"text": "no último fds fiz uma conpra pela net de um smartfone da microsoft e uma tv da lg. jah to usando o cel :) eh incrivel a tecnologia dele: tem wifi, blutoth, etc....."}'
response = requests.post(action_url, headers=headers, data=data.encode('utf-8'))
print response.text