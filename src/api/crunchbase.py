# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 12:06:09 2015

@author: Paco
"""

from api import API

class Crunchbase(API):

    _class_name = 'Crunchbase'
    _category = 'Data'
    _help_url = 'https://developer.crunchbase.com/docs'
    _version = '2'
    _api_url = 'http://api.crunchbase.com/v/' + _version + '/'


    def __init__(self,apikey):
        self._api_key = apikey

    def _parsing_data(self,data):
        res = {'name':list()}
        for d in data['data']['items']:
            res['name'].append(self._tools.key_test('name',d))
        return res

    def new_organizations(self):
        url = self._api_url+'organizations?user_key='+self._api_key+'&order=created_at%20desc'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def updated_organizations(self):
        url = self._api_url+'organizations?user_key='+self._api_key+'&order=updated_at%20desc'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def search_organization(self,text=''):
        text = text.replace(' ','+')
        url = self._api_url+'organizations?user_key='+self._api_key+'&query='+text
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def new_people(self):
        url = self._api_url+'peoples?user_key='+self._api_key+'&order=created_at%20desc'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def new_products(self):
        url = self._api_url+'products?user_key='+self._api_key+'&order=created_at%20desc'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)
