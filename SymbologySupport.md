# Symbology Support

Also see [[XMLConfigReference]] for descriptions of these elements within the xml mapfile.

## Styles

Named styles, each layer can reference 0...N styles.

Order is important -- as in the 'painter model' or [Painter's algorithm](http://en.wikipedia.org/wiki/Painter's_algorithm) to be specific. Layers that are declared first in your XML file, or added programmatically through Layer::add_style are drawn first. Layers that are declared or added later are drawn last.

## Rules

Each style can have 0...N rules. Rules can have min/max scale denominators <someone explain min/max denom here!> and filter expressions.

## Filters

Syntax for filter expressions is very simple, you enclose variables (evaluated at runtime) in square brackets: `[attribute_name]`.

Support for:

 * Arithmetic: `+`, `-`, `*`, `/`
 * Comparison: `>`, `<`, `=`, `<>`, `>=`, `<=`
 * Logical operators: `and`, `or`, `not`
 * Regular expression matching: `[attribute_name].match('reg_ex')`

See [[Filter]] for more details (especially regarding how this is different for XML).

## Symbolizers

Symbolizers describe how features should appear on a map.

 * [[LineSymbolizer]]
 * [[LinePatternSymbolizer]]
 * [[PolygonSymbolizer]]
 * [[PolygonPatternSymbolizer]]
 * [[PointSymbolizer]]
 * [[TextSymbolizer]]
 * [[RasterSymbolizer]]
 * [[ShieldSymbolizer]]
 * [[BuildingSymbolizer]]
 * [[MarkersSymbolizer]]
 * [[GlyphSymbolizer]] (deprecated)