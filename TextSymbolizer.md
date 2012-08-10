## Configuration Options for TextSymbolizer

| *parameter* | *value*  | *description* | *unit* | *default* |
----------------|---------|----------------|-------|------------|
| name        |    -      | This is the query field you want to use for the label text, e.g. "street_name" (deprecated in Mapnik2, see section "new syntax" below)| - | - |  
|face-name     |   -      | Font name (see [[UsingCustomFonts]])| - | - |
|fontset-name|| FontSet name ||
|size||Font size|||
|text-ratio|| Try to keep a given height to width ratio|||
|wrap-character||Use this character instead of a space to wrap long names|||
|wrap-width||Length before wrapping long names|px|0|
|wrap-before||Wrap text before wrap-width is reached. If this setting is off your lines will always be a bit longer than wrap-width. If this setting is on the lines will usually be a bit shorter, but can be longer if there is a single word that is longer than your current line limit.|||
|text-transform||Allows conversion of text to lower or upper case before display. Values are "none", "uppercase", "lowercase" and "capitalize". || "none" |
|line-spacing||Vertical spacing between lines of multiline labels. This spacing is in addition to the normal font line spacing|px|0|
|character-spacing||Additional horizontal spacing between characters. Currently works for point placement only, not line placement. You will get the normal spacing defined by the font plus this amount of extra space. |px|0|
|spacing||Space between repeated labels. If spacing is 0 only one label is placed.|px|0|
|label-position-tolerance||Allow labels to be moved from their point in line placement. Lower values indicate that Mapnik tries less positions and generally leads to fewer labels. Higher values lead to Mapnik trying more different positions along a line to find a free spot. If unset or 0, Mapnik sets this value based on the total length of the line to ensure enough labels are placed.|||
|force-odd-labels||Force an odd amount of labels to be generated.|bool|false|
|max_char_angle_delta||Maximum angle (in degrees) between two consecutive characters in a label allowed. The lower the number the fewer labels placed - this is to stop placing labels around sharp corners. See r365 for more info|||
|fill||Color of the text fill, e.g. #FFFFFF|||
|halo-fill||Color of the text halo|||
|halo-radius||Radius of the halo in whole pixels (fractional pixels are not accepted)|px||
|dx, dy||Displace label by fixed amount on either axis. Also see note at vertical-alignment|px|0.0|
|avoid-edges||Boolean to avoid labeling near intersection edges|||
|minimum-distance||Minimum distance between repeated labels such as street names or shield symbols (works across features)|px|0.0|
|allow-overlap||Allow labels to overlap other labels - Note: you can also clear the label collision cache at the LAYER level to promote more overlap. See 'clear_label_cache' at [[XMLConfigReference]] part layer|bool|false|
|placement||"line" to label along lines instead of by point|||
|vertical-alignment||Position of label relative to point position ("top" (label on top of point), "middle", "bottom", "auto") "auto" is "middle" for dy=0, "bottom" for dy>0, "top" for dy<0||auto|
|horizontal-alignment||Position of label relative to point position ("left, "middle", "right", "auto")||auto|
|justify-alignment||Justify multi-line text ("left, "middle", "right", "auto")||auto|
|opacity||1 is fully opaque while zero is fully transparent and .5 would be 50% transparent|-|1|
|minimum-padding||if >0 helps prevents a label (or shield) from being placed too near the edge of the map. |px|0.0|
|minimum-path-length||place labels only on paths longer than this value.|px|0.0|
|orientation||Rotate text|degree|0|
|placement-type||Placement finder algorithm. Currently supported: "dummy" (do nothing) and "simple" (automatically create new positions using a simple configuration; see below)|string|"dummy"|
|placements||List of possible placements. Only valid if placement-type="simple" is used.|string|"X"|
|upright|left,right,auto|Select which way direction is used to place characters upright.|-|auto|

## Examples

Some examples of Mapnik's ability to place text along lines:

[[/images/output_old.png]]

### XML


```xml
<TextSymbolizer face-name="DejaVu Sans Book" size="10" fill="black" halo-fill= "white" halo-radius="1" placement="line" allow-overlap="false">[FIELD_NAME]></TextSymbolizer>
```

See [[XMLGettingStarted]] for more XML example uses of TextSymbolizer.

### Python


```python
t = TextSymbolizer(Expression('[FIELD_NAME]'), 'DejaVu Sans Book', 10, Color('black'))
t.halo_fill = Color('white')
t.halo_radius = 1
t.label_placement = label_placement.LINE_PLACEMENT # POINT_PLACEMENT is default
dir(t) # for the rest of the attributes
```

### C++


```cpp
#include <mapnik/map.hpp>
#include <mapnik/font_engine_freetype.hpp>

using namespace mapnik;
try {
   freetype_engine::register_font("/path/to/font.ttf");
   /* some code */
   rule_type rule;
   text_symbolizer ts("[FIELD_NAME]", "DejaVu Sans Book", 10, color(0, 0, 0));
   ts.set_halo_fill(color(255, 255, 200));
   ts.set_halo_radius(1);
   rule.append(ts);
}
```

The first parameter is the field name of a database field, or from a shape file, or an OSM file. In case of a shape file or OSM file, the field name is case sensitive.
You must load the needed fonts first, otherwise you'll get a run time error. But you can load as many true type fonts as you like. Mapnik is coming with a couple of fonts in "mapnik/fonts". I recommend to load all of this fonts, regardless if you need them or not. 

## Placements
In Mapnik 2 the possibility to try different placements if the text can't be placed at the intended position is introduced. 

Algorithms:
### Simple
(This is the only algorithm supported in Mapnik 2.0)
It expects a string to specify which positions and size should be used. The format is POSITIONS,[SIZES].
POSITIONS is any combination of N, E, S, W, NE, SE, NW, SW (direction) and X (exact position as give by "displacement") (separated by commas, may not be empty).

[SIZE] is a optional list of font sizes, separated by commas. The first font size is always the one given in the TextSymbolizer parameters.

First all directions are tried, then font size is reduced and all directions are tried again. The process ends when a placement is found or the last font size is tried without success.

For this algorithm horizontal-alignment and vertical-alignment should be set to "auto".

Examples: 

* "N,S,15,10,8" (tries placement above with font-size give in "size" tag, then below and if that fails it tries placement above with size 15, then blow with size 15, above with 10, ...).
* "N,S" (only font size from "size" tag)
* "X,10,5" (keep position, but try to reduce size)
* _Invalid:_ "10,5" (no position specified)

Note: Whitespace is ignored, e.g. "N,S,15,10" and "N, S,15,10" and "N, S, 15, 10" are equivalent.

An XML example might look like:

```xml
<TextSymbolizer 
  allow-overlap="false"
  face-name="DejaVu Sans Book"
  placement-type="simple"
  placements="N,S,15,10,8"
/>[label]</TextSymbolizer>
```

### List
(Supported starting with Mapnik 2.1)
Here a list of styles is defined and tried one by one till a valid position is found. Each style inherits from the previous one.

It is defined in XML by:
```xml
<TextSymbolizer face-name="DejaVu Sans Book" size="16" placement="point" dy="8" fill="blue" placement-type="list">[name]
    <Placement size="10" dy="-8" fill="red"/><!-- Reduces text size and changes offset -->
    <Placement fill="green">[abbreviated_name]</Placement> <!-- size="10", dy="-8", fill="green", shorter text -->
    <Placement fill="orange" dy="8">[nr]</Placement> <!-- size="10", dy="8", fill="orange", shortest text -->
</TextSymbolizer>
```
(Note [abbreviated_name] and [nr] have to be supplied by the data source!)

## New syntax
Starting with Mapnik 2.0 a new syntax is used:

```xml
<TextSymbolizer name="[label]" />
```

becomes

```xml
<TextSymbolizer>[label]</TextSymbolizer>
```

This change was made to be forward compatible with changes to text formatting being introduced in later versions.

## New features in HarfBuzz branch
* upright="auto/left/right" (See table above)
* dx is also used for line placements
* Multi-line support for line placements