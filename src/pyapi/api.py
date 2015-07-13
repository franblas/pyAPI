# -*- coding: utf-8 -*-
"""
Created on Fri Jun 05 21:13:32 2015

@author: Paco
"""

from utils import Utils

class API(object):

    _class_name = ''
    _category = ''
    _help_url = ''
    _api_url = ''
    _api_key = ''
    _version = '0'
    _nb_call = 0
    _tools = Utils()

    def __init__(self): pass

    def get_nb_call(self):
        return self._nb_call

    def get_class_info(self):
        return self._class_name,self._category,self._help_url,self._version,self._api_url,self._api_key

    def _increment_nb_call(self):
        self._nb_call = self._nb_call + 1

    def _parsing_data(self,data): pass
