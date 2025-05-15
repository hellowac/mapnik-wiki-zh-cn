Released June 3rd, 2013

(Packaged from [9231205](https://github.com/mapnik/mapnik/commit/9231205))

See also: [API-changes-between-v2.1-and-v2.2](https://github.com/mapnik/mapnik/wiki/API-changes-between-v2.1-and-v2.2)

- Removed 3 depedencies without loosing any functionality: `ltdl`, `cairomm` and `libsigc++` (#1804,#806,#1681)

- Added 64 bit integer support in expressions, feature ids, and the grid_renderer (#1661,#1662,#1662)

- Added the ability to disable the need for various dependencies: `proj4`, `libpng`, `libtiff`, `libjpeg`

- Added faster reprojection support between `epsg:3857` and `epsg:4326` (#1705,#1703,#1579)

- Fixed concurrency problem when using cursors in postgis plugin (#1823,#1588)

- Fixed postgres connection pool leaks when using `persist_connection=false` (#1764)

- Fixed postgres connection key to respect highest value of `max_size` and `initial_size` for any layer in map (#1599)

- Fixed potential crash in wkb parsing when postgis returns null geometry (#1843)

- Fixed blurry rendering of image and SVG icons (#1316)

- Added detection of invalid srs values when loading xml (#646)

- Added support for specifying a base_path as a third, optional argument to load_xml

- Removed muffling of projection errors while rendering (#646)

- Improved logging system (https://github.com/mapnik/mapnik/wiki/Logging)

- Added support for reading images from in memory streams (#1805)

- Optimized halo rendering. When halo radius is < 1 new method will be used automatically (#1781)

- Added `text-halo-rasterizer` property. Set to `fast` for lower quality but faster
  halo rendering (#1298) which matched new default method when radius is < 1.

- Added support in `shape`, `sqlite`, `geojson`, and `csv` plugin for handling non-latin characters in the paths to file-based resources (#1177)

- Fixed rendering of markers when their size is greater than the specified `spacing` value (#1487)

- Fixed handling of alpha premultiplication in image scaling (#1489)

- Optimized rendering when a style with no symbolizers is encountered (#1517)

- Optimized string handling and type conversion by removing `boost::to_lower`, `boost::trim`, and `boost::lexical_cast` usage (#1687,#1687,#1633)

- Optimized alpha preserving `hextree` method for quantization of png images (#1629)

- Faster rendering of rasters by reducing memory allocation of temporary buffers (#1516)

- Fixed some raster reprojection artifacts (#1501)

- Fixed raster alignment when width != height and raster is being scaled (#1748,#1622)

- Added support for caching rasters for re-use during rendering when styling more than once per layer (#1543)

- Improved compile speeds of the code - in some cases by up to 2x and removed need for freetype dependency when building code against mapnik (#1688, #1756)

- Removed internal rule cache on `mapnik::Map` c++ object (#1723)

- Improved the scaled rendering of various map features when using `scale_factor` > 1 (#1280,#1100,#1273,#1792,#1291,#1344,#1279,#1624,#1767,#1766)

- Added C++ api for overriding scale_denominator to enable rendering at fixed scale (#1582)

- Added Layer `buffer-size` that can be used to override Map `buffer-size` to avoid
  over-fetching of data that does not need to be buffered as much as other layers.
  Map level `buffer-size` will be default if layers do not set the option. Renamed a
  previously undocumented parameter by the same name that impacted clipping extent and
  was not needed (clipping padding should likely be a symbolizer level option) (#1566)

- Fixed potential file descriptor leaks in image readers when invalid images were encountered (#1783)

- Fixed alpha handling in the `blur` and `invert` image filters (#1541)

- Fixed error reporting in the python plugin (#1422)

- Added the ability to run tests without installing with `make test-local`

- Reduced library binary size by adding support for `-fvisibility-inlines-hidden` and `-fvisibility=hidden` (#1826,#1832)

- Added `mapnik::map_request` class, a special object to allow passing mutable map objects to renderer (#1737)

- Added the ability to use `boost::hash` on `mapnik::value` types (#1729)

- Removed obsolete `geos` plugin (functionality replaced by `csv` plugin) and unmaintained `kismet` plugin (#1809,#1833)

- Added new `mapnik-config` flags: `--all-flags`, `--defines`, `--git-describe`, `--includes`, `--dep-includes`, `--cxxflags`, `--cxx` (#1443)

- Added support for unicode strings as arguments in python bindings (#163)

- Added DebugSymbolizer which is able to render the otherwise invisible collision boxes (#1366)

- Optimized rendering by reducing overhead of using `gamma` property (#1174)

- Fixed rendering artifacts when using `polygon-gamma` or `line-gamma` equal to 0 (#761,#1763)

- Fixed and optimized the display of excessive precision of some float data in labels (#430,#1697)

- Removed the `bind` option for datasources (#1654)

- Added ability to access style list from map by (name,obj) in python (#1725)

- Added `is_solid` method to python mapnik.Image and mapnik.ImageView classes (#1728)

- Changed scale_denominator C++ interface to take scale as first argument rather than map.

- Added support for `background-image` in cairo_renderer (#1724)

- Fixed building symbolizer rendering to be fully sensitive to alpha (8b66128c892 / bc8ea1c5a7a)

- `<Filter>[attr]</Filter>` now returns false if attr is an empty string (#1665)

- `<Filter>[attr]!=null</Filter>` now returns true if attr is not null (#1642)

- Added support for DBF `Logical` type: #1614

- Added serialization of `line-offset` to save_map (#1562)

- Enabled default input plugin directory and fonts path to be set inherited from environment settings in
  python bindings to make it easier to run tests locally (#1594). New environment settings are:
    - MAPNIK_INPUT_PLUGINS_DIRECTORY
    - MAPNIK_FONT_DIRECTORY

- Added support for controlling rendering behavior of markers on multi-geometries `marker-multi-policy` (#1555,#1573)

- Added alternative PNG/ZLIB implementation (`miniz`) that can be enabled with `e=miniz` (#1554)

- Added support for setting zlib `Z_FIXED` strategy with format string: `png:z=fixed`

- Fixed handling of transparency level option in `octree` png encoding (#1556)

- Added ability to pass a pre-created collision detector to the cairo renderer (#1444)

- Tolerance parameter is now supported for querying datasources at a given point (#503/#1499)

- Improved detection of newlines in CSV files - now more robust in the face of mixed newline types (#1497)

- Allow style level compositing operations to work outside of featureset extents across tiled requests (#1477)

- Support for encoding `literal` postgres types as strings 69fb17cd3/#1466

- Fixed zoom_all behavior when Map maximum-extent is provided. Previously maximum-extent was used outright but
  now the combined layer extents will be again respected: they will be clipped to the maximum-extent if possible
  and only when back-projecting fails for all layers will the maximum-extent be used as a fallback (#1473)

- Compile time flag called `PLUGIN_LINKING` to allow input datasource plugins to be statically linked with the mapnik library (#249)

- Fixed `dasharray` rendering in cairo backend (#1740)

- Fixed handling of `opacity` in svg rendering (#1744)

- Fixed uneven rendering of markers along lines (#1693)

- Fixed handling of extra bytes in some shapefile fields (#1605)

- Fixed handling (finally) of null shapes and partially corrupt shapefiles (#1630,#1621)

- Added ability to re-use `mapnik::image_32` and `mapnik::grid` by exposing a `clear` method (#1571)

- Added support for writing RGB (no A) png images by using the format string of `png:t=0` (#1559)

- Added experimental support for geometry simplification at symbolizer level (#1385)
