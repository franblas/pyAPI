# -*- coding: utf-8 -*-
"""
Created on Sat Jun 06 12:27:38 2015

@author: Paco
"""

from api import API

class GoogleBooks(API):
    
    _class_name = 'Google Books'    
    _category = 'Book'
    _help_url = 'https://developers.google.com/books/docs/v1/using#RetrievingVolume'
    _api_url = 'https://www.googleapis.com/books/v1/'
    
    def _parsing_data(self,data):
        res = {'title':list(),'publishedDate':list(),'canonicalVolumeLink':list(),'description':list(),'pageCount':list(),'categories':list()}
        for d in data['items']:
            res['title'].append(self._tools.key_test('title',d['volumeInfo']))
            res['publishedDate'].append(self._tools.key_test('publishedDate',d['volumeInfo']))
            res['canonicalVolumeLink'].append(self._tools.key_test('canonicalVolumeLink',d['volumeInfo']))
            res['description'].append(self._tools.key_test('description',d['volumeInfo']))
            res['pageCount'].append(self._tools.key_test('pageCount',d['volumeInfo'],'int'))
            res['categories'].append(self._tools.key_test('categories',d['volumeInfo'],'list'))
        return res  
        
    def search_by_author(self,author='',limit=10):
        author = author.replace(' ','+')
        url = self._api_url+'volumes?q=inauthor:'+author+'&maxResults='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 

    def search_book(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'volumes?q='+text+'&maxResults='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data)         
