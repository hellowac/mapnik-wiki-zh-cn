# Mapnik Releases

Past, current, and future releases.

## 3.0.6

Changelog: [[Api-changes-between-v2.3-and-v3.0]]


## 2.2.0
_2013-06-03_

Changelog: [[Release2.2.0]]

The 2.2.0 release is primarily a performance and stability release. The code line represents development in the master branch since the release of 2.1.0 in Aug 2012 and therefore includes nearly a year of bug-fixes and optimizations. Nearly 500 new tests have been added bring the total coverage to 925. Shapefile and PostGIS datasources have benefited from numerous stability fixes, 64 bit integer support has been added to support OSM data in the grid renderer and in attribute filtering, and many fixes have landed for higher quality output when using a custom `scale_factor` during rendering. Critical code paths have been optimized include raster rendering, xml map loading, string to number conversion, vector reprojection when using `epsg:4326` and `epsg:3857`, `hextree` encoding, halo rendering, and rendering when using a custom `gamma`. Mapnik 2.2 also compiles faster than previous releases in the 2.x series and drops several unneeded and hard to install dependencies making builds on OS X and Windows easier than any previous release.

* This release attempts to maintain backward compatibility in the XML styling interface and will issue new deprecation warnings for any changes. See [[API-changes-between-v2.1-and-v2.2]] for details.

## 2.1.0
_2012-08-23_

Changelog: [[Release2.1.0]]

* This release includes significant refactoring in Mapnik core, with many new features like image compositing, geometry i/o formats, image-filters, and geometry clipping and smoothing. It has vastly improved map loading speeds and better rendering performance all around.
* This release attempts to maintain backward compatibility in the XML styling interface and will issue new deprecation warnings for changes. See [[API-changes-between-v2.0-and-v2.1]] for details.
* New datasource plugins include: [GeoJSON](https://github.com/mapnik/mapnik/wiki/GeoJSON-Plugin), [CSV](https://github.com/mapnik/mapnik/wiki/CSV-Plugin), and [Python](https://github.com/mapnik/mapnik/wiki/Python-Plugin).
* This release does not maintain full backwards compatibility in the python datasource API - notably the mapnik.Feature interface has changed slightly and now requires a mapnik.Context to be passed to the constructor.
* This release includes major refactoring of the TextSymbolizer, but should still be backwards compatible from XML and python.

## 2.0.2
_2012-08-03_

Changelog: [[Release2.0.2]]

Small bugfix release. Significance is a several memory leaks and crash possibilities were fixed as well as change to marker width/height was reverted that was originally backported to 2.0.1 and should not have been since it changes the rendered size of marker ellipses.

## 2.0.1
_2012-04-09_

Changelog: [[Release2.0.1]]

Small bugfix release. Significance is full compatibility with PostGIS 2.0 and it rolls back library naming from `libmapnik2` to `libmapnik` and in python now again supports `import mapnik`, while still supporting `import mapnik2` in a deprecated mode.

## 2.0.0
_2011-09-26_

Changelog: [[Release2.0.0]]

* This release includes significant refactoring in Mapnik core.
* This release is a major new version and brings several deprecation warnings and backward incompatible changes. See [[Mapnik2_Changes]] for more details. 

## 0.7.2
_2011-10-18_

Changelog: [[Release0.7.2]]

* Bug fix and forward compatibility (with Mapnik 2.0.0) release
* No backwards incompatible changes, except that it will default to using Mapnik 2 XML syntax for `mapnik.save_map()` format.

## 0.7.1
_2010-11-15_

Changelog: [[Release0.7.1]]

* Behavior change in SCons build, should now prefer linking to user installed libraries over system libs.
* Width/height/type attributes of PolygonPatternSymbolizer and LinePatternSymbolizer now optional (auto-calculated).
* Better quantized PNG output

## 0.7.0
_2010-02-03_

Changelog: [[Release0.7.0]]

* Major behavior change: PostGIS plugin now throws `mapnik::datasource_exception` when queries fail.
* Width/height/type attributes of PointSymbolizer and ShieldSymbolizer now optional (auto-calculated).
* Text vertical_alignment now dependent on dy (#485, r1527).

## 0.6.1
_2009-07-14_

Changelog: [[Release0.6.1]]
 
 * No known backward incompatible changes

## 0.6.0
_2009-04-01_

Changelog:[[Release0.6.0]]

## 0.5.1
_2008-04-05_

## 0.5.0 
_2008-02-07_

## 0.4.0
_2007-02-26_

## 0.3.0
_2006-05-22_

## 0.2.5
_2006-02-13_

## 0.2.4
_2006-01-02_

## 0.2.3 
_2005-12-03_

## 0.2.2
_2005-09-08_

## 0.2.1
_2005-09-01_

## 0.2.0
_2005-06-17_

## 0.1.0
_2005-03-06_
