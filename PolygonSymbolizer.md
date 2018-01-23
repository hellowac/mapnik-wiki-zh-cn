[[Symbolizer|SymbologySupport]] that specifies rendering of an area enclosed by a polygon. 

For example, the `rundemo.py` and `rundemo.cpp` applications use PolygonSymbolizer objects to "fill-in" Canadian provinces with different colors and to make bodies of water look blue.

[[/images/demo256.png]]

## Configuration Options
| *parameter* | *value*  | *default* | * description * | *accepts expressions* |
-------------|---------|------------|----------------|-----------------------|
| fill            |  CSS colour | "grey" | Fill color to assign to a polygon, defaults to rgba(128,128,128,1) which means gray and fully opaque (alpha = 1), same as rgb(128,128,128) | mapnik >= 3.0 |
| fill-opacity | 0.0 - 1.0 | 1.0 | The opacity of the polygon (an alternative way of specifying alpha). Can be used in combination with an rgba color and will be multiplied with the existing alpha component of the color. | mapnik >= 3.0 |
| gamma | 0.0 - 1.0 | 1.0 | Level of antialiasing of polygon edges - basically gamma 1 (the default) means fully antialiasing, while a lesser gamma reduces the antialiasing level leading to more jaggy polygon edges. Lower gamma may be desirable in cases where you would prefer that the background color not "shine through". | mapnik >= 3.0 |
| comp-op | | none | [[Compositing]] | no |

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