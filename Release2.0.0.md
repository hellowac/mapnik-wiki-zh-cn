<!-- Name: Release2.0.0 -->
<!-- Version: 5 -->
<!-- Last-Modified: 2011/09/28 01:36:00 -->
<!-- Author: artem -->
# Mapnik 2.0.0 release

Announcement: [Release 2.0](http://mapnik.org/news/2011/sep/26/release_2_0/) 

Overview of the 2.0.0 Milestone: milestone:"Mapnik 2.0"

Complete list of [tickets closed against this milestone](http://trac.mapnik.org/query?group=status&milestone=Mapnik%202.0)

## Mapnik 2.0.0 Changelog

- Add minimum-path-length property to text_symbolizer to allow labels to be placed only on lines of a certain length (#865)

- Add support for png quantization using fixed palettes (#843)

- Add AlsoFilter functionality - http://trac.mapnik.org/wiki/AlsoFilter

- SQLite Plugin: optimize i/o using shared cache and no mutexes (#797)

- Directly link input plugins to libmapnik to avoid having to set dlopen flags from binding languages (#790)

- Throw an error during registration for fonts which Freetype2 does not report a family or style name (r2985).

- Fixed quoting syntax for "table"."attribute" in PostGIS plugin (previously if table aliases were used quoting like "table.attribute" would cause query failure) (r2979).

- Added the ability to control the PostGIS feature id by suppling a key_field to reference and integer attribute name (r2979).

- Added alternative, more robust proj_transform functions to project a bbox using more points than just the four
  corners to ensure an optimally sized bbox despite proj4 out of bounds conditions. (olt)

- Added map.base parameter that can be set to control where files with relative paths should be interpreted
  from when a map is loaded from a string or saved to a string. It defaults to an empty string which means
  that the base path will be the current working directory of the mapnik process. When a stylesheet is read
  from a file that files directory is used. And a custom value can still be passed as an argument to 
  load_map_from_string().

- Added python function 'render_grid' to allow conversion of grid buffer to python object containing list of grid
  pixels, list of keys, and a and dictionary of feature attributes.

- Added new rendering backend, grid_renderer, that collects the attributes of rendered features and
  burns their ids into a grid buffer.

- Added optional 'maximum-extent' parameter to map object. If set will be used, instead of combined
  layer extents, for return value of map.zoom_all(). Useful in cases where the combined layer extents
  cannot possibly be projected into the map srs or the user wishes to control map bounds without
  modifying the extents of each layer.

- Support for NODATA values with grey and rgb images in GDAL plugin (#727)

- Print warning if invalid XML property names are used (#110)

- Made XML property names use consistent dashes, never underscores (#644)

- Added support for drawing only first matching rule using filter-mode="first" in Style (#706)

- Added support to PointSymbolizer ('ignore_placement') for skipping adding placed points to collision detector (#564)

- Added ability to register fonts within XML using Map level 'font_directory' parameter (#168)

- TextSymbolizer: Change text_convert to text_transform to better match css naming (r2211)

- Shapefile Plugin: Throw error if attribute name is requested that does not exist (#604)

- Upgraded to the latest proj4 string literal for EPSG:4326 (WGS84) as global default projection (#333)

- Added 'mapnik_version_from_string()' function in python bindings to easily convert string representation
  of version number to the integer format used in 'mapnik/version.hpp'. e.g. '0.7.1' --> 701.

- Added xinclude (http://www.w3.org/TR/xinclude/) support to libxml2-based xml parser (oldtopos) (#567)

- Optimized rendering speeds by avoiding locking in the projection code (r2063) (r2713)

- Added support for setting global alignment of polygon pattern fills (#203)

- Added support for choosing OGR layer by index number using 'layer_by_index' parameter (r1904)

- Added support for fractional halo widths (using FT Stroker) (#93)

- Added support for reading jpeg images (in addition to png/tiff) for image symbolizers (#518)

- Made libjpeg dependency optional at compile time and added mapnik2.has_jpeg() method to check for support in python (#545).

- Fixed reading of PostGIS data on Big Endian systems (#515)

- PostGIS: Added better support for alternative schemas (#500)

- AGG Renderer - Enforced default gamma function on all symbolizers to ensure proper antialiasing
  even when gamma is modified on the PolygonSymbolizer. (#512)

- Added ability to read pre 2.0.0 stylesheets, but prints a warning for deprecated syntax (r1592, #501)

- Rasterlite Plugin: Experimental support for Rasterlite, to practically use sqlite database with wavelet compressed rasters (#469)

- PNG: fixed png256 for large images and some improvements to reduce color corruptions (#522)

- Implement MarkersSymbolizer in Cairo render and improve the markers placement finder. (#553)
