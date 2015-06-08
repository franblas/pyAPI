# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 20:31:49 2015

@author: Paco
"""

import urllib, json

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
        
    def _encode_str(self,text):
        if text is None:
            return ''
        else:    
            return text.encode(self._general_encoding)
            
    def key_test(self,key,d,t='str'):
        if key in d:
            if t == 'str':
                return self._encode_str(d[key])
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
                   
    