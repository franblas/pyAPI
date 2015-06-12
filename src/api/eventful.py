# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:40:24 2015

@author: Paco
"""

from api import API

class Eventful(API):
    
    _class_name = 'Eventful'    
    _category = 'Event'
    _help_url = 'http://api.eventful.com/docs/'
    _api_url = 'http://api.eventful.com/json/'
        
    def __init__(self,apikey):
        self._api_key = apikey
        
    def _parsing_data(self,data):
        res = {'id':list(),'description':list(),'title':list(),'country':list(),'city':list(),'address':list(),'date':list(),'latitude':list(),'longitude':list(),'url':list()}
        for d in data['events']['event']:
            res['id'].append(self._tools.key_test('id',d))
            res['description'].append(self._tools.key_test('description',d))
            res['title'].append(self._tools.key_test('title',d))
            res['country'].append(self._tools.key_test('country_name',d))
            res['city'].append(self._tools.key_test('city_name',d))
            res['address'].append(self._tools.key_test('venue_address',d))
            res['date'].append(self._tools.key_test('start_time',d))
            res['latitude'].append(self._tools.key_test('latitude',d,'float'))
            res['longitude'].append(self._tools.key_test('longitude',d,'float'))
            res['url'].append(self._tools.key_test('url',d))
        return res        

    def _parsing_data2(self,data):
        res = {'id':list(),'description':list(),'name':list(),'country':list(),'city':list(),'address':list(),'latitude':list(),'longitude':list(),'url':list()}
        for d in data['venues']['venue']:
            res['id'].append(self._tools.key_test('id',d))
            res['description'].append(self._tools.key_test('description',d))
            res['name'].append(self._tools.key_test('name',d))
            res['country'].append(self._tools.key_test('country_name',d))
            res['city'].append(self._tools.key_test('city_name',d))
            res['address'].append(self._tools.key_test('address',d))
            res['latitude'].append(self._tools.key_test('latitude',d,'float'))
            res['longitude'].append(self._tools.key_test('longitude',d,'float'))
            res['url'].append(self._tools.key_test('url',d))
        return res

    def _parsing_data3(self,data):
        res = {'id':list(),'description':list(),'performer':list(),'location':list(),'latitude':list(),'longitude':list()}
        for d in data['demands']['demand']:
            res['id'].append(self._tools.key_test('id',d))
            res['description'].append(self._tools.key_test('description',d))
            res['performer'].append(self._tools.key_test('name',d['performer']))
            res['location'].append(self._tools.key_test('location',d))
            res['latitude'].append(self._tools.key_test('latitude',d,'float'))
            res['longitude'].append(self._tools.key_test('longitude',d,'float'))
        return res

    def search_events(self,text='',location='paris',limit=10):
        text = text.replace(' ','+')
        location = location.replace(' ','+')
        url = self._api_url+'events/search?app_key='+self._api_key+'&keywords='+text+'&location='+location+'&date=Future&page_size='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
 
    def search_venues(self,text='',location='paris',limit=10):
        text = text.replace(' ','+')
        location = location.replace(' ','+')
        url = self._api_url+'venues/search?app_key='+self._api_key+'&keywords='+text+'&location='+location+'&page_size='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data)
        
    def search_demands(self,location='paris',limit=10):
        location = location.replace(' ','+')
        url = self._api_url+'demands/search?app_key='+self._api_key+'&location='+location+'&page_size='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data3(data)