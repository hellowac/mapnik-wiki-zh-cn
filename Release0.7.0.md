<!-- Name: Release0.7.0 -->
<!-- Version: 4 -->
<!-- Last-Modified: 2010/02/03 09:36:14 -->
<!-- Author: springmeyer -->
# Mapnik 0.7.0 Release

Announcement: http://mapnik.org/news/2010/jan/19/release_0_7_0/

Overview of the 0.7.0 Milestone: milestone:0.7.0

Complete list of [tickets closed against this milestone](http://trac.mapnik.org/query?group=status&milestone=0.7.0)

## Mapnik 0.7.0 Changelog

(Packaged from r1574)

- Core: Fixed linking to external libagg (r1297,r1299)

- Core: Completed full support for PPC (Big endian) architectures (r1352 -> r1357)

- Gdal Plugin: Added support for Gdal overviews, enabling fast loading of > 1GB rasters (#54)

    * Use the gdaladdo utility to add overviews to existing GDAL datasets

- PostGIS: Added an optional 'geometry_table' parameter. The 'geometry_table' used by Mapnik to look up 
  metadata in the geometry_columns and calculate extents (when the 'geometry_field' and 'srid' parameters
  are not supplied). If 'geometry_table' is not specified Mapnik will attempt to determine the name of the 
  table to query based on parsing the 'table' parameter, which may fail for complex queries with more than
  one 'from' keyword. Using this parameter should allow for existing metadata and table indexes to be used
  while opening the door to much more complicated subqueries being passed to the 'table' parameter without
  failing (#260, #426).

- PostGIS Plugin: Added optional 'geometry_field' and 'srid' parameters. If specified these will allow
  Mapnik to skip several queries to try to determine these values dynamically, and can be helpful to avoid
  possible query failures during metadata lookup with complex subqueries as discussed in #260 and #436, but
  also solvable by specifying the 'geometry_table' parameter. (r1300,#376)

- PostGIS: Added an optional 'extent_from_subquery' parameter that when true (while the 'extent' parameter is
  not provided and 'estimate_extent' is false) will direct Mapnik to calculate the extent upon the exact table
  or sql provided in the 'table' parameter. If a sub-select is used for the table parameter then this will,
  in cases where the subquery limits results, provide a faster and more accurate layer extent. It will have
  no effect if the 'table' parameter is simply an existing table. This parameter is false by default. (#456)

- PostGIS Plugin: Added 'bbox' token substitution ability in sql query string. This opens the door for various
  complex queries that may aggregate geometries to be kept fast by allowing proper placement of the bbox
  query to be used by indexes. (#415)

    * Pass the bbox token inside a subquery like: !bbox!

    * e.g. (Select ST_Union(geom) as geom from table where ST_Intersects(geometry,!bbox!)) as map

- PostGIS Plugin: Added 'scale_denominator' substitution ability in sql query string (#415/#465)

    * Pass the scale_denominator token inside a subquery like: !scale_denominator!

    * e.g. (Select * from table where field_value > !scale_denominator!) as map

- PostGIS Plugin: Added support for quoted table names (r1454) (#393)

- PostGIS: Add a 'persist_connection' option (default true), that when false will release 
  the idle psql connection after datasource goes out of scope (r1337) (#433,#434)

- PostGIS: Added support for BigInt (int8) postgres type (384)

- PostGIS Plugin: Throw and report errors if SQL execution fails (r1291) (#363, #242)

- PostGIS Plugin: Fixed problem in conversion of long numbers to strings (r1302,1303)

- PostGIS Plugin: Added missing support for BigInt(int8) postgres datatypes (r1250) (#384)

- OGR Plugin: Added support for reading multipoint features (#458)

- Shape Plugin: Fixed bug in file extension stripping (#413)

- Shape Plugin: Fixed missing compiler flags that causes crashing on newer g++ versions (#436)

- PNG: Fixed problem with garbled/striped png256 output along sharpe edges(#416,#445,#447,#202)

- PNG: Added support for semitransparency in png256 output (#477,#202)

- PolygonSymbolizer: Added 'gamma' attribute to allow for dilation of polygon edges - a solution
  to gap artifacts or "ghost lines" between adjacent polygons and allows for slight sharpening of
  the edges of non overlapping polygons. Accepts any values but 0-1 is the recommended range.
   
- TextSymbolizer: Large set of new attributes: 'text_convert', 'line_spacing', 'character_spacing', 
  'wrap_character', 'wrap_before', 'horizontal_alignment', 'justify_alignment', and 'opacity'.

    * More details at changesets: r1254 and r1341

- SheildSymbolizer: Added special new attributes: 'unlock_image', 'VERTEX' placement, 'no_text' and many
  attributes previously only supported in the TextSymbolizer: 'allow_overlap', 'vertical_alignment', 
  'horizontal_alignment', 'justify_alignment', 'wrap_width', 'wrap_character', 'wrap_before', 'text_convert',
  'line_spacing', 'character_spacing', and 'opacity'.

    * More details at changeset r1341

- XML: Added support for using CDATA with libxml2 parser (r1364)

- XML: Fixed memory leak in libxml2 implementation (#473)

- XML: Added function to serialize map to string, called 'mapnik.save_map_to_string()' (#396)

- XML: Added parameter to <Map> called 'minimum_version' to allow for enforcing the minimum Mapnik version
  needed for XML features used in the mapfiles. Uses Major.Minor.Point syntax, for example
  <Map minimum_version="0.6.1"> would throw an error if the user is running Mapnik less than 0.6.1.

- XML: Added support for relative paths when using entities and 'mapnik.load_map_from_string()' (#440)

- XML: Made width and height optional for symbolizers using images (r1543)

- XML: Ensured that default values for layers are not serialized in save_map() (r1366)

- XML: Added missing serialization of PointSymbolizer 'opacity' and 'allow_overlap' attributes (r1358)

- XML: Default text vertical_alignment now dependent on dy (#485, r1527)

- Python: Exposed ability to write to Cairo formats using 'mapnik.render_to_file()' and without pycairo (#381)

- Python: Fixed potential crash if pycairo support is enabled but python-cairo module is missing (#392)

- Python: Added 'mapnik.mapnik_svn_revision()' function to svn revision of Mapnik was compiled at.

- Python: Added 'mapnik.has_pycairo()' function to test for pycairo support (r1278) (#284)

- Python: Added 'mapnik.register_plugins()' and 'mapnik.register_fonts()' functions (r1256)

- Python: Pickling support for point_symbolizer (r1295) (#345)

- Python: Ensured mapnik::config_errors now throw RuntimeError exception instead of UserWarning exception (#442)

- Filters: Added support for '!=' as an alias to '<>' for not-equals filters (avoids &lt;&gt;) (r1326) (#427)  

- SCons: Improved boost auto-detection (r1255,r1279)

- SCons: Fixed support for JOBS=N and FAST=True to enable faster compiling (r1440)

- SCons: Ensured that -h or --help will properly print help on custom Mapnik options before a user
  has been able to properly run 'configure'. (r1514)

- SCons: Added ability to link to custom icu library name using ICU_LIB_NAME (r1414)

- SCons: Improved reliability of python linking on OSX (#380)

- Fonts: Added unifont to auto-installed fonts, which is used by the OSM styles as a fallback font (r1328)