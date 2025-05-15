## Removed

- `geos` and `kismet` plugins were removed (#1809,#1833)
- `ltdl`, `cairomm`, and `libsigc++` dependencies were removed
- Removed the `bind` option for datasources (#1654)

## Changed

- The `max_size` and `initial_size` options for the `PostGIS` datasource impact behavior for a single, global pool of postgresql connections. In Mapnik >= 2.2.0, when set for any layer, if the `max_size` or `initial_size` is larger than the default (10 for `max_size` and 1 for `initial_size`) or any previously set value then the global value will be increased. In older Mapnik only the values set in the first layer would be respected. [Ticket](https://github.com/mapnik/mapnik/issues/1599)
- Proj4 init errors due to invalid `srs` values will now cause exceptions when a map is loaded from XML as well as when encountered during rendering. The latter will very unlikely happen now that validation is done at map loading time. Previously errors were not reported except at render time and only as warnings printed to stderr (#646)
- <strike>`<Filter>[attr] != ''</Filter>` now matches only empty strings. This syntax previously matched both empty strings and nulls but this behavior was unintended and buggy given that Mapnik has supported a `null` type since 2.0.0. If you wish to filter out all `attr` values that are not `empty strings` or `null` or `false boolean type` then you can do `<Filter>[attr]</Filter>` or `<Filter>[attr] != '' and [attr] != null and [attr] != false</Filter>`</strike> No longer the case for 2.2 release, due to backwards compatibility fix as per <https://github.com/mapnik/mapnik/issues/1859>

## Added

- Added Logging framework documentation synced with 2.2 status: <https://github.com/mapnik/mapnik/wiki/Logging>
- `DebugSymbolizer` - if used it will draw the invisible collision boxes collected up to that point in rendering the stylesheet. Also can be used to draw all verticies of geometries with `mode=vertex` (#1366)
- Added new `mapnik-config` flags: `--all-flags`, `--defines`, `--git-describe`, `--includes`, `--dep-includes`, `--cxxflags`, `--cxx` (#1443)
- Added support for reading images from in memory streams (#1805) in c++ and python.
- Added `text-halo-rasterizer` property. Set to `fast` for lower quality but faster halo rendering (#1298) which matched new default method when radius is < 1.
- Added C++ api for overriding scale_denominator to enable rendering at fixed scale (#1582)
- Added Layer `buffer-size` that can be used to override Map `buffer-size` (#1566)
- Added `mapnik::map_request` class, a special object to allow passing mutable map objects to renderer (#1737)
- Added `is_solid` method to python mapnik.Image and mapnik.ImageView classes (#1728)
- Added support for controlling rendering behavior of markers on multi-geometries `marker-multi-policy` (#1555,#1573)
- Added alternative PNG/ZLIB implementation (`miniz`) that can be enabled with `e=miniz` (#1554)
- Added support for setting zlib `Z_FIXED` strategy with format string: `png:z=fixed`
- Added ability to re-use `mapnik::image_32` and `mapnik::grid` by exposing a `clear` method (#1571)
- Added support for writing RGB (no A) png images by using the format string of `png:t=0` (#1559)
