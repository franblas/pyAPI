# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 10:05:16 2015

@author: Paco
"""

from api import API

class IMDB(API):
    
    _class_name = 'IMDB'    
    _category = 'Movie'
    _help_url = 'http://www.omdbapi.com/'
    _api_url = 'http://www.imdb.com/xml/'
    _api_url2 = 'http://www.omdbapi.com/'
    
    def _parsing_data(self,data):
        res = {'popular':list(),'exact':list(),'substring':list()}
        for d in data:
            res['popular'].append(self._tools.key_test('name',d['name_popular']))
            res['exact'].append(self._tools.key_test('name',d['name_exact']))
            res['substring'].append(self._tools.key_test('name',d['name_substring']))
        return res  

    def _parsing_data2(self,data):
        res = {'popular':list(),'exact':list(),'substring':list()}
        for d in data:
            res['popular'].append(self._tools.key_test('title',d['title_popular']))
            res['exact'].append(self._tools.key_test('title',d['title_exact']))
            res['substring'].append(self._tools.key_test('title',d['title_substring']))
        return res 
        
    def _parsing_data3(self,data):
        res = {'title':list(),'year':list(),'type':list()}
        for d in data['search']:
            res['title'].append(self._tools.key_test('Title',d))
            res['year'].append(self._tools.key_test('Year',d))
            res['type'].append(self._tools.key_test('Type',d))
        return res 
        
    def search_name(self,text=''):
        text = text.replace(' ','+')
        url = self._api_url+'find?json=1&q='+text
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
        
    def search_title(self,text=''):
        text = text.replace(' ','+')
        url = self._api_url+'find?json=1&q='+text
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data)     
        
    def search_omdb(self,text=''):
        text = text.replace(' ','+')
        url = self._api_url2+'?s='+text
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data3(data)         
        
        