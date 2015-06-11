# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 20:31:49 2015

@author: Paco
"""

import urllib, json, requests
from verbose import Verbose

class Utils(object):
    
    _class_name = 'Utils'    
    _category = 'Useful'
    _general_encoding = 'utf8'
    _rss_url_parser = 'https://ajax.googleapis.com/ajax/services/feed/load?v=2.0&q=' 
    _verbose = True    
    
    def __init__(self): pass
    
    def get_class_info(self):
        return self._class_name,self._category    

    def data_from_url(self,url):
        try:
            response = urllib.urlopen(url)    
            data = json.loads(response.read())
            if self._verbose:
                Verbose('GET: '+url).cprint()
            return data    
        except:
            if self._verbose:
                Verbose('GET: '+url).cprint(Verbose._colors.RED)
            return {}

    def data_from_url_flickr(self,url):
        try:
            response = requests.get(url)
            data = json.loads(response.content.replace('jsonFlickrApi(','')[:-1])
            if self._verbose:
                Verbose('GET: '+url).cprint()
            return data
        except:
            if self._verbose:
                Verbose('GET: '+url).cprint(Verbose._colors.RED)
            return {}
            
    def rss_parser(self,url):
        temp = self._rss_url_parser+str(url)
        return self.data_from_url(temp)      
        
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
                   
    