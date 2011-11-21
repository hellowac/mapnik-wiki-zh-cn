<!-- Name: XMLConfigReference -->
<!-- Version: 44 -->
<!-- Last-Modified: 2011/08/30 14:59:29 -->
<!-- Author: springmeyer -->
[[TOC]]

# Mapnik configuration XML

See also a reference PDF, created by David Eastcott: http://media.mapnik.org/docs/MapnikXMLDescription.pdf

To validate the XML see ValidatingXml

## General

Comments can be placed in the configuration file using the default xml <!-- --> syntax

## Map
The Map object defines the master object of a mapnik configuration XML. It defines map wide parameters and serves as the envelope for Style and Layer definitions.

 * Element: *Map*
 * Element type: Root element

 * Attributes:
  * *bgcolor*: HTML color code for the background-color of the map (for instance #000000)
    * renamed to 'background-color' in Mapnik2.
  * *background-image*: Available in Mapnik2: use an image for the background instead of a color fill.
  * *font_directory*: Available in Mapnik2: pass a directory that contains fonts, which will automatically be registered if they end in ttf, otf, ttc, pfa, pfb, ttc, or dfont.
  * *srs*: Coordinate system in which the map is rendered (for instance '+proj=latlong+datum=WGS84' for a WGS84 Geographic coordinate system)
  * *buffer_size*: Default 0; Good value is usually tile size/2 to help avoid cut labels. This influences envelope used by placement detector ( i.e. 'avoid_edges' parameter)
  * *paths_from_xml*: Check if relative paths should be interpreted as relative to/from XML location (default is true)
  * *minimum_version*: Declare the minimum version of mapnik to be used with the stylesheet. Example: minimum_version="0.6.1". Will print a notice if you use an older mapnik version. (Since r1453)

 * Children:
  * *[#Style Style]*
  * *[#Layer Layer]*
  * *FileSource*: See http://trac.mapnik.org/changeset/574
  * *Datasource*: See [#Datasource Datasource] and http://trac.mapnik.org/changeset/574
  * *FontSet*: Defines a fontset for fallback fonts (if a character isn't found in the first font, proceed through the list until it is found)
  * *Include*: The container tag used to wrap all context in files included via XInclude

  * *xmlcomment*: (Ignored by Mapnik)
  * *xmlattr*: (Ignored by Mapnik)
----

## Style
A Style object  defines the way objects can be rendered. A Mapnik configuration file can have an unlimited number of Style objects. Style objects are referenced by Layer objects in order to actually be rendered.

 * Element: *Style*
 * Element type: Collection of Rules
 * Attributes
  * *name*: Name for this Style object. Needs to be unique per configuration file. A Style is referenced by a Layer through the corresponding StyleName parameter. If a name is ommited, what will happen?

 * Children:
  * *[#Rule Rule]*

  * *xmlcomment*: (Ignored by Mapnik)
  * *xmlattr*: (Ignored by Mapnik)
----

## Layer
 * Element: *Layer*
 * Element type: References a Style (StyleName) and a DataSource

 * Attributes:
  * *name*: The Name of the layer
  * *status*: Default "on"; *on* or *off*, "0" or "1"
  * *clear_label_cache*: Default "off". Setting this to "on" clears the internal placement detector list, causing the items of this layer, and from this layer on, to be rendered without taking previous rendered items into account ('clear collision avoidance list')
  * *cache-features*: Default "off". Setting this to "on" triggers mapnik to attempt to cache features in memory for rendering when (and only when) a layer has multiple styles attached to it. (only available in >mapnik 2 since r2636).
  * *srs*: Default inherits from map.srs; Reference system from the the project [[Proj.4](http://trac.osgeo.org/proj/)]. e.g. +proj=latlong +datum=WGS84
  * *abstract*: Default ""
  * *title*: Default ""
  * *minzoom*: Default 0.0
  * *maxzoom*: Default 1.797693134862316e+308
  * *queryable*: Default "false"

 * Children:
  * *StyleName*: The name of a defined [#Style style]. The style must contain the same string in the attribute *name*.
  * *[#Datasource Datasource]*
----

## Datasource
 See also the [0.6.0 Python API docs](http://svn.mapnik.org/tags/release-0.6.0/docs/api_docs/python/mapnik-module.html#Datasource)

 * Element: *Datasource*
 * Element type: References the map data source and parameters.

 * Attributes:
  * *name*: Create a datasource template [#574](http://trac.mapnik.org/changeset/574)
  * *base*: Inherit from a datasource template [#574](http://trac.mapnik.org/changeset/574)
 * Generic Parameters:
  * type: Specifies the format of the data source
   * Possible values:
     * '''shape'''	:	ESRI shapefile
     * '''postgis'''	:	Postgis table or query
     * '''raster'''	:	Tiled or stripped TIFF
     * '''gdal'''	:	GDAL supported raster dataset (not build by default)
     * '''ogr'''          :       OGR supported vector datasource (not build by default)
     * '''osm'''		:	Open Street Map (not build by default)
  * *estimate_extent*: boolean to tell Mapnik to estimate the extent of the layer (true) or not (false)
  * *extent*:		manually enter an extent if estimate_extent is set to false

 * Additional parameters for type *postgis*    
   * *cursor_size* (default _0_):
   * *dbname*: Database name.
   * *extent_from_subquery* (default _false_):
   * *geometry_field*: Use the geometry_field parameter to specify which field to use if you have >1 geometry in the table/query (added in r769). This field and the SRID will be deduced from the query in most cases, but may need to be manually specified in some cases.
   * *host*: The name of the PostGIS server.
   * *initial_size* (default _1_):
   * *max_size* (default _10_):
   * *multiple_geometries* (default _false_):
   * *password*: The password of the username to access the PostGIS database.
   * *persist_connection* (default _true_):
   * *port*: The port of the PostGIS server.
   * *row_limit* (default _0_): The maximum number of rows to query.
   * *table*: Name of the table or PostGIS query. subquery has to use syntax of:  '( ) as table'.
   * *type* (default _utf-8_):
   * *srid* (default _0_): The integer SRID of the geometry in the table's geometry column. This can be deduced from the table parameter in most cases, but doing so requires an extra database query that can be avoided by providing this parameter.
   * *user*: Username to access the PostGIS database.

 * Additional parameters for type *shape*
   * *encoding*:	        Character encoding in the shapefile. Default 'utf-8'. ESRI Shapefiles are usually 'latin1'
   * *file*:		For shape type; location and name (without extension) of the ESRI shapefile

 * Additional parameters for type *gdal*
   * *file*:		Path to the raster file

 * Additional parameters for type *ogr*
   * *layer*:		The layer name, run `ogrinfo` on the data to get the layer name (hint: for shapefiles it is the same name as the file)

 * Additional parameters for type *osm*
   * *file*:		location and name (with extension) of the OSM Filename
   * *parser*:            Parser for the xml file. (Should be 'libxml2')
   * *url*:               URL from which to load the OSM data.  The *bbox* parameter must also be specified.  This is not the full URL, just the base.  For example _http://127.0.0.1:8800/tiledata_
   * *bbox*:              The bounding-box parameter to be added to the URL.  There's no defined format for this, but whatever is included in this value will be appended to the URL after a '?bbox='.  So if *bbox* is *115.136719,-31.802893,116.894531,-33.284620* and URL is _http://127.0.0.1:8800/tiledata_ then the full URL used will be _http://127.0.0.1:8800/tiledata?bbox=115.136719,-31.802893,116.894531,-33.284620_.  Both *url* and *bbox* must be specified to use a URL.
----

## Rule
 * Element: *Rule*
 * Element type:

 * Attributes
  * *name*
  * *title*
 
 * Children:
  * *["Filter"]*      
  * *ElseFilter*
  * *MinScaleDenominator*
  * *MaxScaleDenominator*
  * *PointSymbolizer*
  * *LinePatternSymbolizer*
  * *PolygonPatternSymbolizer*
  * *TextSymbolizer*
  * *ShieldSymbolizer*
  * *LineSymbolizer*
  * *PolygonSymbolizer*
  * *BuildingSymbolizer*
  * *RasterSymbolizer*
  * *MarkersSymbolizer*

Also see SymbologySupport for more info on Symbolizers

> v.0.7.1: Please note that some Symbolizers require attributes while others require <CssParameter>-elements.[[BR]]
> Refer to the examples given on the individual pages for the correct syntax.[[BR]]
> This has been fixed in Mapnik 2.0

## Include
 * Element: *Include*
 * Element type: Provides a container for included XML.  Should be used only in included files as the outermost tag.

 * Attributes - None

 * Children:
  * *[#Style Style]*
  * *[#Layer Layer]*
  * *FileSource*: See http://trac.mapnik.org/changeset/574
  * *Datasource*: See [#Datasource Datasource] and http://trac.mapnik.org/changeset/574
  * *FontSet*: Defines a fontset for fallback fonts (if a character isn't found in the first font, proceed through the list until it is found)

