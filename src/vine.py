# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 21:33:40 2015

@author: Paco
"""

from api import API

class Vine(API):
    
    _class_name = 'Vine'    
    _category = 'Video'
    _help_url = 'https://github.com/starlock/vino/wiki/API-Reference'
    _api_url = 'https://api.vineapp.com/'
 
    def _parsing_data(self,data):
        res = {'url':list(),'description':list()}
        for d in data['data']:
            res['description'].append(self._tools.key_test('description',d['records']))
            res['url'].append(self._tools.key_test('permalinkUrl',d['records']))
        return res  
        
    def get_popular(self):
        url = self._api_url+'timelines/popular'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
        
    def search(self,text=''):
        text = text.split(' ')[0]
        url = self._api_url+'timelines/tags/'+text
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)     

        