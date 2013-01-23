# Mapnik 0.7.2 Release

- Added forward compatibility for Mapnik 2.0 XML syntax (https://http://github.com/mapnik/mapnik/wiki/wiki/Mapnik2/Changes)

- Build fixes to ensure boost_threads are not used unless THREADING=multi build option is used

- Fixes for the clang compiler

- Support for latest libpng (>= 1.5.x) (r2999)

- Fixes to the postgres pool

- Fix for correct transparency levels in png256/png8 output (#540)

- Various build system fixes, especially for gcc compiler on open solaris.

- When plugins are not found, report the searched directories (#568)

- Improved font loading support (#559)

- Fix to shapeindex for allowing indexing of directory of shapefiles like `shapeindex dir/*shp`

- Fixed handling of null and multipatch shapes in shapefile driver - avoiding inf loop (#573)

- Fixed raster alpha blending (#589,#674)

- Enhanced support for faster reprojection if proj >= 4.8 is used (#575)

- Allow for late-binding of datasources (#622)

- Fix to OSM plugin to avoid over-caching of data (#542)

- Various fixes to sqlite, ogr, and occi driver backported from trunk.

- Ensured that '\n' triggers linebreaks in text rendering (#584)

- Support for boost filesystem v3

- Fixes to cairo renderer to avoid missing images (r2526)

- Fixed reading of label_position_tolerance on text_symbolizer and height for building_symbolizer
