# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 21:39:18 2015

@author: Paco
"""

from api import API

class RubyGems(API):

    _class_name = 'Ruby Gems'
    _category = 'Code'
    _help_url = 'http://guides.rubygems.org/rubygems-org-api/'
    _version = '1'
    _api_url = 'https://rubygems.org/api/v' + _version + '/'

    def _parsing_data(self,data):
        res = {'name':list(),'downloads':list(),'info':list(),'url':list()}
        for d in data:
            res['name'].append(self._tools.key_test('name',d))
            res['downloads'].append(self._tools.key_test('downloads',d,'int'))
            res['info'].append(self._tools.key_test('info',d))
            res['url'].append(self._tools.key_test('homepage_uri',d))
        return res

    def search(self,text=''):
        text = text.replace(' ','+')
        url = self._api_url+'search.json?query='+text
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def latest_added(self):
        url = self._api_url+'activity/latest.json'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def latest_updated(self):
        url = self._api_url+'activity/just_updated.json'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def total_download_gems(self):
        url = self._api_url+'downloads.json'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return data
