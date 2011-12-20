<!-- Name: PointSymbolizer -->
<!-- Version: 19 -->
<!-- Last-Modified: 2011/03/02 01:02:42 -->
<!-- Author: Ldp -->
# PointSymbolizer

A PointSymbolizer specifies the rendering of a "graphic symbol" at a point.

If you want to draw a graphic symbol and a text you would better use a ShieldSymbolizer.

Staring from r1793 PointSymbolizer supports [Scalable Vector Graphics (SVG)](http://www.w3.org/TR/SVG/) as input images,
see examples below.

| *parameter* | *value*  | *default* |
--------------|---------|-----------|
| file    |  path to image file | none |
| width | px | 4 |
| height | px | 4 |
| type | png tiff (+ svg (trunk)) | none |
| allow_overlap | allow text to overlap the point image; true/false | false |
| opacity | *Development version (trunk)* Opacity of the symbolizer: 0.0 - 1.0 | 1.0 | 
|   transform    |   [SVG transform](http://www.w3.org/TR/SVG/coords.html#TransformAttribute) | identity |
|   ignore-placement | allow subsequent point/shield symbolizers to overlap this symbol; true/false | false |

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
    <PointSymbolizer allow_overlap="yes" file="/Users/artem/projects/ 
    openstreetmap/mapnik/symbols/station_small.png" type="png" width="5"  
    height="5" />
```

### Do Not Allow Overlap

[[/images/allow_overlap=no.png]]

#### XML

```xml
    <PointSymbolizer allow_overlap="no" file="/Users/artem/projects/ 
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
