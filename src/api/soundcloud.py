# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 10:17:32 2015

@author: Paco
"""

from api import API

class Soundcloud(API):
    
    _class_name = 'Soundcloud'    
    _category = 'Music'
    _help_url = 'https://developers.soundcloud.com/docs/api/guide'
    _api_url = 'http://api.soundcloud.com/'
    
    def __init__(self,apikey):
        self._api_key = apikey    
    
    def _parsing_data(self,data):
        res = {'title':list(),'downloads':list(),'favorites':list(),'comments':list(),'genre':list(),'duration':list(),'tags':list(),'description':list(),'url':list()}
        for d in data:
            res['title'].append(self._tools.key_test('title',d))
            res['downloads'].append(self._tools.key_test('download_count',d,'int'))
            res['favorites'].append(self._tools.key_test('favoritings_count',d,'int'))
            res['comments'].append(self._tools.key_test('comment_count',d,'int'))
            res['genre'].append(self._tools.key_test('genre',d))
            res['duration'].append(self._tools.key_test('duration',d))
            res['tags'].append(self._tools.key_test('tag_list',d,'list'))
            res['description'].append(self._tools.key_test('description',d))
            res['url'].append(self._tools.key_test('permalink_url',d))
        return res  
      
    def _parsing_data2(self,data):
        res = {'username':list(),'country':list(),'name':list(),'description':list(),'city':list(),'website':list(),'tracks':list(),'followers':list()}
        for d in data:
            res['username'].append(self._tools.key_test('username',d))
            res['country'].append(self._tools.key_test('country',d))
            res['name'].append(self._tools.key_test('full_name',d))
            res['description'].append(self._tools.key_test('description',d))
            res['city'].append(self._tools.key_test('city',d))
            res['website'].append(self._tools.key_test('website',d))
            res['tracks'].append(self._tools.key_test('track_count',d,'int'))
            res['followers'].append(self._tools.key_test('followers_count',d,'int'))
        return res   
    
    def _parsing_data3(self,data):
        res = {'name':list(),'tracks':list(),'members':list(),'contributors':list(),'url':list(),'description':list()}
        for d in data:
            res['name'].append(self._tools.key_test('name',d))
            res['tracks'].append(self._tools.key_test('track_count',d,'int'))
            res['members'].append(self._tools.key_test('members_count',d,'int'))
            res['contributors'].append(self._tools.key_test('contributors_count',d,'int'))
            res['url'].append(self._tools.key_test('permalink_url',d))
            res['description'].append(self._tools.key_test('description',d))
        return res    
        
    def _parsing_data4(self,data):
        res = {'id':list(),'text':list()}
        for d in data:
            res['id'].append(self._tools.key_test('track_id',d,'int'))
            res['text'].append(self._tools.key_test('body',d))
        return res
        
    def search_tracks(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'tracks.json?client_id='+self._api_key+'&q='+text+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 

    def get_infos_track(self,idd=182242225):
        url = self._api_url+'tracks/'+str(idd)+'?client_id='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def get_latest_tracks(self,limit=10):
        url = self._api_url+'tracks.json?client_id='+self._api_key+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)

    def search_users(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'users?client_id='+self._api_key+'&q='+text+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data)         
        
    def search_groups(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'groups?client_id='+self._api_key+'&q='+text+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data3(data)
        
    def get_latest_comments(self,limit=10):    
        url = self._api_url+'comments?client_id='+self._api_key+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data4(data)       
        