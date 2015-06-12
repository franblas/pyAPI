# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:33:05 2015

@author: Paco
"""

from api import API

class Freebase(API):
    
    _class_name = 'Freebase'    
    _category = 'Data'
    _help_url = 'https://developers.google.com/freebase/v1/search'
    _api_url = 'https://www.googleapis.com/freebase/v1/'
        
    def __init__(self,apikey):
        self._api_key = apikey
        
    def _parsing_data(self,data):
        res = {'id':list(),'name':list(),'notable':list(),'score':list()}
        for d in data['result']:
            res['id'].append(self._tools.key_test('mid',d))
            res['name'].append(self._tools.key_test('name',d))
            res['notable'].append(self._tools.key_test('notable',d,'list'))
            res['score'].append(self._tools.key_test('score',d,'float'))
        return res        

    def search(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'search?query='+text+'&key='+self._api_key+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 

