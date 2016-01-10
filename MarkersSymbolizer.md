|*Name*|*Description*|*Default*|Applies to SVG |
--------|------------|---------|----------------|
|allow-overlap | Allow the symbolizer to overlap others. | false | yes |
|spacing | Distance between markers in pixels. | 100 | yes |
|max-error | Maximum amount the marker can be move from its designated place to avoid collisions. This value is a fraction of "spacing", e.g. spacing = 100, max_error = 0.2 then the maximum the marker can be moved is 20pixels, if this is not enough it isn't drawn at all. | 0.2 |yes |
|file | The SVG file to use for the marker | built-in marker | yes |
|transform | [SVG transform](http://www.w3.org/TR/SVG/coords.html#TransformAttribute) | identity | yes |
|opacity | Opacity | 1.0 | yes |
|fill | Color of the marker fill, e.g. #FFFFFF. | blue | no |
| stroke | CSS colour - A Color value such as 'green' or #A3D979 | black | no |
| stroke-width | 0.0 - n  - Width of outline in pixels | 1.0 | no |
| stroke-opacity | 0.0 - 1.0 - 1 is fully opaque while zero is fully transparent and .5 would be 50% transparent | 1.0  | no |
| width | width of marker pixels | 10 | no |
| height |  height of marker in pixels | 10 | no |
| placement | "point", "interior", "line", "vertex-first" (mapnik >= 3), "vertex-last" (mapnik >= 3) | line (mapnik <=2.0.x) point (mapnik >= 2.1)| no (todo) |
| ignore-placement | "true" or "false"  | "false" | no (todo) |
| marker-type | "arrow" "ellipse" | "arrow" if line placement, "ellipse" if point placement | no |

It can be added to a Rule with line features like:

```xml
<MarkersSymbolizer />
```

[[/images/offsets_directions.png]]

The [[MarkersSymbolizer]] should draw blue directional arrows *in the direction of the geometry* (for things like one-way streets).

In case you notice arrows pointing the wrong direction, this means that the segment has been coded in the wrong way.

The ST_reverse function of Postgis can fix this (The problem will then be to identify the geometries that need to be updated).

### SVG markers

*NEW*: Staring from r1793 [[MarkersSymbolizer]] supports [Scalable Vector Graphics (SVG)](http://www.w3.org/TR/SVG/) as input images:

[[/images/markers_symbolizer.png]]


```xml
<Rule>
    <MaxScaleDenominator>10000</MaxScaleDenominator>
    <MarkersSymbolizer spacing="100" file="/Users/artem/Desktop/svg/ladybird.svg" transform="translate(0 -16) scale(2.0)"/>
</Rule>
```

### Dynamic Ellipses
*NEW*: Starting from r2158 MarkersSymbolizer supports width/height/fill/stroke properties to dynamically draw circles (w == h) or ellipses (w != h) when no SVG file is supplied:

[[/images/dynamic_ellipse_markers.png]]


```xml
<MarkersSymbolizer fill="darkorange" opacity=".7" width="20" height="10" stroke="orange" stroke-width="7" stroke-opacity=".2" placement="point" marker-type="ellipse"/>
```

CAVEAT: these properties do not apply to SVG files, and SVG transforms are not supported for modifying ellipses (yet).

OSM currently renders one-way street arrows with Mapnik using several stacked [LineSymbolizers](LineSymbolizer) with varying dash-arrays, but could potentially use the [[MarkersSymbolizer]] in the future:

```xml
<LinePatternSymbolizer file="/home/mapnik/mapnik/symbols/arrow.png" type="png" width="74" height="8" />
```
