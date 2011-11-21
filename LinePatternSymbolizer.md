<!-- Name: LinePatternSymbolizer -->
<!-- Version: 8 -->
<!-- Last-Modified: 2009/09/17 01:14:55 -->
<!-- Author: theosys -->
## Configuration Options for LinePatternSymbolizer

|| *parameter* || *value* || *default* ||
|| file || path to image file || none ||
|| base || base path where to search for file || none ||
|| width || px || 4 ||
|| height || px || 4 ||
|| type || png tiff || none ||

*Note* that the line direction matters!

## Examples
A natural=cliff tag on an OpenStreetMap tile, rendered with LinePatternSymbolizer.
[[BR]]
[[Image(http://a.tile.openstreetmap.org/18/141423/87855.png)]]

### Default


#### XML


    #!xml
    <LinePatternSymbolizer width="16" height="16" type="png" file="/path/to/icon.png"/>


#### Python


    #!python
    l = LinePatternSymbolizer('/path/to/icon.png','png',10,10) # file, type, width, height

#### C++


    #!cpp
    rule_type rule;
    rule.append(line_pattern_symbolizer("/path/to/icon.png", "png", 20, 20)); // file, type, width, height
