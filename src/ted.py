# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:35:08 2015

@author: Paco
"""

from api import API

class Ted(API):
    
    _class_name = 'Ted'    
    _category = 'Event'
    _help_url = 'http://developer.ted.com/io-docs'
    _api_url = 'https://api.ted.com/v1/'
    
    def __init__(self,apikey):
        self._api_key = apikey
        
    def _parsing_data(self,data):
        res = {'id':list(),'title':list(),'description':list(),'date':list()}
        for d in data['results']:
            k = self._tools._encode_str(d.keys()[0])
            res['id'].append(self._tools.key_test('id',d[k],'int'))
            res['description'].append(self._tools.key_test('description',d[k]))
            if k == 'talk':
                res['date'].append(self._tools.key_test('recorded_at',d[k]))
                res['title'].append(self._tools.key_test('name',d[k]))
            elif k == 'playlist':
                res['date'].append(self._tools.key_test('created_at',d[k]))
                res['title'].append(self._tools.key_test('title',d[k]))
            else: pass    
        return res        

    def _parsing_data2(self,data):
        res = {'id':list(),'title':list(),'description':list(),'summary':list()}
        for d in data['themes']:
            res['id'].append(self._tools.key_test('id',d['theme'],'int'))
            res['description'].append(self._tools.key_test('description',d['theme']))
            res['title'].append(self._tools.key_test('name',d['theme']))
            res['summary'].append(self._tools.key_test('shortsummary',d['theme']))
        return res

    def _parsing_data3(self,data,data2):
        res = {'firstname':list(),'lastname':list(),'description':list()}
        for d,dd in zip(data['speakers'],data2['tedx_speakers']):
            res['firstname'].append(self._tools.key_test('firstname',d['speaker']))
            res['lastname'].append(self._tools.key_test('lastname',d['speaker']))
            res['description'].append(self._tools.key_test('whotheyare',d['speaker']))            
            res['firstname'].append(self._tools.key_test('first_name',dd['tedx_speaker']))
            res['lastname'].append(self._tools.key_test('last_name',dd['tedx_speaker']))
            res['description'].append(self._tools.key_test('description',dd['tedx_speaker']))
        return res

    def _parsing_data4(self,data,data2):
        res = {'description':list(),'title':list(),'date':list(),'url':list()}
        resx = {'title':list(),'description':list(),'twitter':list(),'date':list(),'flickr':list(),'youtube':list()} 
        for d,dd in zip(data['events'],data2['tedx_events']):
            res['description'].append(self._tools.key_test('description',d['event']))
            res['title'].append(self._tools.key_test('name',d['event']))
            res['date'].append(self._tools.key_test('starts_at',d['event']))            
            res['url'].append(self._tools.key_test('url',d['event']))
            resx['description'].append(self._tools.key_test('description',dd['tedx_event']))
            resx['title'].append(self._tools.key_test('title',dd['tedx_event']))
            resx['date'].append(self._tools.key_test('ends_at',dd['tedx_event']))                        
            resx['twitter'].append(self._tools.key_test('twitter_codes',dd['tedx_event']))            
            resx['flickr'].append(self._tools.key_test('flickr_tags',dd['tedx_event']))
            resx['youtube'].append(self._tools.key_test('you_tube_playlist',dd['tedx_event']))
        return res,resx

    def _parsing_data5(self,data):
        res = {'id':list(),'title':list(),'description':list(),'date':list()}
        for d in data['talks']:
            res['id'].append(self._tools.key_test('id',d['talk'],'int'))
            res['description'].append(self._tools.key_test('description',d['talk']))
            res['date'].append(self._tools.key_test('recorded_at',d['talk']))
            res['title'].append(self._tools.key_test('name',d['talk']))
        return res

    def search(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'search.json?q='+text+'&api-key='+self._api_key+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 

    def get_themes(self,limit=10):
        url = self._api_url+'themes.json?&api-key='+self._api_key+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data) 

    def get_speakers(self,limit=10):
        url = self._api_url+'speakers.json?&api-key='+self._api_key+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        url2 = self._api_url+'tedx_speakers.json?&api-key='+self._api_key+'&limit='+str(limit)
        data2 = self._tools.data_from_url(url2)
        self._increment_nb_call()
        return self._parsing_data3(data,data2)    
        
    def get_events(self,limit=10):
        url = self._api_url+'events.json?&api-key='+self._api_key+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        url2 = self._api_url+'tedx_events.json?&api-key='+self._api_key+'&limit='+str(limit)
        data2 = self._tools.data_from_url(url2)
        self._increment_nb_call()
        return self._parsing_data4(data,data2)
        
    def get_talks(self,limit=10):
        url = self._api_url+'talks.json?&api-key='+self._api_key+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data5(data) 
        