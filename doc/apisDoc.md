# APIs

## Sumup

<table>
<thead>
<tr>
	<th>API name</th>
	<th>Category</th>
	<th>Need key ?</th>
</tr>
</thead>
<tbody>
<tr>
	<td><a href='#500px'>500 px</a></td>
	<td>Picture</td>
	<td>Yes</td>
</tr>
<tr>
	<td><a href='#9gag'>9 Gag</a></td>
	<td>Social</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#crunchbase'>Crunchbase</a></td>
	<td>Data</td>
	<td>Yes</td>
</tr>
<tr>
	<td><a href='#dailymotion'>Dailymotion</a></td>
	<td>Video</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#delicious'>Delicious</a></td>
	<td>Social</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#docker'>Docker</a></td>
	<td>Code</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#ebay'>Ebay</a></td>
	<td>Shopping</td>
	<td>Yes</td>
</tr>
<tr>
	<td><a href='#eventbrite'>Eventbrite</a></td>
	<td>Event</td>
	<td>Yes</td>
</tr>
<tr>
	<td><a href='#eventful'>Eventful</a></td>
	<td>Event</td>
	<td>Yes</td>
</tr>
<tr>
	<td><a href='#flickr'>Flickr</a></td>
	<td>Picture</td>
	<td>Yes</td>
</tr>
<tr>
	<td><a href='#freebase'>Freebase</a></td>
	<td>Data</td>
	<td>Yes</td>
</tr>
<tr>
	<td><a href='#googlebooks'>GoogleBooks</a></td>
	<td>Book</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#googletrends'>GoogleTrends</a></td>
	<td>Data</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#imdb'>Imdb</a></td>
	<td>Movie</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#instagram'>Instagram</a></td>
	<td>Picture</td>
	<td>Yes</td>
</tr>
<tr>
	<td><a href='#osm'>Osm</a></td>
	<td>Map</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#panoramio'>Panoramio</a></td>
	<td>Picture</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#pinterest'>Pinterest</a></td>
	<td>Social</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#reddit'>Reddit</a></td>
	<td>Social</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#rubygems'>RubyGems</a></td>
	<td>Code</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#soundcloud'>SoundCloud</a></td>
	<td>Music</td>
	<td>Yes</td>
</tr>
<tr>
	<td><a href='#spotify'>Spotify</a></td>
	<td>Music</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#ted'>Ted</a></td>
	<td>Event</td>
	<td>Yes</td>
</tr>
<tr>
	<td><a href='#themoviedatabase'>The Movie Database</a></td>
	<td>Movie</td>
	<td>Yes</td>
</tr>
<tr>
	<td><a href='#tumblr'>Tumblr</a></td>
	<td>Social</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#venmo'>Venmo</a></td>
	<td>Payement</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#vine'>Vine</a></td>
	<td>Video</td>
	<td>No</td>
</tr>
<tr>
	<td><a href='#wikipedia'>Wikipedia</a></td>
	<td>Data</td>
	<td>No</td>
</tr>
</tbody>
</table>

## <a id="500px"></a>500 px
### Dictionary structure
```
get_popular(limit=10)       
```  
```
get_best_rated(limit=10)       
```  
```
get_today(limit=10)       
```  
```
search(text='',limit=10)       
```
```
get_stories(limit=10)
```
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Name of the picture</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the picture</td>
</tr>
<tr>
	<td>latitude</td>
	<td>Latitude where the picture is taken</td>
</tr>
<tr>
	<td>longitude</td>
	<td>Longitude where the picture is taken</td>
</tr>
<tr>
	<td>link</td>
	<td>Url of the picture</td>
</tr>
<tr>
	<td>usercountry</td>
	<td>Original country of the user</td>
</tr>
</tbody>
</table>

## <a id="9gag"></a>9 Gag
### Dictionary structure
```
get_trend()
```  
```
get_hot()
```
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Name of the article</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the article</td>
</tr>
</tbody>
</table>

