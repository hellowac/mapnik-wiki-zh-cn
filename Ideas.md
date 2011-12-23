<!-- Name: Ideas -->
<!-- Version: 2 -->
<!-- Last-Modified: 2010/06/10 14:56:40 -->
<!-- Author: cmarqu -->

 * icon rotation: could also be used for amenity=viewpoint when tagged with viewing angles
 * SVG icons: allow replacing colors (e.g. color a black icon in blue); have an alpha parameter
 * move icon a bit if it would collide with others
 * replace an already placed icon with a collection icon when there is another one to be shown right there
 * push lines apart so that there is a minimum distance between them
 * be able to construct file names from tag values in XML (e.g. "symbol_file=parking.svg" should be mapped to e.g. ~/mapnik/parking.svg or http://example.com/parking.svg). Right now, people resort  to generating XML styles by a script.
 * (might need sanitizing/sandboxing to prevent malicious icons in the URL case)
 * when there is a very curvy road, place the name along a smoothed line (when the text is not centered to the line but with a dy)
 * multi-line text constructed from several tags, e.g. for peak name and height (can be done when you accept the same styling for these text fragments)
 * stronger coupling between icon and text (maybe similar to the ShieldSymbolizer?) so that manual text dy tweaking is not required anymore (want to be able to say: "place this icon in size 20x20  and put the text in size 12pt five pixels below it")
 * collapsing of little small areas with the same tags into a single big one (for e.g. a big forest), so that e.g. the name is drawn only once
 * be able to suppress automatic text rotation (per style or layer) - contour lines should always be displayed so that the base line of the text points to the lower ground
 * underlined text (for e.g. capitals)
 * sometimes, peak names drawn in a half circle, would be cool if Mapnik could do that as well
