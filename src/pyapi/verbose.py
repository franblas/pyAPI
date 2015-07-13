# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:40:05 2015

@author: Paco
"""

from colorama import Fore

class _Colors(object):
    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE

class Verbose(object):
    
   _text = ''
   _colors = _Colors()
    
   def __init__(self,text):
       self._text = text
          
   def cprint(self,color=_colors.BLUE): 
       print(color+self._text)
       print(Fore.RESET)


       