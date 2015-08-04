# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 13:39:01 2015

@author: Paco
"""

from api import API

class Eventbrite(API):

    _class_name = 'Eventbrite'
    _category = 'Event'
    _help_url = 'https://developer.eventbrite.com/docs/'
    _version = '3'
    _api_url = 'https://www.eventbriteapi.com/v' + _version + '/'

    def __init__(self,apikey):
        self._api_key = apikey

    def _parsing_data(self,data):
        res = {'url':list(),'category':list(),'latitude':list(),'longitude':list(),'name':list(),'past':list(),'future':list(),'description':list()}
        for d in data['events']:
            res['url'].append(self._tools.key_test('url',d))
            res['latitude'].append(self._tools.key_test('latitude',d['venue'],'float'))
            res['longitude'].append(self._tools.key_test('longitude',d['venue'],'float'))
            res['name'].append(self._tools.key_test('text',d['name']))
            res['category'].append(self._tools.key_test('name',d['category']))
            res['past'].append(self._tools.key_test('num_past_events',d['organizer'],'int'))
            res['future'].append(self._tools.key_test('num_future_events',d['organizer'],'int'))
            res['description'].append(self._tools.key_test('text',d['description']))
        return res

    def _parsing_data2(self,data):
        res = {'url':list(),'name':list(),'start':list(),'end':list(),'description':list()}
        for d in data['events']:
            res['url'].append(self._tools.key_test('url',d))
            res['name'].append(self._tools.key_test('text',d['name']))
            res['start'].append(self._tools.key_test('local',d['start']))
            res['end'].append(self._tools.key_test('local',d['end']))
            res['description'].append(self._tools.key_test('text',d['description']))
        return res

    def search(self,text=''):
        text = text.replace(' ','%20')
        url = self._api_url+'events/search/?token='+self._api_key+'&q='+text
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def search_by_coordinates(self, lat=48.87, lon=2.30, radius=2, units='km'):
        url = self._api_url+'events/search/?token='+self._api_key+'&location.latitude='+str(lat)+'&location.longitude='+str(lon)+'&location.within='+str(radius)+units
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data)

    def get_popular(self):
        url = self._api_url+'events/search/?token='+self._api_key+'&popular=true'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def get_by_city(self,text=''):
        text = text.replace(' ','%20')
        url = self._api_url+'events/search/?token='+self._api_key+'&venue.city='+text
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)
