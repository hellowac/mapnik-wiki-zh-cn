# Mapnik 2.1.0 Changelog

Released Aug 23, 2012

(Packaged from [a25aac8](https://github.com/mapnik/mapnik/commit/a25aac8))

See also: [API-changes-between-v2.0-and-v2.1](https://github.com/mapnik/mapnik/wiki/API-changes-between-v2.0-and-v2.1)

- Feature-level compositing (`comp-op`) for all symbolizers (except building) in AGG and Cairo renderers ([#1409](https://github.com/mapnik/mapnik/issues/1409))

- Style-level compositing (`comp-op`) ([#1409](https://github.com/mapnik/mapnik/issues/1409)) and style-level opacity for AGG renderer ([#314](https://github.com/mapnik/mapnik/issues/314))

- New experimental framework for image manipulation called `image-filters` to allow things to be done across entire layer canvas like burring ([#1412](https://github.com/mapnik/mapnik/issues/1412))

- Support for recoloring stroke, fill, and opacity of SVG files ([#1410](https://github.com/mapnik/mapnik/issues/￼1410) / [#659](https://github.com/mapnik/mapnik/issues/659))

- Support for data-driven transform expressions ([#664](https://github.com/mapnik/mapnik/issues/664))

- New support for offsetting geometries / parallel lines in line_symbolizer ([#927](https://github.com/mapnik/mapnik/issues/927)/[#1269](https://github.com/mapnik/mapnik/issues/1269))

- New support for clipping geometries - now default enabled on all symbolizers ([#1116](https://github.com/mapnik/mapnik/issues/1116))

- Framework for chainable geometry transformations (called `vertex_converters`) so that you can do things like clip, smooth, and offset at the same time ([#927](https://github.com/mapnik/mapnik/issues/927))

- WKT parsing now is more robust and supports multi-geometries ([#745](https://github.com/mapnik/mapnik/issues/745))

- New support for outputting WKT/WKB/GeoJSON/SVG from mapnik.Geometry objects ([#1411](https://github.com/mapnik/mapnik/issues/1411))

- New experimental `python` datasource plugin ([#1337](https://github.com/mapnik/mapnik/issues/1337))

- New experimental `geojson` datasource plugin using in-memory rtree indexing ([#1413](https://github.com/mapnik/mapnik/issues/1413))

- Cairo rendering is now much more similiar to AGG rendering as cairo backend now supports `scale_factor` ([#1280](https://github.com/mapnik/mapnik/issues/1280)) and other fixes have landed ([#1343](https://github.com/mapnik/mapnik/issues/1343), [#1233](https://github.com/mapnik/mapnik/issues/1233), [#1344](https://github.com/mapnik/mapnik/issues/), [#1242](https://github.com/mapnik/mapnik/issues/1242), [#687](https://github.com/mapnik/mapnik/issues/687), [#737](https://github.com/mapnik/mapnik/issues/737), [#1006](https://github.com/mapnik/mapnik/issues/1006), [#1071](https://github.com/mapnik/mapnik/issues/1071))

- mapnik::Feature objects and datasource plugins now use a `Context` to store attribute schemas to reduce the memory footprint of features ([#834](https://github.com/mapnik/mapnik/issues/834))

- Added Stroke `miterlimit` ([#786](https://github.com/mapnik/mapnik/issues/786))

- Python: exposed Map `background_image` (and aliased `background` to `background_color`)

- Python: exposed BuildingSymbolizer

- Support in the CSV plugin for reading JSON encoded geometries ([#1392](https://github.com/mapnik/mapnik/issues/1392))

- Increased grid encoding performance ([#1315](https://github.com/mapnik/mapnik/issues/1315))

- Added support for setting opacity dynamically on images in polygon pattern and markers symbolizers

- Added support for filtering on a features geometry type, either `point`, `linestring`, `polygon`,
  or `collection` using the expression keyword of `[mapnik::geometry_type]` ([#546](https://github.com/mapnik/mapnik/issues/546))

- MarkersSymbolizer width and height moved to expressions ([#1102](https://github.com/mapnik/mapnik/issues/1102))

- PostGIS: Added `simplify_geometries` option - will trigger ST_Simplify on geometries before returning to Mapnik ([#1179](https://github.com/mapnik/mapnik/issues/1179))

- Improved error feedback for invalid values passed to map.query_point

- Fixed rendering of thin svg lines ([#1129](https://github.com/mapnik/mapnik/issues/1129))

- Improved logging/debugging system with release logs and file redirection (<https://github.com/mapnik/mapnik/wiki/Logging>) ([#937](https://github.com/mapnik/mapnik/issues/937) and partially [#986](https://github.com/mapnik/mapnik/issues/986), [#467](https://github.com/mapnik/mapnik/issues/467))

- GDAL: allow setting nodata value on the fly (will override value if nodata is set in data) ([#1161](https://github.com/mapnik/mapnik/issues/1161))

- GDAL: respect nodata for paletted/colormapped images ([#1160](https://github.com/mapnik/mapnik/issues/1160))

- PostGIS: Added a new option called `autodetect_key_field` (by default false) that if true will
  trigger autodetection of a given tables' primary key allowing for feature.id() to represent
  globally unique ids. This option has no effect if the user has not manually supplied the `key_field` option. ([#804](https://github.com/mapnik/mapnik/issues/804))

- Cairo: Add full rendering support for markers to match AGG renderer functionality ([#1071](https://github.com/mapnik/mapnik/issues/1071))

- Fix Markers rendering so that ellipse height/width units are pixels (previously were unintentionally radii) ([#1134](https://github.com/mapnik/mapnik/issues/1134))

- Added `ignore-placement` attribute to markers-symbolizer ([#1135](https://github.com/mapnik/mapnik/issues/1135))

- Removed `PointDatasource` - use more robust MemoryDatasource instead ([#1032](https://github.com/mapnik/mapnik/issues/1032))

- SQLite - Added support for !intersects! token in sql subselects ([#809](https://github.com/mapnik/mapnik/issues/809)) allow custom positioning of rtree spatial filter.

- New CSV plugin - reads tabular files - autodetecting geo columns, newlines, and delimiters. Uses in-memory featureset for fast rendering and is not designed for large files ([#902](https://github.com/mapnik/mapnik/issues/902))

- Fixed bug in shield line placement when dx/dy are used to shift the label relative to the placement point (Matt Amos) ([#908](https://github.com/mapnik/mapnik/issues/908))

- Added <layer_by_sql> parameter in OGR plugin to select a layer by SQL query (besides name or index): see <https://www.gdal.org/ogr/ogr_sql.html> for specifications (kunitoki) ([#472](https://github.com/mapnik/mapnik/issues/472))

- Added support for output maps as tiff files (addresses [#967]((https://github.com/mapnik/mapnik/issues/967)) partially)

- Added support for justify-alignment=auto. This is the new default. ([#1125](https://github.com/mapnik/mapnik/issues/1125))
