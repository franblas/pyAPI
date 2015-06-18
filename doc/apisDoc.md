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
	<td>9 Gag</td>
	<td>Social</td>
	<td>No</td>
</tr>
<tr>
	<td>Crunchbase</td>
	<td>Data</td>
	<td>Yes</td>
</tr>
<tr>
	<td>Dailymotion</td>
	<td>Video</td>
	<td>No</td>
</tr>
<tr>
	<td>Delicious</td>
	<td>Social</td>
	<td>No</td>
</tr>
<tr>
	<td>Docker</td>
	<td>Code</td>
	<td>No</td>
</tr>
<tr>
	<td>Ebay</td>
	<td>Shopping</td>
	<td>Yes</td>
</tr>
<tr>
	<td>Eventbrite</td>
	<td>Event</td>
	<td>Yes</td>
</tr>
<tr>
	<td>Eventful</td>
	<td>Event</td>
	<td>Yes</td>
</tr>
<tr>
	<td>Flickr</td>
	<td>Picture</td>
	<td>Yes</td>
</tr>
<tr>
	<td>Freebase</td>
	<td>Data</td>
	<td>Yes</td>
</tr>
<tr>
	<td>GoogleBooks</td>
	<td>Book</td>
	<td>No</td>
</tr>
<tr>
	<td>GoogleTrends</td>
	<td>Data</td>
	<td>No</td>
</tr>
<tr>
	<td>Imdb</td>
	<td>Movie</td>
	<td>No</td>
</tr>
<tr>
	<td>Instagram</td>
	<td>Picture</td>
	<td>Yes</td>
</tr>
<tr>
	<td>Osm</td>
	<td>Map</td>
	<td>No</td>
</tr>
<tr>
	<td>Panoramio</td>
	<td>Picture</td>
	<td>No</td>
</tr>
<tr>
	<td>Pinterest</td>
	<td>Social</td>
	<td>No</td>
</tr>
<tr>
	<td>Reddit</td>
	<td>Social</td>
	<td>No</td>
</tr>
<tr>
	<td>RubyGems</td>
	<td>Code</td>
	<td>No</td>
</tr>
<tr>
	<td>SoundCloud</td>
	<td>Music</td>
	<td>Yes</td>
</tr>
<tr>
	<td>Spotify</td>
	<td>Music</td>
	<td>Yes</td>
</tr>
<tr>
	<td>Ted</td>
	<td>Event</td>
	<td>Yes</td>
</tr>
<tr>
	<td>The Movie Database</td>
	<td>Movie</td>
	<td>Yes</td>
</tr>
<tr>
	<td>Tumblr</td>
	<td>Social</td>
	<td>No</td>
</tr>
<tr>
	<td>Venmo</td>
	<td>Payement</td>
	<td>No</td>
</tr>
<tr>
	<td>Vine</td>
	<td>Video</td>
	<td>No</td>
</tr>
<tr>
	<td>Wikipedia</td>
	<td>Data</td>
	<td>No</td>
</tr>
</tbody>
</table>

## <a id="500px"></a>500 px
### Dataframe
```
getPopular <- function(.,nblimit=10)       
```  
```
getBestReated <- function(.,nblimit=10)       
```  
```
getToday <- function(.,nblimit=10)       
```  
```
searchPictures <- function(.,search="",nblimit=10)       
```
<table>
<thead>
<tr>
	<th>Column</th>
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

