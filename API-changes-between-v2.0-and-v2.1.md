## Deprecated

 * `TextSymbolizer` - most attributes moved to either `format` or `placements` properties
   * TODO - doc all these out

## Removed

 * `GlyphSymbolizer` - functionality can now be achieved with the `TextSymbolizer`

## Changed

 * `MarkersSymbolizer`
   * `width` and `height` are now expressions rather than raw floats

## Added

 * `comp-op` - All symbolizers now support compositing in the AGG and Cairo renderers