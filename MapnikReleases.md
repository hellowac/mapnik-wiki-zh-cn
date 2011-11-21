<!-- Name: MapnikReleases -->
<!-- Version: 14 -->
<!-- Last-Modified: 2011/10/03 14:26:07 -->
<!-- Author: springmeyer -->
# Mapnik Releases

Learn about about past, current, and future releases.

## Upgrade Notes

### Backwards Incompatibility

## 0.5.x -> 0.6.1

Changelog: wiki:Release0.6.0

Changelog: wiki:Release0.6.1
 
 * No known backward incompatible changes

## 0.7.0

Changelog: wiki:Release0.7.0

 * Major behavior change: PostGIS plugin now throws `mapnik::datasource_exception` when queries fail.
 * Width/height/type attributes of PointSymbolizer and ShieldSymbolizer now optional (auto-calculated).
 * Text vertical_alignment now dependent on dy (#485, r1527).

## 0.7.1

Changelog: wiki:Release0.7.1

 * Behavior change in SCons build, should now prefer linking to user installed libraries over system libs.
 * Width/height/type attributes of PolygonPatternSymbolizer and LinePatternSymbolizer now optional (auto-calculated).
 * Better quantized PNG output

## 0.7.2

Changelog: TBA

 * Bug fix and forward compatibility (with Mapnik 2.0.0) release
 * No backwards incompatible changes, except that it will default to using Mapnik 2 XML syntax for `mapnik.save_map()` format.

## 2.0.0

Changelog: wiki:Release2.0.0

 * This release include significant refactoring in Mapnik core.
 * This release is a major new version and brings several deprecation warnings and backward incompatible changes. See http://trac.mapnik.org/wiki/Mapnik2/Changes for more details. 


## Resources
 * [Learn about development Milestones](http://trac.mapnik.org/roadmap?show=all)
 * Download source code for releases at MapnikInstallation