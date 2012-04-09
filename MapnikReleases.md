# Mapnik Releases

Past, current, and future releases.

## 2.0.1 (Current stable release)

Changelog: [[Release2.0.1]]

Small bugfix release. Significance is full compatibility with PostGIS 2.0 and it rolls back library naming from `libmapnik2` to `libmapnik` and in python now again supports `import mapnik`, while still supporting `import mapnik2` in a deprecated mode.

## 2.0.0

Changelog: [[Release2.0.0]]

* This release include significant refactoring in Mapnik core.
* This release is a major new version and brings several deprecation warnings and backward incompatible changes. See [[Mapnik2_Changes]] for more details. 

## 0.7.2

Changelog: TBA

* Bug fix and forward compatibility (with Mapnik 2.0.0) release
* No backwards incompatible changes, except that it will default to using Mapnik 2 XML syntax for `mapnik.save_map()` format.

## 0.7.1

Changelog: [[Release0.7.1]]

* Behavior change in SCons build, should now prefer linking to user installed libraries over system libs.
* Width/height/type attributes of PolygonPatternSymbolizer and LinePatternSymbolizer now optional (auto-calculated).
* Better quantized PNG output

## 0.7.0

Changelog: [[Release0.7.0]]

* Major behavior change: PostGIS plugin now throws `mapnik::datasource_exception` when queries fail.
* Width/height/type attributes of PointSymbolizer and ShieldSymbolizer now optional (auto-calculated).
* Text vertical_alignment now dependent on dy (#485, r1527).

## 0.6.1

Changelog: [[Release0.6.1]]
 
 * No known backward incompatible changes

## 0.6.0

Changelog:[[Release0.6.0]]
