## Removed
 * Python pickling support was removed for `map/style/rule/symbolizers/fontset/query` - these were poorly maintained and future support for fast, core deepcopy should handle most key use cases - see [#1390 (map deepcopy)](https://github.com/mapnik/mapnik/issues/1390)
 * `MetaWriter` - [disabled in 2.1.x series - may be re-enabled in future releases](https://github.com/mapnik/mapnik/issues/1240)
 * `PointDatasource` - Use `MemoryDatasource` instead. PointDatasource was an incomplete wrapper around MemoryDatasource, and is obsolete now that `Feature` objects can leverage WKB and WKT to create geometries and features can be added to MemoryDatasources.
 * `GlyphSymbolizer` - functionality can now be achieved with the `TextSymbolizer`
 * `MarkersSymbolizer` 
  * `marker-type` is removed, built in ellipse and arrow types now can be referenced like `file="shape://ellipse"` and `file="shape://arrow"` - although this interface is unstable and may continue to change.
 * `ShieldSymbolizer` attribute `no_text` - Simply leave the text empty if you don't want any text to be rendered.
 * `XML DTD` in `utils/xml` since it was unmaintained: https://github.com/mapnik/mapnik/issues/1402

## Changed

 * `MarkersSymbolizer`
   * default `marker-placement` is now `point` instead of `line` - meaning if you want your symbols (like arrows) to be oriented along lines you now need to specify `placement=line`, whereas previously this was the default. This changes reflects the goal of making the MarkersSymbolizer default behavior more reasonable for any geometry type, including points, lines, and polygons and to make it consistent with the `TextSymbolizer` and `ShieldSymbolizer` which also default to `point` placement.
   * `width` and `height` are now optional expressions rather than raw floats and their values represent diameter in pixels not radii. If not set they will be `None`, but the default ellipse has a `radius` of `10` meaning that if you set `width="20"` and `height="20"` then there will be no change in the rendering size of the ellipse. The arrow default dimensions can be maintained with `width="27" height="12"`. Altering width or height will build a new `ellipse` svg marker internally by default if no custom file type is provided. For non-ellipse types setting `width` and `height` will proportionally scale the marker, but ideally you should use `transform="scale(x,y)" instead.
   * A new `fill-opacity` setting is available and now `opacity` reverse to a new overall opacity that will be multiplied against the `fill-opacity` or `stroke-opacity` - this is to match how svg behaves.

## Added
 * `MarkersSymbolizer`
  * `fill-opacity` is new.
  * `opacity` value now works to set the alpha of bitmap images.
 * `Expression` - you can now use the built in keyword of `[mapnik::geometry_type]` to filter features by geometry type either by name or integer key. The mapping is `0:no geometry`, `1:point`, '2:linestring`, `3:polygon`, and `4:collection`. A collection indicates that the `Feature` has more than one geometry of different types. So a `Feature` with three linestrings will be reported as `linestring` but a `Feature` with a point and a linestring will be reported as a `collection`. - for more details see [#546](https://github.com/mapnik/mapnik/issues/546)
 * To All symbolizers (in most cases)
   * `comp-op` - All symbolizers now support compositing in the AGG and Cairo renderers
   * `clip` - All(most) symbolizers - boolean of whether to clip geometries before rendering (defaults to `true`)
   * `smooth` - bezier smooth value - 0-1, 0 (default) means no smoothing, 1 means fully smoothed, higher values create wild loopbacks
 * `LineSymbolizer`
   * `offset` - offset lines either in positive (right side) or negative (left side)
 * [`TextSymbolizer`](https://github.com/mapnik/mapnik/wiki/TextSymbolizer)
   * New placement alogrithm: `list`
   * Text formatting

   Changes documented in TextSymbolizer documentation
 * Python Bindings:
   * `mapnik.Image.get_pixel()` - get unsigned int value representing the rgba value, useful for fast pixel comparisons
   * `mapnik.Grid.get_pixel()` - get int value representing the feature id encoded in the grid pixels
   * bindings for text placement and formatting work 

## Deprecated

 * `TextSymbolizer` - most attributes moved to either `format` or `placements` properties

   `properties`:
      * label-placement
      * horizontal-alignment
      * justify-alignment
      * vertical-alignment
      * orientation
      * displacement
      * label-spacing
      * label-position-tolerance
      * avoid-edges
      * minimum-distance
      * minimum-padding
      * minimum-path-length
      * maximum-angle-char-delta
      * force-odd-labels
      * allow-overlap
      * largest-bbox-only
      * text-ratio
      * wrap-width

   `format`:
      * face_name
      * fontset
      * text-size
      * character-spacing
      * line-spacing
      * text-opacity
      * wrap-char
      * wrap-before
      * text-transform
      * fill
      * halo-fill
      * halo-radius

    Backward compatibility is preserved by python wrappers, however a warning message is printed if the old name is used.


 * `RasterSymbolizer`
   *  `mode` is deprecated, now use `comp-op` which supports [many more compositing modes](https://github.com/mapnik/mapnik/blob/master/include/mapnik/image_compositing.hpp#L42-79)
   *  `scaling=fast` is deprecated. It has always been a synonym for `near`, use `near` going forward
   *  `scaling` is now exposed in python as enumerations of `mapnik.scaling_method` not as bare strings