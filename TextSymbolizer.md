## Configuration Options for TextSymbolizer

| *parameter* | *value*  | *description* | *unit* | *default* |
----------------|---------|----------------|-------|------------|
| name        |    -      | This is the query field you want to use for the label text, e.g. "street_name" (deprecated in Mapnik2, see section "new syntax" below)| - | - |  
|face_name     |   -      | Font name (see [[UsingCustomFonts]])| - | - |
|fontset_name|| FontSet name ||
|size||Font size|||
|text_ratio|| Try to keep a given height to width ratio|||
|wrap_character||Use this character instead of a space to wrap long names (since r1254)|||
|wrap_width||Length before wrapping long names|||
|wrap-before||Wrap text before wrap-width is reached. If this setting is off your lines will always be a bit longer than wrap-width. If this setting is on the lines will usually be a bit shorter, but can be longer if there is a single word that is longer than your current line limit. (Mapnik2)|||
|text_transform||Allows conversion of text to lower or upper case before display. (available in >=0.8.0) Values are "none" (default), "uppercase", "lowercase" and "capitalize". (since r2210)|||
|text_convert (old)||same as above but the old name in Mapnik 0.7.x (later renamed to text_transform to more closely match the css property.)  Values are "none" (default), "toupper", and "tolower". (since r1254)|||
|line_spacing||Vertical spacing between lines of multiline labels (in pixels) (since r1254)|||
|character_spacing||Additional horizontal spacing between characters (in pixels). Currently works for point placement only, not line placement. You will get the normal spacing defined by the font plus this amount of extra space. (since r1254)|||
|spacing||Space between repeated labels|||
|label_position_tolerance||Allow labels to be moved from their point in line placement. Lower values indicate that Mapnik tries less positions and generally leads to fewer labels. Higher values lead to Mapnik trying more different positions along a line to find a free spot. If unset or 0, Mapnik sets this value based on the total length of the line to ensure enough labels are placed. Only available in XML in >= mapnik 0.7.2 (r2440)|||
|force_odd_labels||Force an odd amount of labels to be generated. Defaults to false.|||
|max_char_angle_delta||Maximum angle (in degrees) between two consecutive characters in a label allowed. The lower the number the fewer labels placed - this is to stop placing labels around sharp corners. See r365 for more info|||
|fill||Color of the text fill, e.g. #FFFFFF|||
|halo_fill||Color of the text halo|||
|halo_radius||Radius of the halo in whole pixels (fractional pixels are not accepted)|||
|dx, dy||Displace label by fixed amount on either axis. Also see note at vertical_alignment|||
|avoid_edges||Boolean to avoid labeling near intersection edges|||
|min_distance||Minimum distance between repeated labels such as street names or shield symbols (works across features, added in r490) (named minimum-distance in Mapnik2)|||
|allow_overlap||Allow labels to overlap other labels - Note: you can also clear the label collision cache at the LAYER level to promote more overlap. See 'clear_label_cache' at wiki:XMLConfigReference#Layer|||
|placement||"line" to label along lines instead of by point|||
|vertical_alignment||Position of label relative to point position ("top" (label on top of point), "middle", "bottom", "auto") default is "auto". "auto" is "middle" for dy=0, "bottom" for dy>0, "top" for dy<0 ("auto" since r2626, same behavior since r1527, "middle" before that)|||
|horizontal-alignment||Position of label relative to point position ("left, "middle", "right", "auto") default is "auto". (Mapnik2)|||
|justify-alignment||Justify multi-line text ("left, "middle", "right", "auto") default is "auto". (Mapnik2)|||
|opacity||1 is fully opaque while zero is fully transparent and .5 would be 50% transparent|||
|minimum_padding||default 0.0, if >0 helps prevents a label (or shield) from being placed too near the edge of the map. added in r2330 (#547)|||
|minimum-path-length||default 0.0, place labels only on paths longer than this value. Added in r3272 (#865)|||
|orientation||Rotate text (Mapnik2)|||
|placement-type||Placement finder algorithm. Currently supported: "dummy" (do nothing) and "simple" (automatically create new positions using a simple configuration; see below) (since r2626)|||
|placements||List of possible placements. Only valid if placement-type="simple" is used. (since r2626)|||

In Mapnik2 all underscores "_" are replaced by dashes "-" (e.g. avoid-edges instead of avoid_edges)

## Examples

Some examples of Mapnik's ability to place text along lines:

![thumb](http://trac.mapnik.org/raw-attachment/ticket/62/output_old.png)

### XML


```xml
<TextSymbolizer name="FIELD_NAME" face_name="DejaVu Sans Book" size="10" fill="black" halo_fill= "white" halo_radius="1" placement="line" allow_overlap="false"/>
```

See [[XMLGettingStarted]] for more XML example uses of TextSymbolizer.

### Python


```python
t = TextSymbolizer('FIELD_NAME', 'DejaVu Sans Book', 10, Color('black'))
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
   text_symbolizer ts("FIELD_NAME", "DejaVu Sans Book", 10, color(0, 0, 0));
   ts.set_halo_fill(color(255, 255, 200));
   ts.set_halo_radius(1);
   rule.append(ts);
}
```

The first parameter is the field name of a database field, or from a shape file, or an osm file. In case of a shape file or osm file, the field name is case sensitive.
You must load the needed fonts first, otherwise you'll get a run time error. But you can load as many true type fonts as you like. Mapnik is coming with a couple of fonts in "mapnik/fonts". I recommend to load all of this fonts, regardless if you need them or not. 

## Placements
In r2626 the possibility to try different placements if the text can't be placed at the intended position is introduced. Currently only one algorithm ("simple") is implemented.

It expects a string to specify which positions and size should be used. The format is POSITIONS,[SIZES].
POSITIONS is any combination of N, E, S, W, NE, SE, NW, SW (direction) and X (exact position as give by "displacement") (separated by commas, may not be empty).

[SIZE] is a optional list of font sizes, separated by commas. The first font size is always the one given in the TextSymbolizer parameters.

First all directions are tried, then font size is reduced and all directions are tried again. The process ends when a placement is found or the last fontsize is tried without success.

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
  name="[label]" 
  allow-overlap="false"
  face-name="DejaVu Sans Book"
  placement-type="simple"
  placements="N,S,15,10,8"
/>
```

## New syntax
Starting with r3354 Mapnik2 supports a new syntax:

```
<TextSymbolizer name="[label]" />
```

becomes

```xml
<TextSymbolizer>[label]</TextSymbolizer>
```

This change was made to be forward compatible with changes to text formatting being introduced in later versions.
