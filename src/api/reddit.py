# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 21:46:34 2015

@author: Paco
"""

from api import API

class Reddit(API):
    
    _class_name = 'Reddit'    
    _category = 'Social'
    _help_url = 'http://www.reddit.com/dev/api'
    _api_url = 'http://www.reddit.com/'
    
    def _parsing_data(self,data):
        res = {'title':list(),'text':list(),'url':list(),'score':list(),'ups':list(),'num_comments':list(),'subreddit':list()}
        for d in data['data']['children']:
            res['title'].append(self._tools.key_test('title',d['data']))
            res['text'].append(self._tools.key_test('selftext',d['data']))
            res['url'].append(self._tools.key_test('url',d['data']))
            res['score'].append(self._tools.key_test('score',d['data'],'float'))
            res['ups'].append(self._tools.key_test('ups',d['data'],'int'))
            res['subreddit'].append(self._tools.key_test('subreddit',d['data']))
            res['num_comments'].append(self._tools.key_test('num_comments',d['data'],'int'))
        return res  
    
    def _parsing_data2(self,data):
        res = {'name':list(),'subscribers':list()}
        for d in data['data']['children']:
            res['name'].append(self._tools.key_test('display_name',d['data']))
            res['subscribers'].append(self._tools.key_test('subscribers',d['data'],'list'))
        return res     

    def search(self,text='',limit=10):
        text = text.replace(' ','+') 
        url = self._api_url+'search.json?q='+text+'&t=year&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
        
    def get_hot(self,limit=10):
        url = self._api_url+'hot.json?limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
        
    def get_controversial(self,limit=10):
        url = self._api_url+'controversial.json?limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
   
    def get_random(self): pass
        
    def get_popular_subreddits(self,limit=10):
        url = self._api_url+'subreddits/popular.json?limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data)          
        
    def search_subreddits(self,text='',limit=10):    
        url = self._api_url+'subreddits/search.json?q='+text+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data)          
        