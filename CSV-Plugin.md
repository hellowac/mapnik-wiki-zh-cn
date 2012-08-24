_New in Mapnik 2.1_

This plugin can read tabular data with embedded geometries. It auto-detects column types based on common sense type coercion and auto-detects geometry data by looking for header names like `latitude/lat` and `lon/long/lng/longitude` that likely encode point data. It can also handle GeoJSON and WKT encoded geometries and will find these if any column headers are named `geojson` or `wkt` (case-insensitive).

This plugin reads the entire file upon initialization and caches features in memory so it is extremely fast for rendering from after initial startup (for reasonable size files under 5-10 MB).

For more details on the motivations and design of this plugin see: https://github.com/mapnik/mapnik/issues/902
