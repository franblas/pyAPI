# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:52:40 2015

@author: Paco
"""

from api import API

class TheMovieDatabase(API):
    
    _class_name = 'The Movie Database'    
    _category = 'Movie'
    _help_url = 'https://www.themoviedb.org/documentation/api'
    _api_url = 'https://api.themoviedb.org/3/'
    
    def __init__(self,apikey):
        self._api_key = apikey
        
    def _parsing_data(self,data):
        res = {'id':list(),'lang':list(),'overview':list(),'title':list(),'popularity':list(),'date':list(),'note':list(),'count':list()}
        for d in data['results']:
            res['id'].append(self._tools.key_test('id',d,'int'))
            res['lang'].append(self._tools.key_test('original_language',d))
            res['title'].append(self._tools.key_test('original_title',d))
            res['overview'].append(self._tools.key_test('overview',d))
            res['popularity'].append(self._tools.key_test('popularity',d,'float'))
            res['date'].append(self._tools.key_test('release_date',d))
            res['note'].append(self._tools.key_test('vote_average',d,'float'))
            res['count'].append(self._tools.key_test('vote_count',d,'int'))
        return res        

    def _parsing_data2(self,data):
        res = {'id':list(),'lang':list(),'title':list(),'popularity':list(),'date':list(),'note':list(),'count':list()}
        for d in data['results']:
            res['id'].append(self._tools.key_test('id',d,'int'))
            res['lang'].append(self._tools.key_test('origin_country',d,'list'))
            res['title'].append(self._tools.key_test('original_name',d))
            res['popularity'].append(self._tools.key_test('popularity',d,'float'))
            res['date'].append(self._tools.key_test('first_air_date',d))
            res['note'].append(self._tools.key_test('vote_average',d,'float'))
            res['count'].append(self._tools.key_test('vote_count',d,'int'))
        return res 

    def _parsing_data3(self,data):
        res = {'id':list(),'name':list(),'popularity':list(),'known_for':list()}
        for d in data['results']:
            res['id'].append(self._tools.key_test('id',d,'int'))
            res['known_for'].append(self._tools.key_test('known_for',d,'list'))
            res['name'].append(self._tools.key_test('name',d))
            res['popularity'].append(self._tools.key_test('popularity',d,'float'))
        return res

    def _parsing_data4(self,data):
        rest = {'id':list(),'lang':list(),'title':list(),'popularity':list(),'date':list(),'note':list(),'count':list()}
        resm = {'id':list(),'lang':list(),'overview':list(),'title':list(),'popularity':list(),'date':list(),'note':list(),'count':list()}     
        for d in data['results']:
            if(len(d)==11):
                rest['id'].append(self._tools.key_test('id',d,'int'))
                rest['lang'].append(self._tools.key_test('origin_country',d,'list'))
                rest['title'].append(self._tools.key_test('original_name',d))
                rest['popularity'].append(self._tools.key_test('popularity',d,'float'))
                rest['date'].append(self._tools.key_test('first_air_date',d))
                rest['note'].append(self._tools.key_test('vote_average',d,'float'))
                rest['count'].append(self._tools.key_test('vote_count',d,'int'))
            elif(len(d)==15):
                resm['id'].append(self._tools.key_test('id',d,'int'))
                resm['lang'].append(self._tools.key_test('original_language',d))
                resm['title'].append(self._tools.key_test('original_title',d))
                resm['overview'].append(self._tools.key_test('overview',d))
                resm['popularity'].append(self._tools.key_test('popularity',d,'float'))
                resm['date'].append(self._tools.key_test('release_date',d))
                resm['note'].append(self._tools.key_test('vote_average',d,'float'))
                resm['count'].append(self._tools.key_test('vote_count',d,'int'))
            else: pass        
        return rest,resm

    # which = upcoming, now_playing, popular or top_rated
    def movies(self,which='popular',page=1):
        url = self._api_url+'movie/'+which+'?page='+str(page)+'&api_key='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 

    # which = on_the_air, airing_today, popular or top_rated
    def tv(self,which='popular',page=1):
        url = self._api_url+'tv/'+which+'?page='+str(page)+'&api_key='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data2(data)

    def people(self,page=1):
        url = self._api_url+'person/popular?page='+str(page)+'&api_key='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data3(data)

    def search(self,text='',page=1):
        text = text.replace(' ','+')
        url = self._api_url+'search/multi?page='+str(page)+'&query='+text+'&api_key='+self._api_key
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data4(data)        