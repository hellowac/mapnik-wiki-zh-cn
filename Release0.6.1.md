<!-- Name: Release0.6.1 -->
<!-- Version: 3 -->
<!-- Last-Modified: 2009/07/14 22:41:21 -->
<!-- Author: springmeyer -->
## Mapnik 0.6.1 Release Changelog

Announcement: http://mapnik.org/news/2009/jul/14/release_0_6_1/

Overview of the 0.6.1 Milestone: milestone:0.6.1

Complete list of [tickets closed against this milestone](http://trac.mapnik.org/query?group=status&milestone=0.6.1)

 * XML: Fixed serialization and parsing bugs related to handling of integers and Enums (#328,#353)
 * SCons: Added the ability to set the PKG_CONFIG_PATH env setting (#217)
 * SCons: Improved linking to only required libraries for libmapnik (#371)
 * Shape Plugin: Added compile time flag to allow disabling the use of memory mapped files (r1213) (#342)
 * Core: Improved support for PPC (Big endian) architectures (r1198 -> r1213)
 * Scons: Improved auto-detection of boost libs/headers (r1200) (#297)
 * Plugins: Exposed list of available/registered plugins (r1180) (#246)
 * SCons: Improve build support for SunCC (patches from River Tarnell) (r1168, r1169)
 * Python: Fixed icu::UnicodeString to PyObject converter (r1240)
 * Python: Pickling support for text_symbolizer (r1164) (#345)
 * Python: Pickling support for proj_transform and view/coord_transform (r1163) (#345) 
 * Python: Pickling support for parameters (r1162) (#345)
 * Python: Pickling support for stroke objects (r1161) (#345)
 * Python: Pickling support for line_symbolizer (r1160) (#345)
 * Python: Pickling support for projection objects (r1159) (#345)
 * Python: Pickling support for shield_symbolizer (r1158) (#345)
 * Python: Pickling support for polygon_symbolizer (r1157) (#345)
 * Python: Pickling support for query objects (r1156) (#345)
 * Python: Pickling support for pattern symbolizers (r1155) (#345)
 * Python: Pickling support for raster_symbolizer (r1154) (#345)
 * Python: Exposed dash_array get method (r1151) (#317)
 * Python: Pickling support for Coord objects (#345)
 * GDAL Plugin: Added an experimental option to open files in 'shared mode' (r1143)
 * Python: Exposed RasterSymbolizer options in Python (r1139)
 * Plugins: Fixed support for non-file based sources in GDAL and OGR plugins (#336,#337)
 * Plugins: Formal inclusion of new plugin for Kismet server (r1127) (#293)
 * Python: Made access to features and featuresets more Pythonic (r1121) (#171,#280,#283)
 * XML: Ensured relative paths in XML are interpreted relative to XML file location (r1124) (#326)
 * XML: Added ability to serialize all default symbolizer values by passing third argument to save_map(m,'file.xml',True)(r1117) (#327)
 * Core: Added support for alpha transparency when writing to png256 (patch from Marcin Rudowski) (#202)
 * SCons: Ensured ABI compatibility information is embedded in libmapnik.dylib on Mac OS X (#322)
 * SCons: Ensured that the full 'install_name' path would be added to libmapnik.dylib on Mac OS X (#374)
 * Tests: Added testing framework in Python using nose (r1101-r1105)
 * Raster Plugin: Added a tile/bbox-based read policy for large (rasters width * height > 1024*1024 will be loaded in chunks) (r1089)
 * OGCServer: Made lxml dependency optional (r1085) (#303)
 * Rasters: Handle rounding to allow better alignment of raster layers (r1079) (#295)
 * AGG Renderer: Added option to control output JPEG quality (r1078) (#198)
 * Plugins: Fixed segfault in OGR Plugin with empty geometries (r1074) (#292)