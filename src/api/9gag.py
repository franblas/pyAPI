# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 21:36:21 2015

@author: Paco
"""

from api import API

class NineGag(API):
    
    _class_name = '9Gag'    
    _category = 'Social'
    _help_url = 'https://github.com/k3min/infinigag'
    _api_url = 'http://infinigag.eu01.aws.af.cm/'
    
    def _parsing_data(self,data):
        res = {'description':list(),'link':list()}
        for d in data['data']:
            res['description'].append(self._tools.key_test('caption',d))
            res['link'].append(self._tools.key_test('link',d))
        return res  
        
    def get_trend(self):
        url = self._api_url+'trending/0'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
        
    def get_hot(self):
        url = self._api_url+'hot/0'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)      