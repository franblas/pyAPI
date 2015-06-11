# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 19:52:02 2015

@author: Paco
"""

from api import API

class Delicious(API):
    
    _class_name = 'Delicious'    
    _category = 'Social'
    _help_url = 'https://delicious.com/rss'
    _api_url = 'http://feeds.delicious.com/v2/json/'

    def _parsing_data(self,data):
        res = {'d':list(),'u':list(),'t':list()}
        for d in data:
            res['d'].append(self._tools.key_test('d',d))
            res['u'].append(self._tools.key_test('u',d))
            res['t'].append(map(lambda x : self._tools.encode_str(x),d['t']))
        return res    
        
    def get_recent(self,limit=10):
        url = self._api_url+'recent?count='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)
        
    def search(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'tag/['+text+']?count='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)