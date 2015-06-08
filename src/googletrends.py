# -*- coding: utf-8 -*-
"""
Created on Sun Jun 07 22:04:18 2015

@author: Paco
"""

from api import API

class GoogleTrends(API):
    
    _class_name = 'Google Trends'    
    _category = 'Data'
    _help_url = ''
    _api_url = 'http://hawttrends.appspot.com/api/'
   
    _country = ["South Africa","Germany","Saudi Arabia","Argentina","Australia","Austria","Belgium","Brazil","Canada","Chilia","Colombia","South Korea","Danemark","Egypt","Spain","USA","Finland","France","Greece","Hong Kong","Hongria","India","Indonesia","Israel","Italia","Japan","Kenya","Malaisia","Mexico","Nigeria","Norway","Holland","Philippines","Poland","Portugal","Czech Republic","Roumania","UK","Russia","Singapour","Sweden","Switzerland","Taiwan","Thailand","Turkey","Ukraine","Vietnam"]
    _cid = [40,15,36,30,8,44,41,18,13,38,32,23,49,29,26,1,50,16,48,10,45,3,19,6,27,4,37,34,21,52,51,17,25,31,47,43,39,9,14,5,42,46,12,33,24,35,28]
  
    def _parsing_data(self,data,idd):
        res = {'trends':list()}
        for d in data[str(idd)]:
            res['trends'].append(self._tools._encode_str(d))
        return res  
        
    def get_trends(self,name='USA'):
        url = self._api_url+'terms/'
        data = self._tools.data_from_url(url)
        self._increment_nb_call()
        idd = self._cid[self._country.index(name)]
        return self._parsing_data(data,idd) 