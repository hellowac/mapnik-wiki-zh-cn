<!-- Name: LearningMapnik -->
<!-- Version: 7 -->
<!-- Last-Modified: 2010/05/02 11:05:01 -->
<!-- Author: springmeyer -->
# Learning Mapnik

== Background == 

*How to Approach Map Design*
 * MapDesign -- use Mapnik to design better looking maps!

*How to understand GIS Concepts*
 * [wiki:IntroductionToGIS] -- a brief intro to the world of mapping systems
 * Projections, geodetics, and polygons, oh my...

## Core Topics

*How to Style your Maps*
 * SymbologySupport

*How to combine Map styles and Layers*
 * See the MapnikTutorials
 * XML Mapfile details [wiki:XMLConfigReference]

*How to read in data*
 * PluginArchitecture

*How to use the Mapnik Python Bindings*
 * See the python api docs here: http://media.mapnik.org/api_docs/python/
   * You can generate these docs yourself too, look at source:trunk/docs/epydoc_config/readme.txt
 * Check out the MapnikTutorials and  the references at ExampleCode
 * Study applications like Cascadenik or Nik2img at http://mapnik-utils.googlecode.com/

*How to use Custom Fonts*
 * UsingCustomFonts

== Performance == 

[wiki:OptimizeRenderingWithPostGIS] -- Optimize rendering speed and simplify the stylesheet with PostGIS


## Advanced Topics
 
MapnikRenderers -- Render with AGG or Cairo

LabelingSupport -- Discover the intricacies of label placement.

OutputFormats -- Which format to use based on speed, quality, and rendering tradeoffs.

[Generating Contours](http://wiki.openstreetmap.org/index.php/Contours) - Using Mapnik with GDAL to build contours of the world.

ManagingLargeXmlFiles -- Do things once and only once using XML entities.

[Hooking up Mapnik to PostGIS](/wiki:PostGIS/)

[Scale and Scale denominators](/wiki:ScaleAndPpi/) -- Scale, Projection and Pixels Per Inch: what it means for determining the scale of your rendered and printed maps.

ModServer -- An experimental mod_python server for Mapnik

[wiki:IntegrateWithWxPython] -- Demonstrate how to integrate mapnik with wxPython

[wiki:FontSet] -- Fallback fonts support

MapnikReferences -- Various other resources related to Mapnik and Mapping