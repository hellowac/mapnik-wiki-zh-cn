# Mapnik Layer

## datasource

## envelope

envelope( (Layer)arg1) -> Box2d :
    Return the geographic envelope/bounding box.
    Determined based on the layer datasource.

Usage:

    >>> from mapnik import Layer
    >>> lyr = Layer('My Layer','+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
    >>> lyr.envelope()
    box2d(-1.0,-1.0,0.0,0.0) # default until a datasource is loaded
    

C++ signature :

    mapnik::box2d<double> envelope(mapnik::layer {lvalue})

## maxzoom

Float

## minzoom

Float

## name

String

## queryable

Boolean

## srs

String representing the spatial reference system of the map.

## styles

a list of strings holding the names of styles

## title

String

## visible

visible( (Layer)arg1, (float)arg2) -> bool :
    Return True if this layer's data is active and visible at a given scale.

    Otherwise returns False.
    Accepts a scale value as an integer or float input.
    Will return False if:
     scale >= minzoom - 1e-6
     or:
     scale < maxzoom + 1e-6
    
Usage:

    >>> from mapnik import Layer
    >>> lyr = Layer('My Layer','+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')
    >>> lyr.visible(1.0/1000000)
    True
    >>> lyr.active = False
    >>> lyr.visible(1.0/1000000)
    False
    

    C++ signature :
        bool visible(mapnik::layer {lvalue},double)
