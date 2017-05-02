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

 - PostGIS/PGraster: The `table`/`geometry_table`/`raster_table` parameter in XML style must be quoted if it would need quoting in SQL query (refs [#3618](https://github.com/mapnik/mapnik/pull/3618)):
```xml
<!-- Mapnik 3.0 -->
<Parameter name="geometry_table">rolling stones</Parameter>

<!-- Mapnik 3.1 -->
<Parameter name="geometry_table">"rolling stones"</Parameter>
```

## Added

 - PGraster: Variable interpolation just like PostGIS plugin (refs [#3618](https://github.com/mapnik/mapnik/pull/3618)).

TODO