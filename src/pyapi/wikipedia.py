# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 10:54:39 2015

@author: Paco
"""

from api import API

class Wikipedia(API):

    _class_name = 'Wikipedia'
    _category = 'Data'
    _help_url = 'http://en.wikipedia.org/w/api.php?action=help&modules=query'
    _api_url = 'http://en.wikipedia.org/w/api.php?action=query&format=json&'

    def _parsing_data(self,data):
        keywiki = str(data['query']['pages'].keys()[0])
        res = {'title':list()}
        for d in data['query']['pages'][keywiki]['linkshere']:
            res['title'].append(self._tools.key_test('title',d))
        return res

    def _parsing_data2(self,data):
        keywiki = str(data['query']['pages'].keys()[0])
        res = {'title':list()}
        for d in data['query']['pages'][keywiki]['links']:
            res['title'].append(self._tools.key_test('title',d))
        return res

    def _parsing_data3(self,data):
        res = {'title':list()}
        for d in data['query']['prefixsearch']:
            res['title'].append(self._tools.key_test('title',d))
        return res

    def _parsing_data4(self,data):
        res = {'title':list(),'timestamp':list(),'count':list()}
        for d in data['query']['search']:
            res['title'].append(self._tools.key_test('title',d))
            res['timestamp'].append(self._tools.key_test('timestamp',d))
            res['count'].append(self._tools.key_test('wordcount',d,'int'))
        return res

    def _parsing_data5(self,data):
        res = {'title':list(),'latitude':list(),'longitude':list(),'distance':list()}
        for d in data['query']['geosearch']:
            res['title'].append(self._tools.key_test('title',d))
            res['latitude'].append(self._tools.key_test('lat',d,'float'))
            res['longitude'].append(self._tools.key_test('lon',d,'float'))
            res['distance'].append(self._tools.key_test('dist',d,'float'))
        return res

    def _parsing_data6(self,data):
        res = {'title':list(),'timestamp':list()}
        for d in data['query']['protectedtitles']:
            res['title'].append(self._tools.key_test('title',d))
            res['timestamp'].append(self._tools.key_test('timestamp',d))
        return res

    def _parsing_data7(self,data):
        res = {'title':list(),'timestamp':list()}
        for d in data['query']['recentchanges']:
            res['title'].append(self._tools.key_test('title',d))
            res['timestamp'].append(self._tools.key_test('timestamp',d))
        return res

    def get_linksphere(self,text='',limit=10):
        text = text.replace(' ','%20')
        url = self._api_url+'prop=linkshere&titles='+text+'&lhlimit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def get_links(self,text='',limit=10):
        text = text.replace(' ','%20')
        url = self._api_url+'prop=links&titles='+text+'&pllimit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data)

    def search_prefix(self,text='',limit=10):
        text = text.replace(' ','%20')
        url = self._api_url+'list=prefixsearch&pssearch='+text+'&pslimit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data3(data)

    def search_text(self,text='',limit=10):
        text = text.replace(' ','%20')
        url = self._api_url+'list=search&srsearch='+text+'&srlimit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data4(data)

    def search_geo(self,lat=48.858844,lon=2.294351,radius=2,limit=10):
        url = self._api_url+'list=geosearch&gsradius='+str(radius*1000)+'&gscoord='+str(lat)+'|'+str(lon)+'&gslimit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data5(data)

    def get_latest_protected(self,limit=10):
        url = self._api_url+'list=protectedtitles&ptlimit'+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data6(data)

    def get_latest_changes(self,limit=10):
        url = self._api_url+'list=recentchanges&rclimit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data7(data)
