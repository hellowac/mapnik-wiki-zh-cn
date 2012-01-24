<!-- Name: StyleShare -->
<!-- Version: 15 -->
<!-- Last-Modified: 2011/05/16 07:42:34 -->
<!-- Author: Harry Wood -->

# Sharing Map Styles

We need a proper app to share styles (Dane has started django code but its not ready yet)

The idea behind this app is that all styles uploaded will have a sample rendered live, therefore:
  * All styles must have relative paths or urls to resources
  * Must either work with OSM data or work against uploaded sample WKT or GeoJSON
  * Will be able to be downloaded as MML if that is their native format or exported as XML
  * Will also be able to be serialized as python pickles (in the future)

For now, list your styles here!

## Name of Style(s)

*Description*: A unique descriptive for your style or set of styles.

*Type*: Cascadenik MML, Mapnik XML, or Python code 

*URI*: If you host them somewhere (like github) then paste the url
  * otherwise, paste inline...

*Minimum Mapnik Version*: What Mapnik version do these style depend on?


## OSM

*Description*: The default style sheet used by openstreetmap.org

*Type*: Mapnik XML

*URI*: http://trac.openstreetmap.org/browser/applications/rendering/mapnik

*Minimum Mapnik Version*: Mapnik 0.7.1 (recommended)



## OSM NL Styles


*Description*: Various styles powering http://www.openstreetmap.nl/

*Type*: Mapnik XML

*URI*: http://git.openstreet.nl/index.cgi/stylesheets.git/

*Minimum Mapnik Version*: Mapnik 0.7.1 [see q](http://help.openstreetmap.org/questions/1746/running-generate_image-gives-features-only-present-in-mapnik-version-071-error)

## Mapquest

*Description*: OSM style featured on open.mapquest.com .   MIT licensed

*URI*: https://github.com/MapQuest/MapQuest-Mapnik-Style

*Minimum Mapnik Version* : 0.8.0  (see readme for other dependencies)

## Haiti OSM WMS overlay

*Description*: TODO

*Type*: Mapnik XML

*URI*: HaitiStyles

*Minimum Mapnik Version*: Mapnik 0.7.0

## Hike & Bike

*Description*: A style for hiking and biking, with hiking symbols

*Type*: Cascadenik MML

*URI*: http://mapnik-utils.googlecode.com/svn/sandbox/cascadenik/hike_n_bike/ (style.mml)

*Minimum Mapnik Version*: 0.7.0 

## By Night

*Description*: An overlay for showing lit (or non-lit) ways, buildings and areas

*Type*: Cascadenik MML

*URI*: http://mapnik-utils.googlecode.com/svn/sandbox/cascadenik/hike_n_bike/ (lighting.mml)

*Minimum Mapnik Version*: 0.6.0

## MapBox

*Description*: see http://tiles.mapbox.com/

*Type*: [[Carto]]

*URI*: http://github.com/mapbox/

*Minimum Mapnik Version*: 2.0.0

## Cascadenik Dev OSM Styles, aka "Remapniking OSM"

*Description*: demo at: http://teczno.com/cascadenik-openstreetmap-II/

*Type*: Cascadenik MML

*URI*: http://mapnik-utils.googlecode.com/svn/trunk/serverside/cascadenik/openstreetmap/

*Minimum Mapnik Version*: 0.6.1

## Tango

*Description*: tango base style file, demo at: http://osm.tcweb.org/

*Type*: Mapnik XML

*URI*: http://github.com/tclavier/mapnik

*Minimum Mapnik Version*: Mapnik 0.7.1

## WikiMedia Toolserver

*Description*: variety of styles used at http://toolserver.org/~osm/styles/

*Type*: Mapnik XML

*URI*: http://svn.toolserver.org/svnroot/p_osm/styles/

*Minimum Mapnik Version*: Mapnik 0.7.1


