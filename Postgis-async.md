Since Mapnik 2.3 the PostGIS pluging can be used asynchrnonously to reduce the overall map rendering time. 

## How it works
Mapnik uses the painter's algorithm to render maps. It means that layers are drawn sequentially. The inner algorithmer is :
    For each layer
       Query the features from the layer
       For each feature in this layer
           Draw the layer

In this case, the renderer spends a lot of time waiting for PostGis to perform the query that will feed with features.

The asynchronous_request parameter in PostGIS pulgin aims to parallelize queries on the remote server and rendering : while a layer is rendering, queries are sent ahead.


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
        <Parameter name="max_async_connection">4</Parameter>
      </Datasource>
  </Layer>
### How to set max_async_connection
*max_async_connection* sets the size of the number of databases connections that can run in parallel for the rendering of one map. Concretely, it means how many layers to load features ahead.
Let's consider an example, with the number of layers geographical features for 7 layers :
1. countries   500
1. urban areas 550
1. parcs   620
1. commercial areas 580
1. lakes   570
1. roads   2500
1. cities  300
Let's we assume database query time and drawing time are equal and proportionnal to the number of features in the layer.
The largest layer is *roads* ; it is 4 time larger thant the others. Hence we should launch the query to get the features for roads before the drawing of layer *urban areas*, so that the query is finished when the drawing of roads is about to start.
