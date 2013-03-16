Check database.txt to find the generated test database    
Sample query 
1)To list the url and geolocation facility of a website which support media_queries but not camera
 query would be
 url,geolocation:media_queries-true,camera-false 
2)To find the features supported by a url
features:url-www.abc.com [,features-true]
General query format  
<requirement1,requirement2,..>:<constraint1,constraint2,...>
