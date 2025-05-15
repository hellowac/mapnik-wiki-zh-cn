## Removed

- `filter_factor` removed from `GDAL` datasource options. This has always been available as a `RasterSymbolizer` property and can continue to be set there.

## Changed

- `colorize-alpha` filter now takes a single color argument (rather than requiring more than one) and will use this single color to paint in place of the existing alpha values.
- Text `label-position-tolerance`  is now a `double` rather than `unsigned` (<https://github.com/mapnik/mapnik/commit/dcbbcdd8a92d4d27176998d9a90a4c836b5174e2>)

## Deprecated

- `bilinear8` (raster `scaling` option) is not recommended for use and will be removed at Mapnik 3.x

## Added

- `webp` image support. See [[Image-IO]] for more details
- `scale-hsla` image filter
- `color-to-alpha` image filter
- `Map` level `background-image-opacity` and `background-image-comp-op`: <https://github.com/mapnik/mapnik/pull/1966>
- `offset` support for `LinePatternSymbolizer`: <https://github.com/mapnik/mapnik/pull/1991>
