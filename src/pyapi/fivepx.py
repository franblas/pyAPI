# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 11:12:25 2015

@author: Paco
"""

from api import API

class CinqCentPx(API):

    _class_name = '500px'
    _category = 'Picture'
    _help_url = 'https://github.com/500px/api-documentation'
    _version = '1'
    _api_url = 'https://api.500px.com/v' + _version + '/'

    def __init__(self,apikey):
        self._api_key = apikey

    def _parsing_data(self,data):
        res = {'title':list(),'description':list(),'latitude':list(),'longitude':list(),'link':list(),'usercountry':list()}
        for d in data['photos']:
            res['title'].append(self._tools.key_test('name',d))
            res['description'].append(self._tools.key_test('description',d))
            res['latitude'].append(self._tools.key_test('latitude',d,'float'))
            res['longitude'].append(self._tools.key_test('longitude',d,'float'))
            res['link'].append(self._tools.key_test('image_url',d))
            res['usercountry'].append(self._tools.key_test('country',d['user']))
        return res

    def get_popular(self,limit=10):
        url = self._api_url+'photos?feature=popular&rpp='+str(limit)+'&consumer_key='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def get_best_rated(self,limit=10):
        url = self._api_url+'photos?feature=highest_rated&rpp='+str(limit)+'&consumer_key='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def get_today(self,limit=10):
        url = self._api_url+'photos?feature=fresh_today&rpp='+str(limit)+'&consumer_key='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def get_stories(self,limit=10):
        url = self._api_url+'blogs?rpp='+str(limit)+'&consumer_key='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def search(self,text='',limit=10):
        url = self._api_url+'photos/search?term='+text+'&rpp='+str(limit)+'&consumer_key='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)
