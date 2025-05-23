[[Symbolizer|SymbologySupport]] that specifies rendering of a "stroke" along a linear geometry.
## Configuration Options
| *parameter* | *value*  | *description* | *unit* | *default* | *accepts expressions*
----------------|---------|----------------|-------|------------|--------------------|
| stroke            |  CSS colour  | A Color value such as 'green' or #A3D979 | - |  "black" | mapnik >= 3.0 |
| stroke-width | 0.0 - n | Width of line | pixels |  1.0 | mapnik >= 3.0 |
| stroke-opacity | 0.0 - 1.0 | 1 is fully opaque while zero is fully transparent and .5 would be 50% transparent| transparency |  1.0  | mapnik >= 3.0 |
| stroke-linejoin  | miter, round, bevel | See [SVG stroke-linejoin](http://www.w3.org/TR/SVG/painting.html#StrokeLinejoinProperty) for an example for each value | - |  miter | no |
| stroke-linecap   | round, butt, square | See [SVG stroke-linecap](http://www.w3.org/TR/SVG/painting.html#StrokeLinecapProperty) for an example for each value | - |  butt  | no |
| stroke-dasharray | 0.0 - n,0.0 - n | A pair of length values [a,b], where (a) is the dash length and (b) is the gap length respectively. More than two values are supported as well (e.g. to start the line not with a stroke, but with a gap). | pixels | none | no |
| comp-op | | [[Compositing]] | | none | no |
| smooth | 0.0 - 1.0 | 1 means completely smoothed lines, 0 means no change | - | 0.0 |

## Examples

### Default
```xml
<LineSymbolizer />
```
#### XML
```xml
<LineSymbolizer stroke="#0000ff" stroke-width="4" />
```
#### Python

```python
l = LineSymbolizer(Color('green'),0.1)
```
To work directly with the stroke object:

```python
l = LineSymbolizer()
s = Stroke(Color('green'),0.1)
s.add_dash(.1,.1)
s.opacity = .5
l.stroke = s
```
Fetch all the possible methods like:

```python
>>> from mapnik import LineSymbolizer
>>> dir(LineSymbolizer().stroke)
```

#### C++

```cpp
rule_type rule;
stroke ls;         // This is the line symbolizer
ls.set_color(color(255, 255, 255));
ls.set_width(4);   // width of the line in pixels
ls.set_line_join(mapnik::ROUND_JOIN);
ls.set_line_cap(mapnik::ROUND_CAP);
ls.add_dash(2.5, 1.0);
ls.set_opacity(0.5);
rule.append(ls);
```