# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 22:39:01 2015

@author: Paco
"""

from api import API

class OSM(API):
    
    _class_name = 'Open Street Map'    
    _category = 'Map'
    _help_url = 'http://wiki.openstreetmap.org/wiki/API_v0.6'
    _api_url = 'http://api.openstreetmap.org/api/0.6/'
    _api_url2 = 'http://nominatim.openstreetmap.org/'

    def _parsing_data(self,data):
        res = {'comment':list(),'coordinates':list()}
        for d in data['features']:
            res['comment'].append(self._tools.key_test('comments',d['properties']))
            res['coordinates'].append(self._tools.key_test('coordinates',d['geometry'],'list'))
        return res  
        
    def _parsing_data2(self,data):
        res = {'latitude':list(),'longitude':list(),'name':list(),'importance':list()}
        for d in data:
            res['latitude'].append(self._tools.key_test('latitude',d,'float'))
            res['longitude'].append(self._tools.key_test('longitude',d,'float'))
            res['name'].append(self._tools.key_test('display_name',d))
            res['importance'].append(self._tools.key_test('importance',d,'int'))
        return res     
        
    def search_notes(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'notes/search.json?q='+text+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
        
    def search(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url2+'search?q='+text+'&format=json&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data) 
        
    def get_coordinates_city(self,text=''):
        res = self.search(text)
        return res['latitude'][0],res['longitude'][0]