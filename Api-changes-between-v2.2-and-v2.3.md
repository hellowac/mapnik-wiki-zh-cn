## Removed

 - `filter_factor` removed from `GDAL` datasource options. This has always been available as a `RasterSymbolizer` property and can continue to be set there.

## Changed

 - Default PNG output now is paletted using the high quality alpha-preserving `hextree` encoder (what used to be only possible with `png8:m=h`. This is now triggered when the `png` format string is used. Use `png32` to maintain rendering of full color rgba images as previously. More details at [this ticket](https://github.com/mapnik/mapnik/issues/2028) and [[Image-IO]]
 - `colorize-alpha` filter now takes a single color argument (rather than requiring more than one) and will use this single color to paint in place of the existing alpha values.
 - Text `label-position-tolerance`  is now a `double` rather than `unsigned` (https://github.com/mapnik/mapnik/commit/dcbbcdd8a92d4d27176998d9a90a4c836b5174e2)

## Added
 - `webp` image support. See [[Image-IO]] for more details
 - `scale-hsla` image filter
 - `color-to-alpha` image filter