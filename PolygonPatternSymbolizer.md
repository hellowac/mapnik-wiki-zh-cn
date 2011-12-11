<!-- Name: PolygonPatternSymbolizer -->
<!-- Version: 8 -->
<!-- Last-Modified: 2011/10/14 08:15:29 -->
<!-- Author: floledermann -->
## Configuration Options for PolygonPatternSymbolizer

| *parameter* | *value* | *default* |
--------------|---------|-----------|
| file | path to image file | none |
| width | px | 4 |
| height | px | 4 |
| type | png tiff | none |

## Examples



[[Image(http://media.mapnik.org/images/polygon_pattern.png)]]



### Default

` FIXME: Add image `

#### XML


    #!xml
    <PolygonPatternSymbolizer width="16" height="16" type="png" file="/path/to/icon.png"/>

#### Python


    #!python
    p = PolygonPatternSymbolizer('/path/to/icon.png','png',10,10) # file, type, width, height

mapnik2:


    #!python
    p = PolygonPatternSymbolizer(PathExpression('/path/to/icon.png'))

#### C++


    #!cpp
    ruly_type rule;
    rule.append(polygon_pattern_symbolizer("path/to/icon.png", "png", 20, 20)); // file, type, width, height