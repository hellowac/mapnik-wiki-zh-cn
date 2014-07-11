<!-- Name: PointSymbolizer -->
<!-- Version: 19 -->
<!-- Last-Modified: 2011/03/02 01:02:42 -->
<!-- Author: Ldp -->
# PointSymbolizer

A PointSymbolizer specifies the rendering of a "graphic symbol" at a point.

If you want to draw a graphic symbol and a text you would better use a ShieldSymbolizer.

Some options described here are not available in mapnik versions < 2.0.

| *parameter* | *value*  | *default* | *accepts expressions* |
--------------|---------|-----------|-----------------------|
| file    |  path to image file | none | mapnik >= 2.0 | 
| width **(removed)** | px | 4 | |
| height **(removed)** | px | 4 | |
| type **(removed)** | png tiff svg | none | |
| allow-overlap | allow text to overlap the point image; true/false | false | no |
| opacity | Opacity of the symbolizer: 0.0 - 1.0 | 1.0 |  no |
|   transform    |   [SVG transform](http://www.w3.org/TR/SVG/coords.html#TransformAttribute) | identity | mapnik >= 3.0<br>you have to specify transform, but you can use expressions for its parameters, e.g. `"rotate([value1]) scale([value2])"` |
|   ignore-placement | allow subsequent point/shield symbolizers to overlap this symbol; true/false | false | no |

## Examples

#### Default

[[/images/point_symbolizer_1.png]]

[[/images/streets2.png]]

#### XML

```xml
    <PointSymbolizer/> 
```

#### Python

```python
    sym = PointSymbolizer()
```

#### C++

```cpp
    using mapnik::point_symbolizer;
    point_symbolizer sym;
```
    
### Image label
    

    [[/images/point_symbolizer_2.png]]
    
#### XML

```xml
    <PointSymbolizer file="/tmp/pub.png" width="16" height="16" type="png" /> 
```

#### Python

```python
    sym = PointSymbolizer("/tmp/pub.png", "png", 16, 16)
    # args are file, type, height, width
    sym.allow_overlap = True
    sym.opacity = .5
```

#### C++
 
```cpp
    using mapnik::point_symbolizer;
    point_symbolizer sym("/tmp/pub.png","png",16,16);
```

### Allow Overlap

[[/images/allow_overlap=yes.png]]

#### XML

```xml
    <PointSymbolizer allow-overlap="yes" file="/Users/artem/projects/ 
    openstreetmap/mapnik/symbols/station_small.png" type="png" width="5"  
    height="5" />
```

### Do Not Allow Overlap

[[/images/allow_overlap=no.png]]

#### XML

```xml
    <PointSymbolizer allow-overlap="no" file="/Users/artem/projects/ 
    openstreetmap/mapnik/symbols/station_small.png" type="png" width="5"  
    height="5" />
```

## SVG symbols (trunk)

[[/images/point_symbolizer_svg.png]]

```xml
    <PointSymbolizer file="/Users/artem/Desktop/svg/lion.svg" opacity="1.0" transform="scale(0.2,0.2)" />
```

[[/images/point_symbolizer_svg2.png]]

```xml
    <PointSymbolizer file="/Users/artem/Desktop/svg/lion.svg" opacity="1.0" transform="rotate(45) scale(0.4,0.4)" />
```
