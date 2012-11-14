Mapnik has supported various custom compositing operations with raster layers since 0.7.x and with vector layers since 2.1.x.

For some examples of what you can do with this feature see:

 - http://mapbox.com/tilemill/docs/guides/comp-op/
 - http://mapnik.org/news/2012/08/27/stamen-compositing-mapnik-v2.1/
 - http://mapbox.com/blog/announcing-tilemill-0.10.0/
 - http://mapbox.com/blog/tilemill-compositing-operations-preview/

Compositing is supported both at the feature level and the style level.

## Feature level compositing

Feature level compositing can be triggered by setting the `comp-op` property on a symbolizer like:

```xml
<PolygonSymbolizer comp-op="multiply" />
```

This means that for every geometry processed the `multiply` operation will be used to blend the rendered pixels of the polygon against the destination pixels (all data previously rendered on the canvas).

Each symbolizer defaults to `comp-op="src-over"` which means that normal blending of the source and destination pixels will occur. Explicitly setting `comp-op="src-over"` or leaving it off will result in the same exact behavior.

If you wish to highlight places of overlap between features in the same style then feature-level compositing may be more useful. If you wish to instead highlight the way different styles overlap (and to perhaps avoid rendering artifacts from overlapping features) then style-level compositing may be preferable (see below).

## Style level compositing

Style level compositing can be triggered by setting the `comp-op` property for an entire style like:

```xml
<Style comp-op="multiply">
  <Rule>
    <PolygonSymbolizer />
    <LineSymbolizer />
  </Rule>
</Style>
```

This means that an internal, blank (fully alpha) canvas will be created before rendering. The geometries will be rendered as normal (for all symbolizers), but against this temporary canvas instead of against the main canvas. When rendering is finished then this canvas will be blended back into the main canvas using the "multiply" operation.

The default (if no `comp-op` is set on a Style) is to skip the creation of a temporary canvas. So, while setting the `comp-op` on a style to `src-over` will invoke the default blending method, but it will also be triggering the rendering all the entire style to a separate canvas, which can lead to different output - perhaps desirable, perhaps not - just be aware of this.

As of Mapnik 2.1 you can also set an `opacity` property at the style level. This will also trigger the usage of an internal, blank canvas which all features of the style will be rendered against. When the temporary canvas is blended back into the main canvas the `opacity` of the temporary canvas will be set on the fly to allow for very consistent opacity of features (this can avoid artifacts for overlapping features). In this case the `src-over` compositing operation will be used if no other `comp-op` is set.
