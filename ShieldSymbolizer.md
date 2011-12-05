<!-- Name: ShieldSymbolizer -->
<!-- Version: 34 -->
<!-- Last-Modified: 2011/11/13 15:42:36 -->
<!-- Author: migurski -->
## Configuration Options for ShieldSymbolizer

NEW: Starting from r1793 ShieldSymbolizer supports [Scalable Vector Graphics (SVG)](http://www.w3.org/TR/SVG/) as input images,
see examples below.


| *parameter* | *value* | *default* |
--------------|---------|-----------|
|allow-overlap | Allow the symbolizer to overlap others | false|
|avoid-edges | Attempts to stay away from the edge of the image | false|
|base | Base symbol template. See [#574](http://trac.mapnik.org/changeset/574) (XML config only) | |
|character-spacing | Horizontal spacing between characters (in pixels). Currently works for point placement only, not line placement | 0|
|dx | Offset the text horizontally. Unit: pixels from the image's center | |
|dy | Offset the text vertically. Unit: pixels from the image's center. Also see note at vertical_alignment. | |
|face-name | Font name for the shield text | |
|file | The file to use for the shield background | |
|fill | Color of the shield text, e.g. #FFFFFF | |
|fontset-name | Name of the FontSet to use. (XML config only) | |
|halo-fill | Color of the colored halo around the text, e.g. #AF2304. | white |
|halo-radius | Thickness of the colored halo around the text as an integer value in pixels | 0 |
|height | The height of the shield file | image's height | 
|horizontal-alignment |  | middle |
|justify-alignment | | midle|
|line-spacing | Vertical spacing between lines of multi-line labels, in pixels | 0|
|min-distance | Minimum distance to the next shield symbol, not necessarily the same shield | 0|
|name | This is the query field you want to use for the label text, e.g. "ref" | |
|no-text | | false|
|opacity| opacity of the image used for the shield | 1|
|text-opacity | opacity of the text placed on top of the shield | 1|
|placement | "line" or "point" | |
|size | Font size of the shield text (a value of zero will prevent text from being written) | |
|spacing | The spacing between repeated occurrences of the same shield | |
|text-convert | Allows conversion of text to lower or upper case before display. Values are "none", "toupper", and "tolower". | "none"|
|type | Type of the shield file, e.g. "png" | |
|unlock-image | If "false", the symbol is placed relative to the text box center. If "true", the symbol is placed relative to the point position | "false"|
|vertical-alignment | Position of label relative to point position ("top" to label on top of a point, "middle", "bottom") for dy = 0, "bottom" for dy > 0, "top" for dy < 0 | "middle"|
|width | The width of the shield file| image's width |
|wrap-before| | "false"|
|wrap-character | Use this character instead of a space to wrap long names | " "|
|wrap-width | Length before wrapping long names| 0 |
| transform | *Development version (trunk)* [SVG transform] (http://www.w3.org/TR/SVG/coords.html#TransformAttribute) | |
|shield-dx|offset the shield image horizontally | |
|shield-dy|offset the shield image vertically | |

## Good to know

ShieldSymbolizer can be used to label points.[[BR]]
E.G. If you want to place points on cities and their name above it. If you try to use a TextSymbolizer and a PointSymbolizer separated you will often see points without texts and/or texts without points.[[BR]]
To draw labeled points configure your shield symbolizer with placement = point and custom value for dx/dy to move the text around the point[[BR]]


## Examples

[[BR]]
[[Image(http://wiki.openstreetmap.org/images/thumb/6/63/Mapnik-highway-motorway.png/120px-Mapnik-highway-motorway.png)]]



Setting up a sample shield symbolizer, from the Cascade Users of OpenSource GeoSpatial (CUGOS) list:
http://groups.google.com/group/cugos/browse_thread/thread/b62b4890e1933bba

### Default



#### XML


    #!xml
    <Style name="My Style">
        <Rule>
            <ShieldSymbolizer name="NAME" face-name="DejaVu Sans Bold" size="6" fill="#000000" file="images/ushighway_shield_20.png" type="png" width="20" height="20" spacing="100" min-distance="50"></ShieldSymbolizer>
        </Rule>
    </Style>

#### Python


    #!python
    shield = ShieldSymbolizer('NAME','DejaVu Sans Bold',6,Color('#000000'),'images/ushighway_shield_20.png','png',20,20)
    # parameters are: (name, font name, font size, font color, image file, image type, width, height)
    shield.min_distance = 50
    shield.label_spacing = 100
    shield.displacement(dx,dy)

#### C++


    #!cpp
    rule_type rule;
    /* Parameters:
          name
          face name
          size
          color
          image
          image type
          width
          height
    */
    shield_symbolizer ss("NAME", "DejaVu Sans Bold", 6, color(0, 0, 0), "/path/to/icon.png", "png", 20, 20);
    ss.set_label_placement(mapnik::LINE_PLACEMENT); // Place label along the line
    ss.set_displacement(dx, dy);
    ss.set_label_spacing(min_distance);
    rule.append(ss);

## SVG shields

[[Image(shield_symbolizer_svg.png)]]


    #!xml
    <Style name="My Style">
        <Rule>
            <ShieldSymbolizer name="'ABC'" fontset-name="bold-fonts" size="10" fill="green" placement="line" file="/Users/artem/Desktop/svg/shield.svg" transform="scale(2.0,2.0)" min-distance="100" spacing="250"/>
        </Rule>
    </Style>

== Resources == 
 * http://www.routemarkers.com/
 * http://www.weait.com/content/badges-badges