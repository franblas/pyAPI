# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 14:53:16 2015

@author: Paco
"""

from api import API

class Ebay(API):
    
    _class_name = 'Ebay'    
    _category = 'Shopping'
    _help_url = 'http://developer.ebay.com/'
    _api_url = 'http://svcs.ebay.com/'
    _api_url2 = 'http://open.api.ebay.com/'
    
    def __init__(self,apikey):
        self._api_key = apikey
        
    def _parsing_data(self,data):
        res = {'id':list(),'title':list(),'category':list(),'url':list(),'location':list(),'status':list()}
        for d in data['findItemsByKeywordsResponse'][0]['searchResult'][0]['item']:
            res['id'].append(self._tools.key_test('itemId',d))
            res['title'].append(self._tools.key_test('title',d,'list'))
            res['category'].append(self._tools.key_test('primaryCategory',d,'list'))
            res['url'].append(self._tools.key_test('viewItemURL',d,'list'))
            res['location'].append(self._tools.key_test('location',d,'list'))
            res['status'].append(self._tools.key_test('sellingStatus',d,'list'))
        return res        
    
    def _parsing_data2(self,data):
        res = {'id':list(),'title':list(),'category':list(),'url':list(),'country':list(),'price':list()}
        for d in data['getMostWatchedItemsResponse']['itemRecommendations']['item']:
            res['id'].append(self._tools.key_test('itemId',d))
            res['title'].append(self._tools.key_test('title',d))
            res['category'].append(self._tools.key_test('primaryCategoryName',d))
            res['url'].append(self._tools.key_test('viewItemURL',d))
            res['country'].append(self._tools.key_test('country',d))
            res['price'].append(self._tools.key_test('buyItNowPrice',d,'list'))
        return res    

    def _parsing_data3(self,data):
        res = {'category':list(),'title':list(),'url':list(),'country':list(),'price':list()}
        for d in data['getSimilarItemsResponse']['itemRecommendations']['item']:
            res['title'].append(self._tools.key_test('title',d))
            res['category'].append(self._tools.key_test('primaryCategoryName',d))
            res['url'].append(self._tools.key_test('viewItemURL',d))
            res['country'].append(self._tools.key_test('country',d))
            res['price'].append(self._tools.key_test('buyItNowPrice',d,'list'))
        return res 
    
    def _parsing_data4(self,data):
        res = {'alternative':list(),'related':list()}
        for d in data['PopularSearchResult']:
            res['alternative'].append(self._tools.key_test('AlternativeSearches',d))
            res['related'].append(self._tools.key_test('RelatedSearches',d))
        return res    
    
    def search(self,text='',limit=10):
        text = text.replace(' ','+')
        url = self._api_url+'services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME='+self._api_key+'&RESPONSE-DATA-FORMAT=json&keywords='+text+'&paginationInput.entriesPerPage='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
    
    def get_most_watched(self,limit=10):
        url = self._api_url+'MerchandisingService?OPERATION-NAME=getMostWatchedItems&SERVICE-NAME=MerchandisingService&CONSUMER-ID='+self._api_key+'&RESPONSE-DATA-FORMAT=JSON&maxResults='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data)      

    def get_similar(self,idd=121187584160,limit=10):
        url = self._api_url+'MerchandisingService?OPERATION-NAME=getSimilarItems&SERVICE-NAME=MerchandisingService&CONSUMER-ID='+self._api_key+'&RESPONSE-DATA-FORMAT=JSON&itemId='+str(idd)+'&maxResults='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data3(data)  

    def get_popular_search(self,text=''):
        text = text.replace(' ','+')
        url = self._api_url2+'shopping?callname=FindPopularSearches&responseencoding=JSON&appid='+self._api_key+'&siteid=0&version=531&QueryKeywords='+text
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data4(data)