### Dataframe 2
```
getStories <- function(.,nblimit=10)       
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Name of the picture</td>
</tr>
<tr>
	<td>usercountry</td>
	<td>Original country of the user</td>
</tr>
<tr>
	<td>username</td>
	<td>Full name of the user</td>
</tr>
</tbody>
</table>

## 9 Gag
### Dataframe
```
getTrend <- function(.)
```  
```
getHot <- function(.)
```
<table>
<thead>
<tr>
	<th>Column</th>
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

## Crunchbase
## Dataframe
```
newOrganisations <- function(.)
```  
```
updatedOrganizations <- function(.)
```  
```
searchOrganization <- function(.,text="")
```  
```
newPeople <- function(.)
```  
```
newProducts <- function(.)
```  
<table>
<thead>
<tr>
	<th>Column</th>
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

## Dailymotion
### Dataframe
```
searchVideos <- function(., text="",limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Name of the video</td>
</tr>
<tr>
	<td>views_total</td>
	<td>Total views for the video</td>
</tr>
<tr>
	<td>bookmarks_total</td>
	<td>Total number of bookmarks for the video</td>
</tr>
<tr>
	<td>comments_total</td>
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
### Dataframe 2
```
searchPlaylists <- function(., text="",limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>name</td>
	<td>Name of the playlist</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the playlist</td>
</tr>
<tr>
	<td>videos_total</td>
	<td>Total number of videos into the playlist</td>
</tr>
</tbody>
</table>
### Dataframe 3
```
searchGroups <- function(., text="",limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>name</td>
	<td>Name of the group</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the group</td>
</tr>
</tbody>
</table>
## Delicious
### Dataframe
```
search <- function(., text="", limit=10)
```  
```
getRecent <- function(., limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
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
## Docker
### Dataframe
```
search <- function(., text="", limit=100)
```  
<table>
<thead>
<tr>
	<th>Column</th>
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

## Ebay
### Dataframe
```
search <- function(., text="", limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>itemId</td>
	<td>Id of the item</td>
</tr>
<tr>
	<td>title</td>
	<td>Name of the announce</td>
</tr>
<tr>
	<td>primaryCategory</td>
	<td>Category of the item</td>
</tr>
<tr>
	<td>viewItemURL</td>
	<td>Url of the announce</td>
</tr>
<tr>
	<td>location</td>
	<td>Location of the announce</td>
</tr>
<tr>
	<td>sellingStatus</td>
	<td>Price of the item</td>
</tr>
</tbody>
</table>
### Dataframe 2
```
getMostWatched <- function(., limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>itemRecommendations.item.itemId</td>
	<td>Id of the item</td>
</tr>
<tr>
	<td>itemRecommendations.item.title</td>
	<td>Name of the announce</td>
</tr>
<tr>
	<td>itemRecommendations.item.primaryCategoryName</td>
	<td>Category of the item</td>
</tr>
<tr>
	<td>itemRecommendations.item.viewItemURL</td>
	<td>Url of the announce</td>
</tr>
<tr>
	<td>itemRecommendations.item.country</td>
	<td>Original country of the announce</td>
</tr>
<tr>
	<td>itemRecommendations.item.buyItNowPrice</td>
	<td>Price of the item</td>
</tr>
<tr>
	<td>itemRecommendations.item.originalPrice</td>
	<td>riginal price of the item</td>
</tr>
</tbody>
</table>
### Dataframe 3
```
getSimilar <- function(., id="121187584160", limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>itemRecommendations.item.title</td>
	<td>Name of the announce</td>
</tr>
<tr>
	<td>itemRecommendations.item.primaryCategoryName</td>
	<td>Category of the item</td>
</tr>
<tr>
	<td>itemRecommendations.item.viewItemURL</td>
	<td>Url of the announce</td>
</tr>
<tr>
	<td>itemRecommendations.item.country</td>
	<td>Original country of the announce</td>
</tr>
<tr>
	<td>itemRecommendations.item.buyItNowPrice</td>
	<td>Price of the item</td>
</tr>
</tbody>
</table>
### Dataframe 4
```
getTopSelling <- function(., limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>productRecommendations.product</td>
	<td>Id of the product</td>
</tr>
<tr>
	<td>productRecommendations.product.title</td>
	<td>Title of the announce</td>
</tr>
<tr>
	<td>productRecommendations.product.reviewCount</td>
	<td>Number of view</td>
</tr>
<tr>
	<td>productRecommendations.product.productURL</td>
	<td>Url of the product</td>
</tr>
</tbody>
</table>
### Dataframe 5
```
getPopularSearch <- function(., text="", limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>AlternativeSearches</td>
	<td>Alternatives search for a given keyword</td>
</tr>
<tr>
	<td>RelatedSearches</td>
	<td>Related search for a given keyword</td>
</tr>
</tbody>
</table>
## Eventbrite
### Dataframe
```
searchEvents <- function(., text="")
```  
```
getPopularEvents <- function(.)
```  
```
getEventsCity <- function(., text="")
```  
<table>
<thead>
<tr>
	<th>Column</th>
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
	<td>num_past_events</td>
	<td>Number of past events for the given group</td>
</tr>
<tr>
	<td>num_future_events</td>
	<td>Number of future events for the given group</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the event</td>
</tr>
</tbody>
</table>
## Google Books
### Dataframe
```
searchByAuthor <- function(., author="", limit=10)
```  
```
searchBook <- function(., text="", limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
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
</tbody>
</table>
## Google Trends
### Countries available
South Africa,Germany,Saudi Arabia,Argentina,Australia,Austria,Belgium,Brazil,Canada,Chilia,Colombia,South Corea,Denemark,Egypt,Spain,USA,Finland,France,Greece,Hong Kong,Hongria,India,Indonesia,Israel,Italia,Japan,Kenya,Malaisia,Mexico,Nigeria,Norway,Holland,Philippines,Poland,Portugal,Czech Republic,Roumania,UK,Russia,Singapour,Sweden,Switzerland,Taiwan,Thailand,Turkey,Ukraine,Vietnam   
### Dataframe
```
getTrends <- function(.,name="USA")
```  
<table>
<thead>
<tr>
	<th>Column</th>
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
## Imdb 
### Dataframe
```
searchOmdb <- function(., text="")
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> Title </td>
	<td>Title of the media</td>
</tr>
<tr>
	<td> Year </td>
	<td>Year of release</td>
</tr>
<tr>
	<td> Type </td>
	<td>Type of media</td>
</tr>
</tbody>
</table>
### Dataframe 2
```
searchTitle <- function(., text="")
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> title </td>
	<td>Title of the media</td>
</tr>
<tr>
	<td> description </td>
	<td>Description of the media</td>
</tr>
</tbody>
</table>
### Dataframe 3
```
searchName <- function(., text="")
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> - </td>
	<td>Names of actor</td>
</tr>
</tbody>
</table>

## Instagram
### Dataframe
```
getPopular <- function(., limit=10)
```
```
searchByCoordinates <- function(.,lat=48.858844,lon=2.294351,limit=10)
```
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> link </td>
	<td>Lnk of the content</td>
</tr>
<tr>
	<td> filter </td>
	<td>Filter used for the picture</td>
</tr>
<tr>
	<td> users_in_photo </td>
	<td>Users tagged in the picture</td>
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
	<td> loc_name </td>
	<td>Place's name of the content</td>
</tr>
<tr>
	<td> count_com </td>
	<td>Number of commentaries</td>
</tr>
<tr>
	<td> data_com </td>
	<td>Text of the commentaries</td>
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
### Dataframe 2
```
getTags <- function(.,text="")
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> media_count </td>
	<td>Tag's popularity</td>
</tr>
<tr>
	<td> name </td>
	<td>Tag's name</td>
</tr>
</tbody>
</table>
### Dataframe 3
```
searchLocations <- function(.,lat=48.858844,lon=2.294351,limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
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
### Dataframe 4
```
searchUsers <- function(.,text="",limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> username </td>
	<td>User's name</td>
</tr>
<tr>
	<td> full_name </td>
	<td>Full user's name</td>
</tr>
<tr>
	<td> id </td>
	<td>User's id</td>
</tr>
<tr>
	<td> profile_picture </td>
	<td>User's profile picture</td>
</tr>
</tbody>
</table>

## OSM 
### Dataframe
```
searchLatestNotes <- function(., text="", limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> V1 </td>
	<td>Latitude of the place</td>
</tr>
<tr>
	<td> V2 </td>
	<td>Longitude of the place</td>
</tr>
<tr>
	<td> V3 </td>
	<td>Description of the place</td>
</tr>
</tbody>
</table>
### Dataframe 2
```
search <- function(., text="", limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> lat </td>
	<td>Latitude of the place</td>
</tr>
<tr>
	<td> lon </td>
	<td>Longitude of the place</td>
</tr>
<tr>
	<td> display_name </td>
	<td>Names of the place</td>
</tr>
<tr>
	<td> importance </td>
	<td>Relevance of the place, regarding the research</td>
</tr>
</tbody>
</table>
### Dataframe 3
```
getCoordinatesCity <- function(., text="")
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td> lat </td>
	<td>Latitude of the place</td>
</tr>
<tr>
	<td> lon </td>
	<td>Longitude of the place</td>
</tr>
</tbody>
</table>
## Panoramio
### Dataframe
```
getPopularWorldPhotos <- function(., limit=10)
```  
```
getPhotosArea <- function(., latitude=0, longitude=0, range=5, limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
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
	<td>owner_name</td>
	<td>Owner of the picture</td>
</tr>
<tr>
	<td>photo_file_url</td>
	<td>Url of the picture</td>
</tr>
<tr>
	<td>photo_title</td>
	<td>Title of the picture</td>
</tr>
<tr>
	<td>upload_date</td>
	<td>Date of the picture</td>
</tr>
</tbody>
</table>
## Reddit
### Dataframe
```
searchArticle <- function(., text="", limit=10)
```  
```
getHotTopics <- function(.,limit=10)
```  
```
getControversialTopics <- function(.,limit=10)
```  
```
getRandomTopics <- function(.)
```
<table>
<thead>
<tr>
	<th>Column</th>
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
	<td>selftext</td>
	<td>Text of the article</td>
</tr>
</tbody>
</table>
### Dataframe 2
```
getPopularSubreddits <- function(.,limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>display_name</td>
	<td>Name of the subreddit</td>
</tr>
<tr>
	<td>subscribers</td>
	<td>Number of users for the subreddit</td>
</tr>
</tbody>
</table>
### Dataframe 3
```
getPopularSubreddits <- function(.,limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>display_name</td>
	<td>Name of the subreddit</td>
</tr>
<tr>
	<td>subscribers</td>
	<td>Number of users for the subreddit</td>
</tr>
<tr>
	<td>title</td>
	<td>Description of the subreddit</td>
</tr>
</tbody>
</table>
## RubyGems
### Dataframe
```
search <- function(., text="")
```  
```
latestAdded <- function(.)
```  
```
latestUpdated <- function(.)
```  
<table>
<thead>
<tr>
	<th>Column</th>
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
	<td>homepage_uri</td>
	<td>Url of the projects gem</td>
</tr>
</tbody>
</table>
### Dataframe 2
```
totalDownloadGems <- function(.)
```   
<table>
<thead>
<tr>
	<th>Column</th>
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
## Soundcloud
### Dataframe
```
searchTracks <- function(., text="", limit=10)
```  
```
getInfosTrack <- function(., id="182242225")
```  
```
getLatestTracks <- function(., limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>title</td>
	<td>Title of the track</td>
</tr>
<tr>
	<td>download_count</td>
	<td>Number of downloads</td>
</tr>
<tr>
	<td>favoritings_count</td>
	<td>Number of favorites</td>
</tr>
<tr>
	<td>comment_count</td>
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
	<td>tag_list</td>
	<td>Tags for the track</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the track</td>
</tr>
<tr>
	<td>permalink_url</td>
	<td>Url of the track</td>
</tr>
</tbody>
</table>
### Dataframe 2
```
searchUsers <- function(., text="", limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
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
	<td>full_name</td>
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
	<td>track_count</td>
	<td>Number of tracks</td>
</tr>
<tr>
	<td>followers_count</td>
	<td>Number of followers</td>
</tr>
</tbody>
</table>
### Dataframe 3
```
searchGroups <- function(., text="", limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>name</td>
	<td>Name of the group</td>
</tr>
<tr>
	<td>track_count</td>
	<td>Number of groups tracks</td>
</tr>
<tr>
	<td>members_count</td>
	<td>Number of groups members</td>
</tr>
<tr>
	<td>contributors_count</td>
	<td>Number of groups contributors</td>
</tr>
<tr>
	<td>permalink_url</td>
	<td>Url of the group</td>
</tr>
<tr>
	<td>description</td>
	<td>Description of the group</td>
</tr>
</tbody>
</table>
### Dataframe 4
```
getLatestComments <- function(., limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>track_id</td>
	<td>Id of the track</td>
</tr>
<tr>
	<td>body</td>
	<td>Latest comment for the track</td>
</tr>
</tbody>
</table>
## Tumblr
### Dataframe
```
searchByTag <- function(., text="", limit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>post_url</td>
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
	<td>note_count</td>
	<td>Number of note for the post</td>
</tr>
<tr>
	<td>source_url</td>
	<td>Url of the source</td>
</tr>
</tbody>
</table>

## Venmo
### Dataframe
```
getPublic <- function(.)
```  
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>message</td>
	<td>Message of the post</td>
</tr>
<tr>
	<td>link</td>
	<td>Link of the post</td>
</tr>
</tbody>
</table>
## Vine
### Dataframe
```
getPopular <- function(.)
```  
```
searchByTag <- function(., tag="")
```   
<table>
<thead>
<tr>
	<th>Column</th>
	<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
	<td>description</td>
	<td>Description of the post</td>
</tr>
<tr>
	<td>link</td>
	<td>Link of the post</td>
</tr>
</tbody>
</table>
## Wikipedia
### Dataframe
```
getLinkSphere <- function(., search="", nblimit=10)
```  
```
getLinks <- function(., search="", nblimit=10)
```  
```
searchByPrefix <- function(., search="", nblimit=10)
```  
```
searchText <- function(.,search="",nblimit=10)
```  
```
searchGeo <- function(.,radius=1000,lat=0,long=0,nblimit=10)
```  
```
latestProtected <- function(.,nblimit=10)
```  
```
latestChanges <- function(.,nblimit=10)
```  
<table>
<thead>
<tr>
	<th>Column</th>
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