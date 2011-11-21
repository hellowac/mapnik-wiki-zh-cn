<!-- Name: OsmPlugin -->
<!-- Version: 27 -->
<!-- Last-Modified: 2010/11/13 10:24:18 -->
<!-- Author: kunitoki -->
[[TOC]]

Mapnik's PluginArchitecture supports the use of different input formats.

This plugin allows for the direct reading of data from the [OpenStreetMap XML format](http://wiki.openstreetmap.org/wiki/.osm). You can use it in two different ways; you can either render a local file, or connect to a URL which provides OSM XML data within a given bounding box.

*NOTE*: the primary way that Mapnik is used to render OpenStreetMap data is to import an [extract](http://wiki.openstreetmap.org/wiki/Planet.osm) into Postgres using the [osm2pgsql](http://wiki.openstreetmap.org/wiki/Osm2pgsql) tool and then read it using the wiki:PostGIS plugin.


# Dependencies

You need libxml2 installed on your system for parsing the XML, and libcurl (http://curl.haxx.se) for making connections across the network (this is needed so that the OSM plugin can connect to remote servers to fetch OSM data).


# Parameters

|| *parameter* || *value*  || *description* || *default* ||
|| file            || string       || the OSM file to load || ||
|| url             || string       || the URL of an OSM data source (see below). || ||
|| bbox            || string       || the bounding box to load from the URL of an OSM data source (see below). || ||
|| parser          || string       || the XML parser: currently, this must have a value of "libxml2" as libxml2 is the only parser currently supported || libxml2 ||
|| filter_factor   || double       || filter to use when querying for raster data || 0.0 ||


# Usage

## How to specify an OSM layer in your Mapnik XML file

Your layer's Datasource must have a "type" parameter with a value of "osm", in a similar way that the shapefile plugin needs a "type" parameter of "shape".
For example:


    #!xml
    <Layer name="roads" status="on" srs="+proj=latlong +datum=WGS84">
        <StyleName>residential</StyleName>
        <StyleName>unclassified</StyleName>
        <StyleName>secondary</StyleName>
        <StyleName>primary</StyleName>
        <StyleName>motorway</StyleName>
        <Datasource>
          <Parameter name="type">osm</Parameter>
          <Parameter name="file">test2.osm</Parameter>
        </Datasource>
    </Layer>

## Specifying the data's source

OSM data may be sourced from two different places: a file (as in the example above) or the web. As the example above illustrates, you can specify a source OSM file by specifying a Parameter with a name of "file". 

For a web data source, we must provide two parameters: the base URL and the bounding box in WGS84 latitude/longitude. These two parameters are named "url" and "bbox". The full URL of the OSM data server will be constructed from the base URL with the bounding box added as a query string. Here is an example:


    #!xml
    <Layer name="roads" status="on" srs="+proj=latlong +datum=WGS84">
        <StyleName>residential</StyleName>
        <StyleName>unclassified</StyleName>
        <StyleName>secondary</StyleName>
        <StyleName>primary</StyleName>
        <StyleName>motorway</StyleName>
        <Datasource>
          <Parameter name="type">osm</Parameter>
          <Parameter name="url">http://www.osmdataserver.com/data.php</Parameter>
          <Parameter name="bbox">-0.8,51,-0.7,51.1<Parameter>
        </Datasource>
    </Layer>

In the above example, the full URL of the OSM data server would be `http://www.osmdataserver.com/data.php?bbox=-0.8,51,-0.7,51.1`. Data will be downloaded from this URL and rendered according to the rules in the style file.

## Styling the output

Styling the output is done in the same way as for other data sources, with tests for different tags done in the `<Filter>` tag. For example this rule will match OSM ways where the 'highway' tag is equal to 'path' and the 'foot' tag is equal to 'designated':


    #!xml
    <Rule>
        <Filter>[highway] = 'path' and [foot] = 'designated'</Filter>
        <LineSymbolizer>
            <CssParameter name="stroke">#fff</CssParameter>
            <CssParameter name="stroke-width">6</CssParameter>
            <CssParameter name="stroke-linejoin">round</CssParameter>
            <CssParameter name="stroke-linecap">round</CssParameter>
            <CssParameter name="stroke-opacity">0.4</CssParameter>
        </LineSymbolizer>
        <LineSymbolizer>
            <CssParameter name="stroke">red</CssParameter>
            <CssParameter name="stroke-width">2.0</CssParameter>
            <CssParameter name="stroke-dasharray">1,4</CssParameter>
            <CssParameter name="stroke-linejoin">round</CssParameter>
            <CssParameter name="stroke-linecap">round</CssParameter>
        </LineSymbolizer>
    </Rule>


## Lines or polygons?

Polygon support is not yet very sophisticated. A few pre-defined tag/value combinations are assumed to be polygons; all others are assumed to be linear ways.
Currently these tag/values are assumed to be polygons:

- natural=wood[[BR]]
- natural=water[[BR]]
- natural=heath[[BR]]
- natural=marsh[[BR]]
- military=danger_area[[BR]]
- landuse=forest[[BR]]
- landuse=industrial.[[BR]]

These are defined in the polygon_types class in the source file osm.h, so if you want to add others for your own use, that's the place to go.

## Demo programs

There are two demo programs available in the source distribution, "render" and "easymapnik".

### render

The first, render.cpp, is a very simple application which will render a given OSM file according to the rules in a given Mapnik XML file. The usage is:

`render MapnikXML w s e n [OSMfile]`

w, s, e and n represent the bounding box to zoom to. By default you specify the source OSM file in the Mapnik XML file; however, you may also supply it as an optional sixth parameter.

### easymapnik

easymapnik is the beginnings of a project to develop an application to allow easy rendering of OSM data from file or from an OSM data server, without the need to install a PostGIS database, or, ultimately, to write a Mapnik rules file. At the moment it's very much a demo app, rather than a production-ready app, but nonetheless it demonstrates how you can render OSM data from an OSM data source or server. It's available in the "demo" directory and has a Makefile which has so far only been tested on OS X 10.5 with a version of Mapnik dating from early 2009. The usage is:

`easymapnik -s source [-w width] [-h height] -x xmlfile [-i InOSMFile] [-o OutPNGFile] [-t] [-z startzoom] [-Z endzoom] [-b bbox] [-u serverURL] [-m]`

To go through each option one at a time:

    -s : specify the source, this maybe either 'osm' or 'api'. The former reads from an OSM file; the latter, from a server.
    -h : height of output image.
    -x : Mapnik XML file; you must currently write this by hand! However it need not specify an OSM file or URL.
    -i : input OSM file; only applies with '-s osm'.
    -o : output PNG file.
    -t : use tiled output mode, which generates Google-style x,y,z tiles. You must specify the -z and -Z
    options for this.
    -z : start zoom for tiled output (see above)
    -Z : end zoom for tiled output (see above)
    -b : bounding box for OSM data URL; only applies with '-s api'.
    -u : server URL; only applies with '-s api'.
    -m : multirequest mode; if you're requesting a relatively large area from the server, the data will
    be fetched in 0.1x0.1 degree tiles.