Since Mapnik 2.3 the PostGIS pluging can be used asynchrnonously to reduce the overall map rendering time. 

## How it works
Mapnik uses the painter's algorithm to render maps. It means that layers are drawn sequentially. The inner algorithmer is :
    For each layer
       Query the features from the layer
       For each feature in this layer
           Draw the layer

In this case, the renderer spends a lot of time waiting for PostGis to perform the query that will feed with features.

The asynchronous_request parameter in PostGIS pulgin aims to parallelize querries on the remote server and rendering : while a layer is rendering, queries are sent ahead.


## When to use it
Must have :
* You have already applyed all the [rendering optimizations with PoistGIS](/wiki:OptimizeRenderingWithPostGIS/)
* you have a lot of PostGIS layers

Nice to have :
* rendering time for layers are quite homogeneous
* your PostGIS database is on another server

## When not to use it
* you use cache-features=false ; if you want to reduce map rendering time, you should not send the same data base query twice if you have enough RAM to store the query restults
* you have less thant 3 PostGIS layers
* you have very heterogenous layers : for example, a huge road layers that takes 8 times longer to render than the other layers

## How to use it
### Usage from XML 
Set a value to *max_async_connection* and *asynchronous_request* to *true* in your existing PostGIS datasources :
<Layer name="countries" status="on" srs="+proj=latlong +datum=WGS84">
      <StyleName>countries_style_label</StyleName>
      <Datasource>
        <Parameter name="type">postgis</Parameter>
        <Parameter name="host">dbhost</Parameter>
        <Parameter name="dbname">admin</Parameter>
        <Parameter name="user">postgres</Parameter>      
        <Parameter name="password"></Parameter>
        <Parameter name="table">world_worldborders</Parameter>
        <Parameter name="asynchronous_request">true</Parameter>
        <Parameter name="max_async_connection">3</Parameter>
      </Datasource>
  </Layer>
