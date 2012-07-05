## Deprecated

 * `TextSymbolizer` - most attributes moved to either `format` or `placements` properties
   * TODO - doc all these out
 * `RasterSymbolizer` - `mode` is deprecated, now use `comp-op` which supports [many more compositing modes](https://github.com/mapnik/mapnik/blob/master/include/mapnik/image_compositing.hpp#L42-79)

## Removed

 * `GlyphSymbolizer` - functionality can now be achieved with the `TextSymbolizer`

## Changed

 * `MarkersSymbolizer`
   * `width` and `height` are now expressions rather than raw floats and their values represent diameter in pixel not radii

## Added

 * To All symbolizers (in most cases)
   * `comp-op` - All symbolizers now support compositing in the AGG and Cairo renderers
   * `clip` - All(most) symbolizers - boolean of whether to clip geometries before rendering (defaults to `true`)
   * `smooth` - bezier smooth value - 0-1, 0 (default) means no smoothing, 1 means fully smoothed, higher values create wild loopbacks
 * `LineSymbolizer`
   * `offset` - offset lines either in positive (right side) or negative (left side)
 