### Important Note: The Mapnik documentation is currently in the process of being restructured and updated for Mapnik 2.0 and the move to GitHub -- please double check all information found here and fix / report any errors you may find. Thanks for your patience.


# Mapnik configuration XML

See also [a reference PDF](http://old.nabble.com/attachment/27685172/0/MapnikXMLDescription.pdf) created by David Eastcott (written for 0.7)

To validate the XML see [[ValidatingXml]]

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
  * *font-directory*: Available in Mapnik2: pass a directory that contains fonts, which will automatically be registered if they end in ttf, otf, ttc, pfa, pfb, ttc, or dfont.
  * *srs*: Coordinate system in which the map is rendered (for instance '+proj=latlong+datum=WGS84' for a WGS84 Geographic coordinate system)
  * *buffer-size*: Default 0; Good value is usually tile size/2 to help avoid cut labels. This influences envelope used by placement detector ( i.e. 'avoid_edges' parameter)
  * *paths-from-xml*: Check if relative paths should be interpreted as relative to/from XML location (default is true)
  * *minimum-version*: Declare the minimum version of mapnik to be used with the stylesheet. Example: minimum-version="0.6.1". Will print a notice if you use an older mapnik version. (Since r1453)

 * Children:
  * *[#Style Style]*
  * *[#Layer Layer]*
  * *FileSource*: See [#574](http://trac.mapnik.org/changeset/574)
  * *Datasource*: See [#Datasource Datasource] and [#574](http://trac.mapnik.org/changeset/574)
  * *FontSet*: Defines a fontset for fallback fonts (if a character isn't found in the first font, proceed through the list until it is found)
  * *Include*: The container tag used to wrap all context in files included via XInclude

  * *xmlcomment*: (Ignored by Mapnik)
  * *xmlattr*: (Ignored by Mapnik)


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


## Layer
 * Element: *Layer*
 * Element type: References a Style (StyleName) and a DataSource

 * Attributes:
  * *name*: The Name of the layer
  * *status*: Default "on"; *on* or *off*, "0" or "1"
  * *clear-label-cache*: Default "off". Setting this to "on" clears the internal placement detector list, causing the items of this layer, and from this layer on, to be rendered without taking previous rendered items into account ('clear collision avoidance list')
  * *cache-features*: Default "off". Setting this to "on" triggers mapnik to attempt to cache features in memory for rendering when (and only when) a layer has multiple styles attached to it. (only available in >mapnik 2 since r2636).
  * *srs*: Default inherits from map.srs; Reference system from the the project [Proj.4](http://trac.osgeo.org/proj/). e.g. +proj=latlong +datum=WGS84
  * *abstract*: Default ""
  * *title*: Default ""
  * *minzoom*: Default 0.0
  * *maxzoom*: Default 1.797693134862316e+308
  * *queryable*: Default "false"

 * Children:
  * *StyleName*: The name of a defined [#Style style]. The style must contain the same string in the attribute *name*.
  * *[#Datasource Datasource]*

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

 * Additional parameters for type *postgis* see: Parameters on the [[PostGIS]] page. 
 * Additional parameters for type *shape* see [[ShapeFile]]
 * Additional parameters for type *gdal* see [[GDAL]].
 * Additional parameters for type *ogr* see [[OGR]].
 * Additional parameters for type *osm*  see [[OsmPlugin]]


## Rule
 * Element: *Rule*
 * Element type:

 * Attributes
  * *name*
  * *title*
 
 * Children:
  * *[[Filter]]*      
  * *[[ElseFilter]]*
  * *[[MinScaleDenominator]]*
  * *[[MaxScaleDenominator]]*
  * *[[PointSymbolizer]]*
  * *[[LinePatternSymbolizer]]*
  * *[[PolygonPatternSymbolizer]]*
  * *[[TextSymbolizer]]*
  * *[[ShieldSymbolizer]]*
  * *[[LineSymbolizer]]*
  * *[[PolygonSymbolizer]]*
  * *[[BuildingSymbolizer]]*
  * *[[RasterSymbolizer]]*
  * *[[MarkersSymbolizer]]*

Also see [[SymbologySupport]] for more info on Symbolizers

> v.0.7.1: Please note that some Symbolizers require attributes while others require <CssParameter>-elements.

> Refer to the examples given on the individual pages for the correct syntax.

> This has been fixed in Mapnik 2.0

## Include
 * Element: *Include*
 * Element type: Provides a container for included XML.  Should be used only in included files as the outermost tag.

 * Attributes - None

 * Children:
  * *[#Style Style]*
  * *[#Layer Layer]*
  * *FileSource*: See [#574](http://trac.mapnik.org/changeset/574)
  * *Datasource*: See [#Datasource Datasource] and [#574](http://trac.mapnik.org/changeset/574)
  * *FontSet*: Defines a fontset for fallback fonts (if a character isn't found in the first font, proceed through the list until it is found)

