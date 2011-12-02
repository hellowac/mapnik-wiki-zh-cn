<!-- Name: PolygonSymbolizer -->
<!-- Version: 11 -->
<!-- Last-Modified: 2010/06/01 04:51:30 -->
<!-- Author: manelclos -->
## Configuration Options for PolygonSymbolizer

A PolygonSymbolizer is often used to render the area enclosed by a [polygon](http://en.wikipedia.org/wiki/Polygon). For example, the `rundemo.py` and `rundemo.cpp` applications use PolygonSymbolizer objects to "fill-in" [Canadian provinces with different colors and to make bodies of water look blue](http://trac.mapnik.org/attachment/wiki/PolygonSymbolizer/demo256.png?format=raw).

| *parameter* | *value*  | *default* |
-------------|---------|------------|
| fill            |  CSS colour | "grey" |
| fill-opacity | 0.0 - 1.0 | 1.0 |
| gamma | 0.0 - 1.0 | 1.0 |

* Note: gamma is available in Mapnik >= 0.7.0, see #428 for more detail.

## Examples

### Default

[[BR]]
[[Image(default_polygon_symbolizer.png)]]


    #!xml
    <PolygonSymbolizer />

### Default fill with Gamma correction
[[BR]]
[[Image(gamma65_polygon_symbolizer.png)]]


    #!xml
    <PolygonSymbolizer>
        <CssParameter name="gamma">.65</CssParameter>
    </PolygonSymbolizer>

### Custom Fill and Opacity


    #!xml
    <PolygonSymbolizer>
         <CssParameter name="fill">steelblue</CssParameter>
         <CssParameter name="fill-opacity">0.5</CssParameter>
    </PolygonSymbolizer>
     }}}
    
    ==== Python ====
    
    {{{
    #!python
    p = PolygonSymbolizer(Color('steelblue'))
    p.fill_opacity = 0.7

#### C++

` FIXME `


----

Example output of the `rundemo.py` utilizing the PolygonSymbolizer for provinces and water bodies:

 [[BR]]
[[Image(demo256.png)]]
