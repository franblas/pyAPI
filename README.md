# pyAPI
Data from multiple APIs with python

## Install package  
```
python setup.py install
```

## Usage
```
from pyapi import reddit
r = reddit.Reddit()
r.search('cat')
```  

If the API need a key, use pyAPI as follow:  
```
from pyapi import soundcloud
s = soundcloud.Soundcloud('yourkey')
s.search_tracks('justice')
```  

## Documentation  
[Documentation of APIs](doc/apisDoc.md)
