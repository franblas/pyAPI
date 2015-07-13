# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 16:54:02 2015

@author: Paco
"""

from api import API

class Pinterest(API):

    _class_name = 'Pinterest'
    _category = 'Social'
    _help_url = 'https://developers.pinterest.com/api_docs/'
    _version = '3'
    _api_url = 'https://api.pinterest.com/v' + _version + '/'

    def _parsing_data(self,data,board=False):
        res = {'id':list(),'description':list(),'repins':list(),'likes':list(),'url':list(),'board':list()}
        for d in data['data']['pins']:
            res['id'].append(self._tools.key_test('id',d))
            res['description'].append(self._tools.key_test('description',d))
            res['repins'].append(self._tools.key_test('repin_count',d,'int'))
            res['likes'].append(self._tools.key_test('like_count',d,'int'))
            res['url'].append(self._tools.key_test('link',d))
            if not board:
                res['board'].append(self._tools.key_test('name',d['board']))
            else:
                res['board'].append(self._tools.key_test('name',data['data']['board']))
        return res

    def get_pins_by_user(self,user='ohjoy'):
        url = self._api_url+'pidgets/users/'+user+'/pins/'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def get_pins_by_board(self,user='ohjoy',board='travel'):
        url = self._api_url+'pidgets/boards/'+user+'/'+board+'/pins/'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data,board=True)
