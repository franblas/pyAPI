# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 14:37:01 2015

@author: Paco
"""

from api import API

class Dailymotion(API):
    
    _class_name = 'Dailymotion'    
    _category = 'Video'
    _help_url = 'http://www.programmableweb.com/news/how-to-use-dailymotion-api-to-leverage-video-search/how-to/2014/06/12'
    _api_url = 'https://api.dailymotion.com/'
        
    def _parsing_data(self,data):
        res = {'title':list(),'views':list(),'bookmarks':list(),'comments':list(),'country':list(),'url':list(),'tags':list()}
        for d in data['list']:
            res['title'].append(self._tools.key_test('title',d))
            res['views'].append(self._tools.key_test('views_total',d,'int'))
            res['comments'].append(self._tools.key_test('comments_total',d,'int'))
            res['bookmarks'].append(self._tools.key_test('bookmarks_total',d,'int'))
            res['country'].append(self._tools.key_test('country',d))
            res['url'].append(self._tools.key_test('url',d))
            res['tags'].append(self._tools.key_test('tags',d,'list'))
        return res        

    def _parsing_data2(self,data):
        res = {'title':list(),'description':list(),'videos':list()}
        for d in data['list']:
            res['title'].append(self._tools.key_test('name',d))
            res['description'].append(self._tools.key_test('description',d))
            res['videos'].append(self._tools.key_test('videos_total',d,'int'))
        return res        
 
    def _parsing_data3(self,data):
        res = {'title':list(),'description':list()}
        for d in data['list']:
            res['title'].append(self._tools.key_test('name',d))
            res['description'].append(self._tools.key_test('description',d))
        return res
   
    def search_videos(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'videos?fields=title,views_total,bookmarks_total,comments_total,country,url,tags&sort=relevance&search='+text+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
    
    def search_playlists(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'playlists?fields=name,description,videos_total&sort=relevance&search='+text+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data) 

    def search_groups(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'groups?fields=name,description&sort=relevance&search='+text+'&limit='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data3(data)
      
