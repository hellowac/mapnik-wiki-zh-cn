## Removed

 - Support for `-ansi` flag / non-c++11 compile. Starting at 3.x a compiler that recognizes `-std=c++11` is required.
 - Removed `paths-from-xml` option from the `<Map>` XML parser (https://github.com/mapnik/mapnik/issues/1893)
 - `ExpressionFormat` in `TextSymbolizer`. Just use `Format` which now supports expressions for all properties.
 - `wrap-char` (aka `wrap-character`) property for `TextSymbolizer`: https://github.com/mapnik/mapnik/issues/2333
 - `bilinear8` (raster scaling option) was obsolete and therefore removed.

## Changed

 - Made `clip:false` in all symbolizers (previous default was `clip:true`) - https://github.com/mapnik/mapnik/issues/2146
 - In C++ `mapnik::Map::addLayer` was changed to `mapnik::Map::add_layer`
 - In C++ `mapnik::Map::removeLayer` was changed to `mapnik::Map::remove_layer`
 - In C++ `mapnik::Map::getLayer` was changed to `mapnik::Map::get_layer`
 - Changed `polygon_pattern_symbolizer` to default to `global` rather than `local` for the `alignment`.
 - CSV plugin now parses and stores the strings of `"true"`, and `"false"` as boolean types (rather than strings) - https://github.com/mapnik/mapnik/issues/1540
 - Default PNG output now is paletted using the high quality alpha-preserving `hextree` encoder (what used to be only possible with `png8:m=h`. This is now triggered when the `png` format string is used. Use `png32` to maintain rendering of full color rgba images as previously. More details at [this ticket](https://github.com/mapnik/mapnik/issues/2028) and [[Image-IO]]

## Added