## <a id="crunchbase"></a>Crunchbase
## Dictionary structure
```
new_organisations()
```  
```
updated_organizations()
```  
```
search_organization(text='')
```  
```
new_people()
```  
```
new_products()
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> - </td>
	<td>Data asked for</td>
</tr>
</tbody>
</table>

## <a id="dailymotion"></a>Dailymotion
### Dictionary structure
```
search_videos(text='',limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Name of the video</td>
</tr>
<tr>
	<td>views</td>
	<td>Total views for the video</td>
</tr>
<tr>
	<td>bookmarks</td>
	<td>Total number of bookmarks for the video</td>
</tr>
<tr>
	<td>comments</td>
	<td>Total number of comments for the video</td>
</tr>
<tr>
	<td>country</td>
	<td>Original country of the video</td>
</tr>
<tr>
	<td>url</td>
	<td>Url of the video</td>
</tr>
<tr>
	<td>tags</td>
	<td>Words associated with the video</td>
</tr>
</tbody>
</table>
### Dictionary structure 2
```
search_playlists(text='',limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Name of the playlist</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the playlist</td>
</tr>
<tr>
	<td>videos</td>
	<td>Total number of videos into the playlist</td>
</tr>
</tbody>
</table>
### Dictionary structure 3
```
search_groups(text='',limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Name of the group</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the group</td>
</tr>
</tbody>
</table>
## <a id="delicious"></a>Delicious
### Dictionary structure
```
search(text='', limit=10)
```  
```
get_recent(limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>d</td>
	<td>Title of the link</td>
</tr>
<tr>
	<td>u</td>
	<td>Url of the link</td>
</tr>
<tr>
	<td>t</td>
	<td>Tags for the link</td>
</tr>
</tbody>
</table>
## <a id="docker"></a>Docker
### Dictionary structure
```
search(text='', limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>name</td>
	<td>Name of the image</td>
</tr>
<tr>
	<td>star_count</td>
	<td>Popularity of the repository</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the image</td>
</tr>
</tbody>
</table>

## <a id="ebay"></a>Ebay
### Dictionary structure
```
search(text='', limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>id</td>
	<td>Id of the item</td>
</tr>
<tr>
	<td>title</td>
	<td>Name of the announce</td>
</tr>
<tr>
	<td>category</td>
	<td>Category of the item</td>
</tr>
<tr>
	<td>url</td>
	<td>Url of the announce</td>
</tr>
<tr>
	<td>location</td>
	<td>Location of the announce</td>
</tr>
<tr>
	<td>status</td>
	<td>Price of the item</td>
</tr>
</tbody>
</table>
### Dictionary structure 2
```
get_most_watched(limit=10)
```  
<table>
<thead>
<tr>
	<th>KeyKey</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>id</td>
	<td>Id of the item</td>
</tr>
<tr>
	<td>title</td>
	<td>Name of the announce</td>
</tr>
<tr>
	<td>category</td>
	<td>Category of the item</td>
</tr>
<tr>
	<td>url</td>
	<td>Url of the announce</td>
</tr>
<tr>
	<td>country</td>
	<td>Original country of the announce</td>
</tr>
<tr>
	<td>price</td>
	<td>Price of the item</td>
</tr>
</tbody>
</table>
### Dictionary structure 3
```
get_similar(idd='121187584160', limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Name of the announce</td>
</tr>
<tr>
	<td>category</td>
	<td>Category of the item</td>
</tr>
<tr>
	<td>url</td>
	<td>Url of the announce</td>
</tr>
<tr>
	<td>country</td>
	<td>Original country of the announce</td>
</tr>
<tr>
	<td>price</td>
	<td>Price of the item</td>
</tr>
</tbody>
</table>

### Dictionary structure 5
```
get_popular_search(text='')
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>alternative</td>
	<td>Alternatives search for a given keyword</td>
</tr>
<tr>
	<td>related</td>
	<td>Related search for a given keyword</td>
</tr>
</tbody>
</table>
## <a id="eventbrite"></a>Eventbrite
### Dictionary structure
```
search(text='')
```  
```
get_popular()
```  
```
get_by_city(text='')
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>name</td>
	<td>Title of the event</td>
</tr>
<tr>
	<td>category</td>
	<td>Category of the event</td>
</tr>
<tr>
	<td>latitude</td>
	<td>Latitude of the event</td>
</tr>
<tr>
	<td>longitude</td>
	<td>Longitude of the event</td>
</tr>
<tr>
	<td>pa</td>st
	<td>Number of past events for the given group</td>
</tr>
<tr>
	<td>future</td>
	<td>Number of future events for the given group</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the event</td>
</tr>
</tbody>
</table>

## <a id="googlebooks"></a>Google Books
### Dictionary structure
```
search_by_author(author='', limit=10)
```  
```
search_book(text='', limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Title of the book</td>
</tr>
<tr>
	<td>publishedDate</td>
	<td>Date of the book</td>
</tr>
<tr>
	<td>canonicalVolumeLink</td>
	<td>Url of the book</td>
</tr>
<tr>
	<td>pageCount</td>
	<td>Number of pages</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the book</td>
</tr>
<tr>
	<td>categories</td>
	<td>Categories of the book</td>
</tr>
</tbody>
</table>

## <a id="googletrends"></a>Google Trends
### Countries available
South Africa,Germany,Saudi Arabia,Argentina,Australia,Austria,Belgium,Brazil,Canada,Chilia,Colombia,South Corea,Denemark,Egypt,Spain,USA,Finland,France,Greece,Hong Kong,Hongria,India,Indonesia,Israel,Italia,Japan,Kenya,Malaisia,Mexico,Nigeria,Norway,Holland,Philippines,Poland,Portugal,Czech Republic,Roumania,UK,Russia,Singapour,Sweden,Switzerland,Taiwan,Thailand,Turkey,Ukraine,Vietnam   
### Dictionary structure
```
get_trends(name='USA')
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> - </td>
	<td>Trends from the country</td>
</tr>
</tbody>
</table>

## <a id="imdb"></a>Imdb 
### Dictionary structure
```
search_omdb(text='')
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> title </td>
	<td>Title of the media</td>
</tr>
<tr>
	<td> year </td>
	<td>Year of release</td>
</tr>
<tr>
	<td> type </td>
	<td>Type of media</td>
</tr>
</tbody>
</table>

### Dictionary structure 2
```
search_title(text='')
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> popular </td>
	<td>Title of the media</td>
</tr>
<tr>
	<td> exact </td>
	<td>Exact title of the media</td>
</tr>
</tbody>
</table>

### Dictionary structure 3
```
search_name(text='')
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> popular </td>
	<td>Name of the media</td>
</tr>
<tr>
	<td> exact </td>
	<td>Exact name of the media</td>
</tr>
</tbody>
</table>

## <a id="instagram"></a>Instagram
### Dictionary structure
```
get_popular(limit=10)
```
```
search_by_coordinates(lat=48.858844,lon=2.294351,limit=10)
```
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> link </td>
	<td>Lnk of the content</td>
</tr>
<tr>
	<td> name </td>
	<td>Name of the picture</td>
</tr>
<tr>
	<td> com </td>
	<td>Comments of the picture</td>
</tr>
<tr>
	<td> latitude </td>
	<td>Latitude of the content</td>
</tr>
<tr>
	<td> longitude </td>
	<td>Longitude of the content</td>
</tr>
<tr>
	<td> count_com </td>
	<td>Number of commentaries</td>
</tr>
<tr>
	<td> count_like </td>
	<td>Number of likes</td>
</tr>
<tr>
	<td> title </td>
	<td>Title of the content</td>
</tr>
</tbody>
</table>
  
### Dictionary structure 2
```
get_tags(text='')
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> count </td>
	<td>Tag's popularity</td>
</tr>
<tr>
	<td> name </td>
	<td>Tag's name</td>
</tr>
</tbody>
</table>

### Dictionary structure 3
```
search_locations(lat=48.858844,lon=2.294351,limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> name </td>
	<td>Place's name</td>
</tr>
<tr>
	<td> latitude </td>
	<td>Place's latitude</td>
</tr>
<tr>
	<td> longitude </td>
	<td>Place's longitude</td>
</tr>
</tbody>
</table>
### Dictionary structure 4
```
search_users(text='',limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> username </td>
	<td>User's name</td>
</tr>
<tr>
	<td> name </td>
	<td>Full user's name</td>
</tr>
<tr>
	<td> id </td>
	<td>User's id</td>
</tr>
<tr>
	<td> pic </td>
	<td>User's profile picture</td>
</tr>
</tbody>
</table>

## <a id="osm"></a>OSM 
### Dictionary structure
```
search_notes(text='', limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> coordinates </td>
	<td>Coordinates of the place</td>
</tr>
<tr>
	<td> comments </td>
	<td>Comments on the place</td>
</tr>
</tbody>
</table>

### Dictionary structure 2
```
search(text='', limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> latitude </td>
	<td>Latitude of the place</td>
</tr>
<tr>
	<td> longitude </td>
	<td>Longitude of the place</td>
</tr>
<tr>
	<td> name </td>
	<td>Names of the place</td>
</tr>
<tr>
	<td> importance </td>
	<td>Relevance of the place, regarding the research</td>
</tr>
</tbody>
</table>

### Dictionary structure 3
```
get_coordinates_city(text='')
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> latitude </td>
	<td>Latitude of the place</td>
</tr>
<tr>
	<td> longitude </td>
	<td>Longitude of the place</td>
</tr>
</tbody>
</table>

## <a id="panoramio"></a>Panoramio
### Dictionary structure
```
get_popular_world(limit=10)
```  
```
get_photos_area(latitude=0, longitude=0, range=5, limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>latitude</td>
	<td>Latitude of the place</td>
</tr>
<tr>
	<td>longitude</td>
	<td>Longitude of the place</td>
</tr>
<tr>
	<td>owner</td>
	<td>Owner of the picture</td>
</tr>
<tr>
	<td>url</td>
	<td>Url of the picture</td>
</tr>
<tr>
	<td>title</td>
	<td>Title of the picture</td>
</tr>
<tr>
	<td>date</td>
	<td>Date of the picture</td>
</tr>
</tbody>
</table>

## <a id="reddit"></a>Reddit
### Dictionary structure
```
search(text='', limit=10)
```  
```
get_hot(limit=10)
```  
```
get_controversial(limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Title of the article</td>
</tr>
<tr>
	<td>url</td>
	<td>Url of the article</td>
</tr>
<tr>
	<td>score</td>
	<td>Score of the article</td>
</tr>
<tr>
	<td>ups</td>
	<td>Score of the article</td>
</tr>
<tr>
	<td>num_comments</td>
	<td>Number of comments for the article</td>
</tr>
<tr>
	<td>subreddit</td>
	<td>Subreddit of the article</td>
</tr>
<tr>
	<td>text</td>
	<td>Text of the article</td>
</tr>
</tbody>
</table>

### Dictionary structure 2
```
get_popular_subreddits(limit=10)
search_subreddits(text='',limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>name</td>
	<td>Name of the subreddit</td>
</tr>
<tr>
	<td>subscribers</td>
	<td>Number of users for the subreddit</td>
</tr>
</tbody>
</table>

## <a id="rubygems"></a>RubyGems
### Dictionary structure
```
search(text='')
```  
```
latest_added()
```  
```
latest_updated()
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>name</td>
	<td>Name of the gem</td>
</tr>
<tr>
	<td>downloads</td>
	<td>Number of downloads of the gem</td>
</tr>
<tr>
	<td>info</td>
	<td>Description of the gem</td>
</tr>
<tr>
	<td>url</td>
	<td>Url of the projects gem</td>
</tr>
</tbody>
</table>

### Dictionary structure 2
```
total_download_gems <- function(.)
```   
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> - </td>
	<td>Total number of download gems</td>
</tr>
</tbody>
</table>

## <a id="soundcloud"></a>Soundcloud
### Dictionary structure
```
search_tracks(text='', limit=10)
```  
```
get_infos_track(idc=182242225)
```  
```
get_latest_tracks(limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Title of the track</td>
</tr>
<tr>
	<td>downloads</td>
	<td>Number of downloads</td>
</tr>
<tr>
	<td>favorites</td>
	<td>Number of favorites</td>
</tr>
<tr>
	<td>comments</td>
	<td>Number of comments</td>
</tr>
<tr>
	<td>genre</td>
	<td>Genre of the track</td>
</tr>
<tr>
	<td>duration</td>
	<td>Duration of the track</td>
</tr>
<tr>
	<td>tags</td>
	<td>Tags for the track</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the track</td>
</tr>
<tr>
	<td>url</td>
	<td>Url of the track</td>
</tr>
</tbody>
</table>

### Dictionary structure 2
```
search_users(text='', limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>username</td>
	<td>Nickname of the user</td>
</tr>
<tr>
	<td>country</td>
	<td>Country of the user</td>
</tr>
<tr>
	<td>name</td>
	<td>Name of the user</td>
</tr>
<tr>
	<td>description</td>
	<td>Description for the profile</td>
</tr>
<tr>
	<td>city</td>
	<td>City of the user</td>
</tr>
<tr>
	<td>website</td>
	<td>Webiste of the user</td>
</tr>
<tr>
	<td>tracks</td>
	<td>Number of tracks</td>
</tr>
<tr>
	<td>followers</td>
	<td>Number of followers</td>
</tr>
</tbody>
</table>

### Dictionary structure 3
```
search_groups(text='', limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>name</td>
	<td>Name of the group</td>
</tr>
<tr>
	<td>tracks</td>
	<td>Number of groups tracks</td>
</tr>
<tr>
	<td>members</td>
	<td>Number of groups members</td>
</tr>
<tr>
	<td>contributors</td>
	<td>Number of groups contributors</td>
</tr>
<tr>
	<td>url</td>
	<td>Url of the group</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the group</td>
</tr>
</tbody>
</table>

### Dictionary structure 4
```
get_latest_comments(limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>id</td>
	<td>Id of the track</td>
</tr>
<tr>
	<td>text</td>
	<td>Latest comment for the track</td>
</tr>
</tbody>
</table>

## <a id="tumblr"></a>Tumblr
### Dictionary structure
```
search(text='', limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>url</td>
	<td>Url of the post</td>
</tr>
<tr>
	<td>slug</td>
	<td>Title of the post</td>
</tr>
<tr>
	<td>date</td>
	<td>Date of the post</td>
</tr>
<tr>
	<td>tags</td>
	<td>Tags for the post</td>
</tr>
<tr>
	<td>note</td>
	<td>Number of note for the post</td>
</tr>
</tbody>
</table>

## <a id="venmo"></a>Venmo
### Dictionary structure
```
search()
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>message</td>
	<td>Message of the post</td>
</tr>
<tr>
	<td>url</td>
	<td>Link of the post</td>
</tr>
</tbody>
</table>

## <a id="vine"></a>Vine
### Dictionary structure
```
get_popular()
```  
```
search(text='')
```   
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>description</td>
	<td>Description of the post</td>
</tr>
<tr>
	<td>url</td>
	<td>Link of the post</td>
</tr>
</tbody>
</table>

## <a id="wikipedia"></a>Wikipedia
### Dictionary structure
```
get_link_sphere(text='', limit=10)
```  
```
get_links(text='',limit=10)
```  
```
search_prefix(text='', limit=10)
```  
```
search_text(text='',limit=10)
```  
```
search_geo(radius=1000,lat=48.858844,long=2.294351,limit=10)
```  
```
get_latest_protected(limit=10)
```  
```
get_latest_changes(limit=10)
```  
<table>
<thead>
<tr>
	<th>Key</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> - </td>
	<td>Data asked for</td>
</tr>
</tbody>
</table>