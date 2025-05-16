# API changes between v2.3 and v3.0

## Removed

- Support for `-ansi` flag / non-c++11 compile. Starting at 3.x a compiler that recognizes `-std=c++11` is required.
- Removed `paths-from-xml` option from the `<Map>` XML parser (<https://github.com/mapnik/mapnik/issues/1893>)
- `ExpressionFormat` in `TextSymbolizer`. Just use `Format` which now supports expressions for all properties (For now `ExpressionFormat` is deprecated and will be parsed automatically into `Format`).
- `bilinear8` (raster scaling option) was obsolete and therefore removed.
- `blend` method removed from `Image` object in python bindings. The same actions can be accomplished with the `composite` function and src_over method.
- `background` property in python bindings has been removed, added the `fill` method to replace all its functionality.

## Changed

- Made `clip:false` in all symbolizers (previous default was `clip:true`) - <https://github.com/mapnik/mapnik/issues/2146>
- In C++ `mapnik::Map::addLayer` was changed to `mapnik::Map::add_layer`
- In C++ `mapnik::Map::removeLayer` was changed to `mapnik::Map::remove_layer`
- In C++ `mapnik::Map::getLayer` was changed to `mapnik::Map::get_layer`
- Changed `polygon_pattern_symbolizer` to default to `global` rather than `local` for the `alignment`.
- CSV plugin now parses and stores the strings of `"true"`, and `"false"` as boolean types (rather than strings) - <https://github.com/mapnik/mapnik/issues/1540>
- `TextSymbolizer` line wrapping behavior has now changed: previously line wrapping only happened on ascii whitespace (if `wrap-character` was not provided) but now it happens on any valid wrapping characters as determined by the default locale and the behavior of the `ICU::BreakIterator`(<http://userguide.icu-project.org/boundaryanalysis>).
- `wrap-character` property for `TextSymbolizer` should behave similarly as 2.3 but the code to support it was completely re-written so there may be slight differences in render: <https://github.com/mapnik/mapnik/issues/2333>

## Added

- `MarkersSymbolizer` now supports `avoid-edges`, `offset`, `geometry-transform`, `simplify` for `line` placement and two new `placement` options called `vertex-last` and `vertex-first` to place a single marker at the end or beginning of a path. Also `clip` is now respected when rendering markers on a LineString
geometry.
- `TextSymbolizer` now supports `smooth`, `simplify`, `halo-opacity`, `halo-comp-op`, and `halo-transform`
- `ShieldSymbolizer` now supports `smooth`, `simplify`, `halo-opacity`, `halo-comp-op`, and `halo-transform`
