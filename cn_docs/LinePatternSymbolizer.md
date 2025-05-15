# LinePattern Symbolizer

[Symbolizer](SymbologySupport) that specifies rendering of repeated png, tiff, or svg symbol to create a line. For example, a cliff edge.

Used as an alternative to a [LineSymbolizer](LineSymbolizer).

![Showing a cliff on openstreetmap.org](http://a.tile.openstreetmap.org/18/141423/87855.png)

## Configuration Options
| *parameter* | *value* | *default* | *accepts expressions* |
|---|---|---|---|
| file | path to image file | none | mapnik >= 2.0 |
| base | base path where to search for file | none | no |
| width **(removed)**| px | 4 | |
| height **(removed)**| px | 4 | |
| type **(removed)**| png tiff | none | |
| comp-op | [Compositing](Compositing) | none | no |

*Note* that the line direction matters!

## Examples

### Default

### XML
```xml
    <LinePatternSymbolizer width="16" height="16" type="png" file="/path/to/icon.png"/>
```

#### Python
```python
    l = LinePatternSymbolizer('/path/to/icon.png','png',10,10) # file, type, width, height
```

#### C++
```cpp
    rule_type rule;
    rule.append(line_pattern_symbolizer("/path/to/icon.png", "png", 20, 20)); // file, type, width, height
```