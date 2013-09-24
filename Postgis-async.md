The PostGIS pluging can be used asynchrnonously since Mapnik 2.3 which can reduce map rendering time if you have several PostGIS layers.

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
* you have very heterogenous layers : for example, a huge road layers that takes  times longer to render than the other layers

## How to use it

