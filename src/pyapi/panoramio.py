# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 21:12:23 2015

@author: Paco
"""

from api import API

class Panoramio(API):
    
    _class_name = 'Panoramio'    
    _category = 'Picture'
    _help_url = 'http://www.panoramio.com/api/data/api.html'
    _api_url = 'http://www.panoramio.com/map/'
    
    def _parsing_data(self,data):
        res = {'latitude':list(),'longitude':list(),'owner':list(),'url':list(),'title':list(),'date':list()}
        for d in data['photos']:
            res['title'].append(self._tools.key_test('photo_title',d))
            res['owner'].append(self._tools.key_test('owner_name',d))
            res['latitude'].append(self._tools.key_test('latitude',d,'float'))
            res['longitude'].append(self._tools.key_test('longitude',d,'float'))
            res['url'].append(self._tools.key_test('photo_file_url',d))
            res['date'].append(self._tools.key_test('upload_date',d))
        return res  
        
    def get_popular_world(self,limit=10):
        url = self._api_url+'get_panoramas.php?order=popularity&set=public&from=0&to='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
        
    def get_photos_area(self,latitude=0,longitude=0,range=5,limit=10):
        minx = str(longitude - range)
        maxx = str(longitude + range)
        miny = str(latitude - range)
        maxy = str(latitude + range)
        url = self._api_url+'get_panoramas.php?order=popularity&set=public&minx='+minx+'&miny='+miny+'&maxx='+maxx+'&maxy='+maxy+'&from=0&to='+str(limit)
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        return self._parsing_data(data) 
        