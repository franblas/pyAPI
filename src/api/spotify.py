# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:49:52 2015

@author: Paco
"""

from api import API

class Spotify(API):
    
    _class_name = 'Spotify'    
    _category = 'Music'
    _help_url = 'https://developer.spotify.com/web-api/'
    _api_url = 'https://api.spotify.com/v1/'
        
    def _parsing_data(self,data):
        res = {'id':list(),'name':list(),'genres':list(),'popularity':list(),'url':list()}
        for d in data['artists']['items']:
            res['id'].append(self._tools.key_test('id',d))
            res['name'].append(self._tools.key_test('name',d))
            res['genres'].append(self._tools.key_test('genres',d,'list'))
            res['popularity'].append(self._tools.key_test('popularity',d,'int'))
            res['url'].append(self._tools.key_test('spotify',d['external_urls']))
        return res        

    def _parsing_data2(self,data):
        res = {'id':list(),'name':list(),'duration':list(),'popularity':list(),'url':list(),'artist':list(),'album':list()}
        for d in data['tracks']['items']:
            res['id'].append(self._tools.key_test('id',d))
            res['name'].append(self._tools.key_test('name',d))
            res['duration'].append(self._tools.key_test('duration_ms',d,'int'))
            res['popularity'].append(self._tools.key_test('popularity',d,'int'))
            res['url'].append(self._tools.key_test('spotify',d['external_urls']))
            res['artist'].append(self._tools.key_test('name',d['artists'][0]))
            res['album'].append(self._tools.key_test('name',d['album']))        
        return res

    def _parsing_data3(self,data):
        res = {'id':list(),'name':list(),'type':list(),'url':list()}
        for d in data['albums']['items']:
            res['id'].append(self._tools.key_test('id',d))
            res['name'].append(self._tools.key_test('name',d))
            res['type'].append(self._tools.key_test('album_type',d))
            res['url'].append(self._tools.key_test('spotify',d['external_urls']))
        return res

    def search_artists(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'search?q='+text+'&type=artist&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 

    def search_tracks(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'search?q='+text+'&type=track&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data)      
        
    def search_albums(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'search?q='+text+'&type=album&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data3(data)