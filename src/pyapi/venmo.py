# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 21:30:42 2015

@author: Paco
"""

from api import API

class Venmo(API):

    _class_name = 'Venmo'
    _category = 'Payement'
    _help_url = 'http://www.snip2code.com/Snippet/54422/Hit-venmo-public-feed-API-to-see-what-th'
    _version = '5'
    _api_url = 'https://venmo.com/api/v' + _version + '/'

    def _parsing_data(self,data):
        res = {'url':list(),'message':list()}
        for d in data['data']:
            res['message'].append(self._tools.key_test('message',d))
            res['url'].append(self._tools.key_test('permalink',d))
        return res

    def search(self):
        url = self._api_url+'public'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)
