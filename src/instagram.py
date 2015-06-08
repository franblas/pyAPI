# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 22:15:15 2015

@author: Paco
"""

from api import API

class Instagram(API):
    
    _class_name = 'Instagram'    
    _category = 'Picture'
    _help_url = 'https://instagram.com/developer/endpoints/'
    _api_url = 'https://api.instagram.com/v1/'
    
    def __init__(self,apikey):
        self._api_key = apikey
        
    def _parsing_data(self,data):
        res = {'latitude':list(),'longitude':list(),'name':list(),'count_com':list(),'com':list(),'count_like':list(),'title':list()}
        for d in data['data']:
            res['latitude'].append(self._tools.key_test('latitude',d['location'],'float'))
            res['longitude'].append(self._tools.key_test('longitude',d['location'],'float'))
            res['name'].append(self._tools.key_test('name',d['location']))
            res['count_com'].append(self._tools.key_test('count',d['comments'],'int'))
            res['com'].append(self._tools.key_test('data',d['comments'],'list'))
            res['count_like'].append(self._tools.key_test('count',d['likes'],'int'))
            res['title'].append(self._tools.key_test('text',d['caption']))
        return res  
    
    def _parsing_data2(self,data):
        res = {'count':list(),'name':list()}
        for d in data['data']:
            res['name'].append(self._tools.key_test('name',d))
            res['count'].append(self._tools.key_test('media_count',d,'int'))
        return res 
        
    def _parsing_data3(self,data):
        res = {'latitude':list(),'longitude':list(),'name':list()}
        for d in data['data']:
            res['name'].append(self._tools.key_test('name',d))
            res['latitude'].append(self._tools.key_test('latitude',d,'float'))
            res['longitude'].append(self._tools.key_test('longitude',d,'float'))
        return res  
        
    def _parsing_data4(self,data):
        res = {'username':list(),'name':list(),'id':list(),'pic':list()}
        for d in data['data']:
            res['name'].append(self._tools.key_test('full_name',d))
            res['username'].append(self._tools.key_test('username',d))
            res['id'].append(self._tools.key_test('id',d,'int'))
            res['pic'].append(self._tools.key_test('profile_picture',d))
        return res      
    
    def get_popular(self,limit=10):
        url = self._api_url+'media/popular?count='+str(limit)+'&client_id='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)   
      
    def search_by_coordinates(self,lat=48.858844,lon=2.294351,limit=10):
        url = self._api_url+'media/search?lat='+str(lat)+'&lng='+str(lon)+'&count='+str(limit)+'&client_id='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
        
    def get_tags(self,text=''):
        text = text.replace(' ','+')
        url = self._api_url+'tags/search?q='+text+'&client_id='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data) 
    
    def search_locations(self,lat=48.858844,lon=2.294351,limit=10):
        url = self._api_url+'locations/search?lat='+str(lat)+'&lng='+str(lon)+'&count='+str(limit)+'&client_id='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data3(data)  
        
    def search_users(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'users/search?q='+text+'&count='+str(limit)+'&client_id='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data4(data)