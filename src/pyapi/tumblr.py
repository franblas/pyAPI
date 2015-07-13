# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 21:22:27 2015

@author: Paco
"""

from api import API

class Tumblr(API):

    _class_name = 'Tumblr'
    _category = 'Social'
    _help_url = 'https://www.tumblr.com/docs/en/api/v2'
    _version = '2'
    _api_url = 'http://api.tumblr.com/v' + _version + '/'

    def __init__(self):
        self._api_key = 'fuiKNFp9vQFvjLNvx4sUwti4Yb5yGutBN4Xh10LXZhhRKjWlV4'

    def _parsing_data(self,data):
        res = {'slug':list(),'tags':list(),'note':list(),'url':list(),'date':list()}
        for d in data['response']:
            res['slug'].append(self._tools.key_test('slug',d))
            res['url'].append(self._tools.key_test('post_url',d))
            res['tags'].append(self._tools.key_test('tags',d,'list'))
            res['note'].append(self._tools.key_test('note_count',d,'int'))
            res['date'].append(self._tools.key_test('date',d))
        return res

    def search(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'tagged?tag='+text+''+'&limit='+str(limit)+'&api_key='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)
