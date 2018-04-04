# Mapnik configuration XML

See also [a reference PDF](http://gis.19327.n8.nabble.com/attachment/5340415/0/MapnikXMLDescription.pdf) created by David Eastcott (written for 0.7)

## General

Comments can be placed in the file using the default xml &lt;!-- --> syntax

Basic usage: a [Map](#map) consists of [Styles](#style) defined in [Rules](#rule), and [Layers](#layer) apply those [Styles](#style) by name to [Datasources](#datasource) such as a Shapefile:
```xml
<Map background-color="white" srs="+proj=tmerc +lat_0=49 +lon_0=-2 +k=0.9996012717 +x_0=400000 +y_0=-100000 +ellps=airy +towgs84=446.448,-125.157,542.06,0.1502,0.247,0.8421,-20.4894 +units=m +no_defs">
  <Style name="TidalWater_FullColour">
    <Rule>
      <MinScaleDenominator>1000</MinScaleDenominator>
      <MaxScaleDenominator>25000</MaxScaleDenominator>
      <PolygonSymbolizer fill="#D5F4F8"/>
    </Rule>
  </Style>
  <Layer>
    <StyleName>TidalWater_FullColour</StyleName>
    <Datasource>
      <Parameter name="file">./OS-VectorMap-District/st/ST_TidalWater.shp</Parameter>
      <Parameter name="type">shape</Parameter>
    </Datasource>
  </Layer>
</Map>
```

## &lt;Map&gt;
 * Element type: The master object of a Mapnik configuration XML. Has map-wide parameters and serves as the container for Styles and Layers.
 * Attributes (in alphabetical order):
   * *"background-color"=* HTML color code for the background-color of the map (for instance #000000)
     * was *"bg-color"=* prior to Mapnik2.
     * Opacity is controlled by the last two digits of an 8-digit value. #00000000 means transparent background. The default value is #000000FF.
   * *"background-image"=* Available in Mapnik2: use an image for the background instead of a color fill.
   * *"buffer-size"=* Default 0; Good value is usually tile size/2 to help avoid cut labels. This influences envelope used by placement detector ( i.e. 'avoid_edges' parameter). Also set maximum-extent, otherwise you will get problems for bboxes near the borders of your map.
   * *"font-directory"=* Available in Mapnik2: pass a directory that contains fonts, which will automatically be registered if they end in ttf, otf, ttc, pfa, pfb, ttc, or dfont.
   * *"maximum-extent"=* Set to maximum extent of (projected) map, ie. in coordinates of result map. For instance "-20037508.34, -20037508.34, 20037508.34, 20037508.34". See also [[BoundsClipping]].
   * *"minimum-version"=* Declare the minimum version of mapnik to be used with the stylesheet. Example: minimum-version="0.6.1". Will print a notice if you use an older mapnik version. 
   * *"paths-from-xml"=* Check if relative paths should be interpreted as relative to/from XML location (default is true)
   * *"srs"=* Coordinate system in which the map is rendered (for instance '+proj=latlong+datum=WGS84' for a WGS84 Geographic coordinate system)

 * Children:
   * *[&lt;Datasource&gt;](#datasource)* See also [37f49e2](https://github.com/mapnik/mapnik/commit/37f49e29cce2d334fe9839)
   * *[&lt;FileSource&gt;](#filesource)*: See [37f49e2](https://github.com/mapnik/mapnik/commit/37f49e29cce2d334fe9839)
   * *&lt;FontSet&gt;*: Defines a fontset for fallback fonts (if a character isn't found in the first font, proceed through the list until it is found)
   * *&lt;Include&gt;*: The container tag used to wrap all context in files included via XInclude
   * *[&lt;Layer&gt;](#layer)*
   * *[&lt;Style&gt;](#style)* 

   * *xmlcomment*: (Ignored by Mapnik)
   * *xmlattr*: (Ignored by Mapnik)


## &lt;Style&gt;
 * Element type: Collection of Rules. Defines the way objects are rendered. A Mapnik configuration file can have an unlimited number of Style objects. Referenced by Layer objects to render geodata.
 * Attributes:
   * *"filter-mode"=* Whether *all* rules in the Style should be evaluated (default) or if rendering should stop after the *first* matching rule. See [#706](https://github.com/mapnik/mapnik/issues/706)
   * *"name"=* Name for this Style object. Needs to be unique per configuration file. A Style is referenced by a Layer through the corresponding StyleName parameter. If a name is ommited, what will happen?
   * *"opacity"=* Style level opacity: 1 is fully opaque while zero is fully transparent and .5 would be 50% transparent. See [#314](https://github.com/mapnik/mapnik/issues/314)
 * Children:
   * *[&lt;Rule&gt;](#rule)*
   * *xmlcomment*: (Ignored by Mapnik)
   * *xmlattr*: (Ignored by Mapnik)

## &lt;Rule&gt;
 * Element type: specifies the symbology to use at a particular zoom level
 * Attributes
   * *"name"=* optional
   * *"title"=* 
 * Children (scale, filter-by-column-values, symbology):
   * *[&lt;MinScaleDenominator&gt;](MinScaleDenominator)*: minimum map scale at which this rule applies
   * *[&lt;MaxScaleDenominator&gt;](MaxScaleDenominator)*: maximum map scale at which this rule applies
   * *[&lt;Filter&gt;](Filter)*: optionally apply based on attribute value
   * *[&lt;ElseFilter&gt;](ElseFilter)*: optionally apply based on attribute value
   * *[&lt;PointSymbolizer&gt;](PointSymbolizer)* (Similar to MarkersSymbolizer, see [#2115](https://github.com/mapnik/mapnik/issues/2115))
   * *[&lt;LineSymbolizer&gt;](LineSymbolizer)*
   * *[&lt;LinePatternSymbolizer&gt;](LinePatternSymbolizer)*
   * *[&lt;MarkersSymbolizer&gt;](MarkersSymbolizer)*
   * *[&lt;ShieldSymbolizer&gt;](ShieldSymbolizer)*
   * *[&lt;PolygonSymbolizer&gt;](PolygonSymbolizer)*
   * *[&lt;PolygonPatternSymbolizer&gt;](PolygonPatternSymbolizer)*
   * *[&lt;TextSymbolizer&gt;](TextSymbolizer)*
   * *[&lt;RasterSymbolizer&gt;](RasterSymbolizer)*
   * *[&lt;BuildingSymbolizer&gt;](BuildingSymbolizer)*
   * *[&lt;GroupSymbolizer&gt;](GroupSymbolizer)*
   * *[&lt;DebugSymbolizer&gt;](DebugSymbolizer)*

See [[SymbologySupport]] for more info on Symbolizers

> v.0.7.1: Please note that some Symbolizers require attributes while others require <CssParameter>-elements.
> Refer to the examples given on the individual pages for the correct syntax.
> This has been updated in Mapnik 2.0

## &lt;Layer&gt;
 * Element type: Applies a Style (StyleName) to a DataSource
 * Attributes:
   * *"abstract"=* Default ""
   * *"cache-features"=* Default "off". Setting this to "on" triggers mapnik to attempt to cache features in memory for rendering when (and only when) a layer has multiple styles attached to it. (only available in >mapnik 2 since r2636).
   * *"clear-label-cache"=* Default "off". Setting this to "on" clears the internal placement detector list, causing the items of this layer, and from this layer on, to be rendered without taking previous rendered items into account ('clear collision avoidance list')
   * *"minzoom"=* Default 0.0
   * *"maxzoom"=* Default 1.797693134862316e+308
   * *"name"=* The name of the layer
   * *"srs"=* Default inherits from Map.srs; Reference system from the the project [Proj.4](http://trac.osgeo.org/proj/). e.g. +proj=latlong +datum=WGS84
   * *"status"=* Default "on"; *on* or *off*, "0" or "1"
   * *"title"=* Default ""
   * *"queryable"=* Default "false"
 * Children:
   * *[&lt;Datasource&gt;](#datasource)*: The geodata to be rendered.
   * *&lt;StyleName&gt;*: The name of a defined Style. Must contain the exact same string as in the attribute *Style.name*.

## &lt;Datasource&gt;
 * Element type: References the map data source and parameters.
 * Attributes:
   * *"name"=* Create a datasource template ([37f49e2](https://github.com/mapnik/mapnik/commit/37f49e29cce2d334fe9839))
   * *"base"=* Inherit from a datasource template ([37f49e2](https://github.com/mapnik/mapnik/commit/37f49e29cce2d334fe9839))
   * Generic Parameters:
     * *"type"=* The format of the data source
       * Possible values:
         * '''shape'''	:	ESRI shapefile
         * '''postgis'''	:	Postgis table or query
         * '''pgraster'''	:	Postgis table or query (containing or returning raster)
         * '''raster'''	:	Tiled or stripped TIFF
         * '''gdal'''	:	GDAL supported raster dataset (not build by default)
         * '''ogr'''          :       OGR supported vector datasource (not build by default)
         * '''osm'''		:	OpenStreetMap (not build by default)
     * *"estimate_extent"=* boolean to tell Mapnik to estimate the extent of the layer (true) or not (false)
     * *"extent"=* manually enter an extent if estimate_extent is set to false
   * Additional parameters for type *postgis* see: Parameters on the [[PostGIS]] page. 
   * Additional parameters for type *pgraster* see: Parameters on the [[PgRaster]] page. 
   * Additional parameters for type *shape* see [[ShapeFile]]
   * Additional parameters for type *gdal* see [[GDAL]].
   * Additional parameters for type *ogr* see [[OGR]].
   * Additional parameters for type *osm*  see [[OsmPlugin]]

See also the [Python API docs](http://mapnik.org/docs/v2.1.0/api/python/index.html)

## &lt;Include&rt;
 * Element type: Provides a container for included XML.  Should be used only in included files as the outermost tag.
 * Attributes - None
 * Children:
   * *[&lt;Style&gt;](#style)*
   * *[&lt;Layer&gt;](#layer)*
   * *&lt;FileSource&gt;*
   * *&lt;Datasource&gt;* See [Datasource](#datasource) 
   * *&lt;FontSet&gt;* Defines a fontset for fallback fonts (if a character isn't found in the first font, proceed through the list until it is found)
