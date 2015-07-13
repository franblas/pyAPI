# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 12:18:28 2015

@author: Paco
"""

from api import API

class Docker(API):

    _class_name = 'Docker'
    _category = 'Code'
    _help_url = 'https://docs.docker.com/reference/api/registry_api/'
    _version = '1'
    _api_url = 'https://index.docker.io/v' + _vesrion + '/'

    def _parsing_data(self,data):
        res = {'name':list(),'star_count':list(),'description':list()}
        for d in data['results']:
            res['name'].append(self._tools.key_test('name',d))
            res['star_count'].append(self._tools.key_test('star_count',d,'int'))
            res['description'].append(self._tools.key_test('description',d))
        return res

    def search(self,text='',limit=10):
        url = self._api_url+'search?q='+text+'&n='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)
