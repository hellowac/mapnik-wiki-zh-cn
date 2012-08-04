Released Aug 3, 2012

(Packaged from [adb2ec741](https://github.com/mapnik/mapnik/commit/adb2ec741))

- Fixed handling of empty WKB geometries ([#1334](https://github.com/mapnik/mapnik/issues/1173))

- Fixed naming of `stroke-dashoffset` in save_map ([cc3cd5f63f28](https://github.com/mapnik/mapnik/commit/cc3cd5f63f28))

- Fixed support for boost 1.50 ([8dea5a5fe239233](https://github.com/mapnik/mapnik/commit/8dea5a5fe239233))

- Fixed TextSymbolizer placement in Cairo backend so it respects avoid-edges and minimum-padding across all renderers ([#1242](https://github.com/mapnik/mapnik/issues/1173))

- Fixed ShieldSymbolizer placement so it respects avoid-edges and minimum-padding across all renderers ([#1242](https://github.com/mapnik/mapnik/issues/1173))

- Rolled back change made in 2.0.1 to marker width/height meaning that Mapnik > 2.0.2 will stick to assuming width/heigh are radii for back compatibility with 2.0.0. The reverted change is seen below as "Fix Markers rendering so that ellipse height/width units are pixels (previously were unintentionally radii)". Issue tracking this is [#1163](https://github.com/mapnik/mapnik/issues/1173)

- XML: Fixed to avoid throwing if a `<Parameters>` element is encountered (which is supported in >= 2.1.x)

- Support for PostGIS 2.0 in the pgsql2sqlite command ([e69c44e](https://github.com/mapnik/mapnik/commit/e69c44e)/[47e5b3c](https://github.com/mapnik/mapnik/commit/47e5b3c))

- Fixed reference counting of Py_None when returning null attributes from Postgres during UTFGrid encoding, which could cause a Fatal Python error: deallocating None ([#1221](https://github.com/mapnik/mapnik/issues/1173))

- Fixed possible breakage registering plugins via python if a custom PREFIX or DESTDIR was used (e.g. macports/homebrew) ([#1171](https://github.com/mapnik/mapnik/issues/1173))

- Fixed memory leak in the case of proj >= 4.8 and a projection initialization error ([#1173](https://github.com/mapnik/mapnik/issues/1173)) 
