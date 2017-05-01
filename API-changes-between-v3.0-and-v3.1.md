Compiler must now support c++14 to build Mapnik 3.1.x

## Removed

TODO

## Changed

 - PostGIS: Variables in postgis SQL queries must now be wrapped in `!`. In Mapnik 3.0.x you could supply `@foo` but now you must supply `!@foo!` - refs https://github.com/mapnik/mapnik/pull/3618
 - PostGIS: the `geometry_table` argument must be quoted if it contains reserved words - refs https://github.com/mapnik/mapnik/pull/3618

## Added

TODO