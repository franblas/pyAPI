# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 20:31:49 2015

@author: Paco
"""

import urllib, json, requests

class Utils(object):
    
    _class_name = 'Utils'    
    _category = 'Useful'
    _general_encoding = 'utf8'
    
    def __init__(self): pass
    
    def get_class_info(self):
        return self._class_name,self._category    

    def data_from_url(self,url):
        response = urllib.urlopen(url);        
        data = json.loads(response.read())
        return data

    def data_from_url_flickr(self,url):
        response = requests.get(url)
        data = json.loads(response.content.replace('jsonFlickrApi(','')[:-1])
        return data
        
    def _encode_str(self,text):
        if text is None:
            return ''
        else:    
            return text.encode(self._general_encoding)
     
    def _avoid_none(self,x,t='float'):
        if x is None:
            if t == 'float':
                return 0.0
            elif t == 'int':
                return 0
            else:
                return
        else:
            return x
       
    def key_test(self,key,d,t='str'):
        if d is not None and key in d:
            if t == 'str':
                return self._encode_str(d[key])
            else:
                if t == 'float':
                    return self._avoid_none(d[key],'float')
                elif t == 'int':
                    return self._avoid_none(d[key],'int')
                else:
                    return d[key]
        else:
            if t == 'str':
                return ''
            elif t == 'float':
                return 0.0
            elif t == 'int':
                return 0
            elif t == 'list':
                return []
            else:
                return
                   
    