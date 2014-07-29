## Removed

 - Support for `-ansi` flag / non-c++11 compile. Starting at 3.x a compiler that recognizes `-std=c++11` is required.
 - Removed `paths-from-xml` option from the `<Map>` XML parser (https://github.com/mapnik/mapnik/issues/1893)
 - `ExpressionFormat` in `TextSymbolizer`. Just use `Format` which now supports expressions for all properties.

## Changed

 - In C++ `mapnik::Map::addLayer` was changed to `mapnik::Map::add_layer`
 - In C++ `mapnik::Map::removeLayer` was changed to `mapnik::Map::remove_layer`
 - In C++ `mapnik::Map::getLayer` was changed to `mapnik::Map::get_layer`

## Added
