# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 16:45:29 2015

@author: Paco
"""

from api import API

class Flickr(API):
    
    _class_name = 'Flickr'    
    _category = 'Picture'
    _help_url = 'https://www.flickr.com/services/api/'
    _api_url = 'https://api.flickr.com/services/'
    
    def __init__(self,apikey):
        self._api_key = apikey
        
    def _parsing_data(self,data):
        res = {'id':list(),'owner':list(),'secret':list(),'title':list()}
        for d in data['photos']['photo']:
            res['id'].append(self._tools.key_test('id',d))
            res['owner'].append(self._tools.key_test('owner',d))
            res['secret'].append(self._tools.key_test('secret',d))
            res['title'].append(self._tools.key_test('title',d))
        return res        
    
    def _parsing_data2(self,data):
        res = {'comments':list(),'description':list(),'posted':list(),'tags':list(),'title':list(),'url':list(),'views':list()}
        d = data['photo']
        res['comments'].append(self._tools.key_test('_content',d['comments']))
        res['description'].append(self._tools.key_test('_content',d['description']))
        res['posted'].append(self._tools.key_test('posted',d['dates'])) 
        res['tags'].append(self._tools.key_test('tag',d['tags'],'list'))
        res['title'].append(self._tools.key_test('_content',d['title']))
        res['url'].append(self._tools.key_test('_content',d['urls']['url'][0]))
        res['views'].append(self._tools.key_test('views',d))
        return res     
    
    def search(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'rest/?method=flickr.photos.search&format=json&api_key='+self._api_key+'&text='+text+'&per_page='+str(limit)
        data = self._tools.data_from_url_flickr(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
 
    def get_infos(self,idd=18644022901):
        url = self._api_url+'rest/?method=flickr.photos.getInfo&format=json&api_key='+self._api_key+'&photo_id='+str(idd)
        data = self._tools.data_from_url_flickr(url)
        self._increment_nb_call()
        return self._parsing_data2(data)      
