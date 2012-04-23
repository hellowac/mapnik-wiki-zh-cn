<!-- Name: PolygonSymbolizer -->
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

[[/images/default_polygon_symbolizer.png]]


```xml
    <PolygonSymbolizer />
```

### Default fill with Gamma correction


[[/images/gamma65_polygon_symbolizer.png]]


```xml
  <PolygonSymbolizer gamma=".65" fill="#bbbbbb"/>
```

### Custom Fill and Opacity

```xml
      <PolygonSymbolizer fill="steelblue"/>
      <PolygonSymbolizer fill-opacity="0.05" fill="green"/>

```
    
### Python
    
```python
    p = PolygonSymbolizer(Color('steelblue'))
    p.fill_opacity = 0.7
```

#### C++

``` c++
    polygon_symbolizer p(color("steelblue"));
    p.set_gamma(0.65);
    p.set_opacity(0.7);
```

----

Example output of the `rundemo.py` utilizing the PolygonSymbolizer for provinces and water bodies:

[[/images/demo256.png]]
