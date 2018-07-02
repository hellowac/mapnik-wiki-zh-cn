Compiler must now support c++14 to build Mapnik 3.1.x

## Removed

TODO

## Changed

 - PostGIS: Variables in postgis SQL queries must now additionally be wrapped in `!` (refs [#3618](https://github.com/mapnik/mapnik/pull/3618)):
```sql
-- Mapnik 3.0
SELECT ... WHERE trait = @variable

-- Mapnik 3.1
SELECT ... WHERE trait = !@variable!
```

 - PostGIS/PGraster: The `table`/`geometry_table`/`raster_table` parameter in XML style must be quoted if it would need quoting in SQL query (for example if it's a reserved word or multiple words; refs [#3618](https://github.com/mapnik/mapnik/pull/3618)):
```xml
<!-- Mapnik 3.0 -->
<Parameter name="geometry_table">rolling stones</Parameter>

<!-- Mapnik 3.1 -->
<Parameter name="geometry_table">"rolling stones"</Parameter>
```

- `load_map()` with `strict=true` throws an exception on duplicate style names (refs [#3770](https://github.com/mapnik/mapnik/pull/3770), [#3917](https://github.com/mapnik/mapnik/pull/3917)).

## Added

 - PGraster: Variable interpolation just like PostGIS plugin (refs [#3618](https://github.com/mapnik/mapnik/pull/3618)).
 - Geobuf input plugin (refs [3715](https://github.com/mapnik/mapnik/pull/3715)).
 - Layers can be nested, `comp-op` and `opacity` on Layer level are supported (refs [3474](https://github.com/mapnik/mapnik/pull/3474)).
 - `extend` option of TextSymbolizer (refs [3512](https://github.com/mapnik/mapnik/pull/3512)).
 - Text simple placement `C` for no displacement (refs [#3596](https://github.com/mapnik/mapnik/pull/3596)).
 - `angled-point` placement of MarkersSymbolizer (refs [3782](https://github.com/mapnik/mapnik/pull/3782)).

TODO